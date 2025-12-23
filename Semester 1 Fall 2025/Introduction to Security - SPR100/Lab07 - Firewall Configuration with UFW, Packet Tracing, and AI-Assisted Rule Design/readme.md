< Content-type: text/html; charset=utf-8 
< Content-Length: 297
<
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd"> 
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>Directory listing for /</title>
</head>
<body>
<h1>Directory listing for /</h1>
<hr>
<ul>
</ul>
<hr>
</body>
</html>
* Closing connection
```
--- 
### Ping result vs rules
- Ping from VM2 initially worked because ICMP traffic is not blocked by default.
After adding the deny rule for VM2, ping stopped receiving replies, which matches the rule that blocks all traffic from 192.168.159.140.
### HTTP result vs rules
- HTTP on port 80 worked at first because I allowed VM2 to access port 80.
After I blocked VM2, curl failed because the firewall no longer allowed traffic from that IP.
### Any surprising behaviour
- One surprising behaviour was that ICMP (ping) cannot be restricted to a specific IP using UFW rules. ICMP is handled differently, and UFW 
does not support proto icmp with “from <IP>”.
Also, curl showed no response instead of a clear “blocked” message, because the firewall silently dropped the packets rather than rejecting 
them.
## Part 1 – Reflection
### How does ufw simplify firewall management compared to raw iptables?
- UFW is easier because it uses simple commands like “allow” and “deny” instead of long iptables chains and rules. 
With ufw, I don’t need to understand the full syntax of netfilter or write complex match conditions.
It also shows rules in a numbered list, which makes editing and deleting rules much simpler.
### Why is “default deny incoming, allow outgoing” a common baseline?
- Default-deny incoming protects the system by blocking all unsolicited traffic unless I explicitly allow it.
This reduces the attack surface and prevents unknown services from being exposed.
Allowing outgoing traffic ensures the server can still update packages, reach the internet, and function normally without extra rules.
### What could go wrong if you enable ufw on a remote server without planning SSH rules?
- If SSH is not allowed before enabling ufw, the firewall will block the existing SSH session and lock me out of the system. 
- I would lose remote access immediately and may need physical access or console access to fix the firewall.
- This is why the rule to allow port 22 must be created first before running ufw enable.
## Part 2: Use TShark to Observe Packets and Firewall Effects 
1) Capture BEFORE New Blocking Rule
On VM1:
```bash
$ tshark -D 
1. ens33
2. any
3. lo (Loopback)
4. bluetooth-monitor
5. nflog
6. nfqueue
7. dbus-system
8. dbus-session
9. ciscodump (Cisco remote capture)
10. dpauxmon (DisplayPort AUX channel monitor capture)
11. randpkt (Random packet generator)
12. sdjournal (systemd Journal Export)
13. sshdump (SSH remote capture)
14. udpdump (UDP Listener remote capture)
```
### $ sudo tshark -i <interface> -a duration:15 -w lab07_before_ufw.pcapng 
```bash
sbastani1@ubuntu:~/SPR100_Labs/Lab07/work$ tshark -i ens33 -a duration:15 -w lab07_before_ufw.pcapng 
Capturing on 'ens33'
 ** (tshark:5899) 06:27:19.580311 [Main MESSAGE] -- Capture started.
 ** (tshark:5899) 06:27:19.580379 [Main MESSAGE] -- File: "lab07_before_ufw.pcapng"
288
```


### During capture, on VM2:
#### $ ping -c 5 <VM1_IP> 
```bash
sbastani1@sbastani1-vm2:~$ ping -c 5 192.168.159.133
PING 192.168.159.133 (192.168.159.133) 56(84) bytes of data.
64 bytes from 192.168.159.133: icmp_seq=1 ttl=64 time=0.540 ms 
64 bytes from 192.168.159.133: icmp_seq=2 ttl=64 time=0.203 ms 
64 bytes from 192.168.159.133: icmp_seq=3 ttl=64 time=0.304 ms 
```
#### $ curl -s -o /dev/null -w "%{http_code}\n" http://<VM1_IP>/ 
```bash
sbastani1@sbastani1-vm2:~$
--- 192.168.159.133 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4079ms 
rtt min/avg/max/mdev = 0.203/0.306/0.540/0.123 ms
000
IO stats:
```
#### $ tshark -r lab07_before_ufw.pcapng -q -z io,stat,1 
```bash
sbastani1@ubuntu:~/SPR100_Labs/Lab07/work$ tshark -r lab07_before_ufw.pcapng -q -z io,stat,1
=============================
| IO Statistics |
| |
| Duration: 14.907185 secs | 
| Interval: 1 secs |
| |
| Col 1: Frames and bytes | 
|---------------------------|
| |1 |
| Interval | Frames | Bytes | 
|---------------------------|
| 0 <> 1 | 4 | 484 | 
| 1 <> 2 | 4 | 316 | 
| 2 <> 3 | 2 | 158 | 
| 3 <> 4 | 4 | 316 | 
| 4 <> 5 | 4 | 316 | 
| 5 <> 6 | 4 | 316 | 
| 6 <> 7 | 2 | 158 | 
| 7 <> 8 | 29 | 2896 | 
| 8 <> 9 | 77 | 7046 | 
| 9 <> 10 | 72 | 6426 | 
| 10 <> 11 | 54 | 4806 | 
| 11 <> 12 | 6 | 568 | 
| 12 <> 13 | 14 | 1578 | 
| 13 <> 14 | 8 | 520 | 
| 14 <> Dur| 4 | 316 | 
=============================
``` 
---
### 2) Apply Blocking Rule and Capture AGAIN
On VM1:
#### $ sudo ufw deny from <VM2_IP> 
#### $ sudo ufw status numbered 
```bash
sbastani1@ubuntu:~/SPR100_Labs/Lab07/work$ sudo ufw status numbered 
Status: active
To Action From
-- ------ ----
[ 1] 22/tcp ALLOW IN Anywhere
[ 2] 80/tcp ALLOW IN Anywhere
[ 3] 23/tcp DENY IN Anywhere
[ 4] 80/tcp ALLOW IN 192.168.159.140
[ 5] 22/tcp ALLOW IN 192.168.159.140
[ 6] Anywhere DENY IN 192.168.159.99
[ 7] Anywhere DENY IN 192.168.159.50
[ 8] Anywhere DENY IN 192.168.159.140
[ 9] 22/tcp (v6) ALLOW IN Anywhere (v6)
[10] 80/tcp (v6) ALLOW IN Anywhere (v6)
[11] 23/tcp (v6) DENY IN Anywhere (v6)
``` 
---
### New capture:
#### $ sudo tshark -i <interface> -a duration:15 -w lab07_after_ufw.pcapng 
```bash 
sbastani1@ubuntu:~/SPR100_Labs/Lab07/work$ tshark -i ens33 -a duration:15 -w lab07_before_ufw.pcapng 
Capturing on 'ens33'
 ** (tshark:5985) 06:34:55.531082 [Main MESSAGE] -- Capture started.
 ** (tshark:5985) 06:34:55.531143 [Main MESSAGE] -- File: "lab07_before_ufw.pcapng"


642 
``` 
---
## On VM2 during the second capture:
### $ ping -c 5 <VM1_IP> 
```bash
sbastani1@sbastani1-vm2:~$ ping -c 5 192.168.159.133
PING 192.168.159.133 (192.168.159.133) 56(84) bytes of data.
64 bytes from 192.168.159.133: icmp_seq=1 ttl=64 time=0.388 ms 
64 bytes from 192.168.159.133: icmp_seq=2 ttl=64 time=0.294 ms 
64 bytes from 192.168.159.133: icmp_seq=3 ttl=64 time=0.275 ms 
64 bytes from 192.168.159.133: icmp_seq=4 ttl=64 time=0.298 ms 
64 bytes from 192.168.159.133: icmp_seq=5 ttl=64 time=0.293 ms
--- 192.168.159.133 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4093ms 
rtt min/avg/max/mdev = 0.275/0.309/0.388/0.040 ms
```
---
### $ curl -s -o /dev/null -w "%{http_code}\n" http://<VM1_IP>/ 
```bash
sbastani1@sbastani1-vm2:~$ curl -s -o /dev/null -w "%{http_code}\n" http://192.168.159.133/ 
000
```
- Ping still worked after applying the deny rule. 
This is normal because UFW does not block ICMP using a simple deny rule. 
UFW mainly filters TCP/UDP ports, so ping continues unless a special ICMP rule 
is added. Since this was not required in the lab, the ping result is expected.
---
### 3) Inspect ICMP and TCP/80 in lab07_after_ufw.pcapng ICMP:
### $ tshark -r lab07_after_ufw.pcapng -Y "icmp" \
### > -T fields -e frame.number -e ip.src -e ip.dst | head 
```bash
sbastani1@ubuntu:~/SPR100_Labs/Lab07/work$ tshark -r lab07_after_ufw.pcapng -Y "icmp" \ 
> -T fields -e frame.number -e ip.src -e ip.dst | head
73 192.168.159.140 192.168.159.133
74 192.168.159.133 192.168.159.140
144 192.168.159.140 192.168.159.133
145 192.168.159.133 192.168.159.140
174 192.168.159.140 192.168.159.133
175 192.168.159.133 192.168.159.140
182 192.168.159.140 192.168.159.133
183 192.168.159.133 192.168.159.140
246 192.168.159.140 192.168.159.133
247 192.168.159.133 192.168.159.140
```
---
## TCP/80:
#### $ tshark -r lab07_after_ufw.pcapng -Y "tcp.port==80" \
#### > -T fields -e frame.number -e ip.src -e ip.dst -e tcp.flags | head 
```bash
sbastani1@ubuntu:~/SPR100_Labs/Lab07/work$ tshark -r lab07_after_ufw.pcapng -Y "tcp.port==80" \ 
> -T fields -e frame.number -e ip.src -e ip.dst -e tcp.flags | head
439 192.168.159.140 192.168.159.133 0x0002
440 192.168.159.133 192.168.159.140 0x0014
```
----
### 4) Export Structured Fields to CSV
#### RUN: $ tshark -r lab07_after_ufw.pcapng \
#### -T fields -E header=y -E separator=, \
#### -e frame.time_relative -e _ws.col.Protocol \
#### -e ip.src -e ip.dst -e icmp.type -e tcp.srcport -e tcp.dstport \
#### > lab07_after_ufw_fields.csv
----
### $ head lab07_after_ufw_fields.csv
```bash
sbastani1@ubuntu:~/SPR100_Labs/Lab07/work$ head lab07_after_ufw_fields.csv 
frame.time_relative,_ws.col.Protocol,ip.src,ip.dst,icmp.type,tcp.srcport,tcp.dstport 
0.000000000,SSH,192.168.159.133,192.168.159.1,,22,2522
0.045541529,TCP,192.168.159.1,192.168.159.133,,2522,22
0.725489297,SSH,192.168.159.133,192.168.159.1,,22,2522
0.771742850,TCP,192.168.159.1,192.168.159.133,,2522,22
0.975372936,SSH,192.168.159.1,192.168.159.140,,11472,22
0.975813684,SSH,192.168.159.140,192.168.159.1,,22,11472
1.004121638,SSH,192.168.159.1,192.168.159.140,,11472,22
1.004347722,SSH,192.168.159.140,192.168.159.1,,22,11472
1.034775886,SSH,192.168.159.1,192.168.159.140,,11472,22
```
---
### Part 2 – Reflection
#### How can tshark show that a firewall rule is working even if you only see one side of the conversation?
- tshark output shows what changed after a rule is applied. Even with only one side captured, the absence of replies to outbound requests 


indicates the firewall is enforcing the rule.
#### What patterns in ICMP and TCP did you see that indicated blocking or refusal (e.g., only echo requests, SYN + RST/ACK)?
- For ICMP (ping), I saw only echo requests and no echo replies after the deny rule.
For TCP on port 80, I saw SYN packets being sent, but no SYN/ACK responses. Sometimes I even saw a reset. 
Both patterns mean the connection was blocked or refused.
#### Why is exporting to CSV useful for later analysis?
- CSV files are easy to open in Excel or similar tools, which makes sorting and filtering packet data straightforward. It is faster to review 
traffic in a spreadsheet and keeps the lab evidence organized.
----
### Part 3: Using AI to Design Complex Firewall Rule Sets
1) Your AI Prompt (Persona / Context / Task / Constraints / Format) 
Write out your prompt for this scenario:
VM1 (Server) and VM2 (Client) on the same subnet. 
Requirements:
SSH (22) only from VM2
HTTP (8080) from whole subnet
DNS (53/udp) from 192.168.56.0/24
Default deny incoming, allow outgoing
Log denied packets 
---
# Prompt:
```bash
Persona:
Act as a Linux system admin.
Context:
I am setting up ufw on VM1 (192.168.159.133). VM2 is 192.168.159.140 and both VMs 
are on the 192.168.159.0/24 subnet.
Task:
Give me the ufw commands to:
- Allow SSH (22) only from VM2
- Allow HTTP on port 8080 from the whole subnet 
- Allow DNS (53/udp) from 192.168.159.0/24
- Default deny incoming and allow outgoing
- Log denied packets
Constraints:
- Use ufw only (no iptables)
- Commands must be safe to run in order
- Add simple comments explaining each rule
Format:
Give the answer as a clean bash command block. 
```
--- 
### 2) What You Expect AI to Return 
#### Expected ufw commands:
```bash
ufw default deny incoming 
ufw default allow outgoing
ufw allow from 192.168.159.140 to any port 22 proto tcp
ufw allow from 192.168.159.0/24 to any port 8080 proto tcp 
ufw allow from 192.168.159.0/24 to any port 53 proto udp
ufw logging on
```
---
#### Any logging or rate-limiting rules:
- The AI should enable logging so denied packets are visible.
- It may also suggest rate-limiting DNS (53/udp) to prevent excessive queries. For example, using:
- ufw limit 53/udp
- This helps slow down abuse without fully blocking the port.
----
### 3) Complex Rule Set You Design Yourself
#### Scenario:
- VM1: 192.168.56.10
- VM2: 192.168.56.11 (admin)


- Blocked IP: 192.168.56.50
- Subnet: 192.168.56.0/24
#### Requirements:
- SSH only from VM2
- HTTP only from subnet
- Block 192.168.56.50
- Allow DNS 53/udp from subnet, rate-limit if possible
- Default deny incoming, allow outgoing, log denied 
---
### a) Prompt You Would Give AI
```bash
Persona:
Act as a Linux firewall admin.
Context:
I am setting up ufw on VM1 (192.168.159.133). VM2 (192.168.159.140) is my admin 
machine. Both are in the 192.168.159.0/24 network.
Task:
Give me the ufw commands to:
- Allow SSH (22) only from VM2
- Allow HTTP (80) for the whole 192.168.159.0/24 subnet 
- Allow DNS (53/udp) for the subnet
- Block one IP (192.168.159.50)
- Default deny incoming, allow outgoing
- Log denied packets
- Add comments explaining each rule
Constraints:
- Use ufw only (no iptables)
- Commands must be safe to run in order 
- Do not break the current SSH session
Format:
Show the commands in a clean bash block. 
```
---
### b) UFW Commands YOU Would Use (No AI)
#### Default policies
- sudo ufw default deny incoming
- sudo ufw default allow outgoing
#### SSH from VM2 only
- sudo ufw allow from 192.168.56.11 to any port 22 proto tcp
#### HTTP from subnet
- sudo ufw allow from 192.168.56.0/24 to any port 80 proto tcp
#### Block specific IP
- sudo ufw deny from 192.168.56.50
#### DNS from subnet (and any rate-limit if used)
- sudo ufw allow from 192.168.56.0/24 to any port 53 proto udp
#### Logging
- sudo ufw logging on 
---
#### OUTPUTS:
```bash
sbastani1@ubuntu:~/SPR100_Labs/Lab07/work$ sudo ufw default deny incoming
[sudo] password for sbastani1:
Default incoming policy changed to 'deny'
(be sure to update your rules accordingly)
sbastani1@ubuntu:~/SPR100_Labs/Lab07/work$ sudo ufw default allow outgoing
Default outgoing policy changed to 'allow'
(be sure to update your rules accordingly)
sbastani1@ubuntu:~/SPR100_Labs/Lab07/work$ sudo ufw allow from 192.168.56.11 to any port 22 proto tcp 
Rule added
sbastani1@ubuntu:~/SPR100_Labs/Lab07/work$ sudo ufw allow from 192.168.56.0/24 to any port 80 proto tcp 
Rule added
sbastani1@ubuntu:~/SPR100_Labs/Lab07/work$ sudo ufw deny from 192.168.56.50
Rule added
sbastani1@ubuntu:~/SPR100_Labs/Lab07/work$ sudo ufw allow from 192.168.56.0/24 to any port 53 proto udp 
Rule added
sbastani1@ubuntu:~/SPR100_Labs/Lab07/work$ sudo ufw logging on
Logging enabled
```
---
### NOTES:



- Default deny incoming: blocks everything unless I allow it.
- Default allow outgoing: lets the server reach the internet normally.
- SSH from 192.168.159.140: only my admin VM can log in over SSH.
- HTTP from subnet: only devices in my local network can access the web server.
- Deny 192.168.159.50: blocks a suspicious or unwanted IP.
- DNS from subnet: only my LAN can use this VM for DNS.
- Rate-limit DNS: prevents abuse or flooding.
- Logging: useful for seeing what packets were denied.
---
### Part 3 – Reflection
#### How does writing a detailed AI prompt help you understand your own firewall requirements?
- Writing the prompt forces me to think clearly about exactly what the firewall needs to allow and block. Instead of guessing, I have to list 
every port, IP, and rule. It makes me realize what the server really needs to stay secure.
#### What are the risks of copy-pasting firewall rules from an assistant without testing?
- The rules might block something important, break SSH, or open ports I didn’t mean to expose. If I don’t test them myself, I could lock 
myself out or leave the system unsafe. AI can make mistakes, so testing is always important.
#### How can you combine AI suggestions with your own tshark tests to deploy rules safely?
- AI can help write the rules, and then I can use tshark to confirm if traffic is actually being allowed or blocked. tshark shows me real 
packets, so I can double-check that the rules behave the way I expect before trusting them.
# Final Reflection (Overall Lab)
#### What is the difference between capture filters (-f) and display filters (-Y)? Give one scenario for each.
- Capture filter (-f): decides what packets are recorded during capture. 
Example: only capture TCP packets going to port 80.
- Display filter (-Y): filters packets after they are already captured. 
Example: search inside the file for only ICMP packets.
#### How can you reliably identify TCP vs UDP traffic using tshark output/fields?
TCP packets show TCP flags (SYN, ACK, RST) and have fields like tcp.srcport. 
UDP packets show udp.srcport and have no flags.
Looking at the protocol column also helps (TCP vs UDP).
#### What can metadata (like ICMP type, TCP flags, DNS names) reveal even if you cannot see the payloads?
Metadata can show what kind of traffic is happening, which machine started the connection, and whether it succeeded or failed.
For example, ICMP type 8 means a ping request, SYN means a connection attempt, and DNS queries show what domain names are being looked up.
#### What ethical and legal boundaries must you respect when capturing and inspecting network traffic?
I should only capture traffic on networks that I own or have permission to test.
It’s not legal or ethical to sniff other people’s data without consent.
I should avoid collecting private information, and only use sniffing tools for school work or approved security testing. 
---
### Checklist:
 [x] lab07_before_ufw.pcapng
 [x] lab07_after_ufw.pcapng
 [x] lab07_after_ufw_fields.csv
 [x] README.md (this file)