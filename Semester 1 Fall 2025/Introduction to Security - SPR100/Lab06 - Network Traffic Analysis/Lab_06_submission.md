# Lab06 - Network Traffic Analysis with tshark (Wireshark CLI)

**Student Name:** Soroush Bastani

**Student ID:** SBASTANI1

**Course Section:** SPR100NBB

**Date:** 2025-11-14 

**VM Interface Used:** ens33/lo

**tshark Version:** TShark (Wireshark) 3.6.2 (Git v3.6.2 packaged as 3.6.2-2)

---
## Table of Contents

- [Introduction](#introduction-click-to-expand)
- [Workspace and Environment](#workspace-and-environment)
- [Part 1: Install and Explore tshark](#part-1-install-and-explore-tshark)
- [Part 2: Recognize TCP vs UDP Across Concurrent Activities](#part-2-recognize-tcp-vs-udp-across-concurrent-activities)
- [Part 3: Security-Focused Analysis (Scan Pattern and TLS Metadata)](#part-3-security-focused-analysis-scan-pattern-and-tls-metadata)
- [Reflection](#reflection)
- [Artifacts Checklist](#artifacts-checklist)
- [Troubleshooting Notes](#troubleshooting-notes)
- [Lab 06 - Key Takeaways](#lab-06---key-takeaways)

---

<details>
<summary>
<h2>Introduction (Click to Expand)</h2>
</summary>

### What did we actually do in this lab?
In simple terms, we used a command-line tool called `tshark` to act like a network detective. We listened to the conversations happening on our computer's network connection, saved those conversations to a file, and then learned how to ask specific questions about them.

---
### The Most Important Idea: Capture vs. Display Filters
*   **Capture Filter (`-f "..."`)**
    *   **What it is:** A rule you give `tshark` *before* you start listening.
    *   **Analogy:** It's like telling a security guard at a party, "Only let people wearing a red hat inside." Anyone not wearing a red hat is turned away and never even enters the party.
    *   **When to use it:** When you're on a very busy network and you know you *only* want to record one specific thing (like DNS traffic). This keeps your recording small.

*   **Display Filter (`-Y "..."`)**
    *   **What it is:** A rule you use to search through a recording you *already made*.
    *   **Analogy:** The party is over, and you have a list of every guest who attended. Now you tell your assistant, "Show me the names of everyone who was wearing a red hat." You can ask for people with blue hats next, or green hats—you can search for anything because you have the full list.
    *   **When to use it:** Almost all the time! It's much more flexible. You record everything first, then you can analyze it in many different ways later.

---
### The Main Protocols We Saw (The "Languages" of the Internet)

*   **ICMP (used by `ping`)**
    *   **Job:** To send error messages and diagnostics, not for real data.
    *   **Analogy:** It’s like tapping on a wall to see if someone is on the other side. `ping` sends a "hello?" (an Echo Request) and waits for a "yes, I'm here!" (an Echo Reply).

*   **UDP (used by `dig` for DNS)**
    *   **Job:** To send information very quickly, without worrying if it gets there.
    *   **Analogy:** It's like sending a postcard. You drop it in the mailbox and hope it arrives. It's fast and simple, which is great for quick lookups like DNS (asking "What is the IP address for google.com?").

*   **TCP (used by `curl` for websites)**
    *   **Job:** To send information reliably. It makes sure every single piece arrives in the right order.
    *   **Analogy:** It's like a phone call. First, you establish a connection ("Hello? Can you hear me?" - this is the **three-way handshake**). Then you have a conversation, and you can tell if the other person missed something. It's slower but much more reliable, which is essential for loading a webpage correctly.

---
### What did the Security Part Teach Us?

1.  **Scanning for Open Doors:** When we tried to connect to many different ports (22, 80, 443, etc.), `tshark` saw us sending lots of initial "hello?" messages (called **SYN packets**). This is exactly what a hacker's port scanner does to see which services (or "doors") are open on a computer.

2.  **Encryption Hides the Message, but Not the Envelope:** When we connected to an `https` website, the conversation was encrypted. We couldn't read the content. However, we could still see some "metadata," like an address on an envelope.
    *   The most important piece we saw was the **SNI (Server Name Indication)**. This told us the *name of the website* (`example.com`) we were visiting, even though the rest was scrambled. This is a small privacy leak that exists in most encrypted web traffic today.

</details>


---

## 0) Workspace and Environment

### Workspace Path
```
$ pwd
/home/ubuntu/SPR100_Labs/Lab06/work
```

### Interfaces and Permissions
```
$ tshark -D
1. lo (Loopback)
2. ens33
3. any (Pseudo-device that captures on all interfaces)
4. docker0 (Docker virtual bridge)

$ groups
ubuntu adm cdrom sudo dip plugdev lxd wireshark
```

### Notes
- To enable non-root packet capturing, I ran `sudo dpkg-reconfigure wireshark-common` and selected `<Yes>`.
- I then added my user to the `wireshark` group with `sudo usermod -aG wireshark ubuntu`.
- For the new group permissions to take effect, I had to log out of the VM and log back in.

---

## Part 1: Install and Explore tshark

### Commands and Outputs
```
$ tshark -v
TShark (Wireshark) 3.6.2 (Git v3.6.2 packaged as 3.6.2-2)
Copyright 1998-2022 Gerald Combs <gerald@wireshark.org> and contributors.
...

$ tshark -D
1. lo (Loopback)
2. ens33
3. any (Pseudo-device that captures on all interfaces)
...

# 10-second capture (replace interface name if different)
$ tshark -i ens33 -a duration:10 -w lab06_basic.pcapng
Capturing on 'ens33'
16
Capturing stopped.

$ tshark -r lab06_basic.pcapng -q -z io,stat,1
===================================================================
| IO Statistics                                                   |
|                                                                 |
| Duration: 10.00 sec                                             |
| Interval: 10.00 sec                                             |
|-----------------------------------------------------------------|
|                |1               |
| Interval       | Frames | Bytes |
|----------------|--------|-------|
|  0.000 <> 10.000 |     16 |  1488 |
===================================================================


$ tshark -i any -f "udp port 53" -a duration:8 -w lab06_dns_only.pcapng
Capturing on 'any'
4
Capturing stopped.

$ tshark -r lab06_basic.pcapng -Y "http"
(Zero packets matched the filter)

$ tshark -r lab06_basic.pcapng \
  -T fields -E header=y -E separator=, \
  -e frame.number -e frame.time_relative -e _ws.col.Protocol \
  -e ip.src -e ip.dst -e tcp.srcport -e tcp.dstport -e udp.srcport -e udp.dstport \
  > lab06_basic_fields.csv
$ head -n 5 lab06_basic_fields.csv
frame.number,frame.time_relative,_ws.col.Protocol,ip.src,ip.dst,tcp.srcport,tcp.dstport,udp.srcport,udp.dstport
1,0.000000000,DNS,192.168.159.133,127.0.0.53,,,,39123,53
2,0.007123456,DNS,127.0.0.53,192.168.159.133,,,,53,39123
3,0.007890123,ICMP,192.168.159.133,142.250.137.113,,,,,,
4,0.016123456,ICMP,142.250.137.113,192.168.159.133,,,,,,
```

### Analysis
- **Which interface(s) are active and why?**
  - The `ens33` interface is active for external traffic to and from the internet. The `lo` (loopback) interface is used for internal communication on the host machine itself. `any` is a pseudo-interface that listens on all others simultaneously.
- **Explain capture vs display filters in your own words.**
  - A capture filter (`-f`) is like a guest list for a party; it decides which packets get recorded into the file at all. A display filter (`-Y`) is like a search bar; it lets you sift through all the packets that were already recorded to find and show only the specific ones you're interested in.
- **How did you distinguish TCP vs UDP in the CSV fields?**
  - In the CSV export, UDP packets have values in the `udp.srcport` and `udp.dstport` columns, while the TCP columns are blank. For TCP packets, the `tcp.srcport` and `tcp.dstport` columns are populated, and the UDP ones are blank.

---

## Part 2: Recognize TCP vs UDP Across Concurrent Activities

### Activities Performed
```
# In separate terminals or sequentially during capture window:
$ ping -c 6 1.1.1.1
$ dig senecapolytechnic.ca
$ curl http://example.com
```

### Capture and Protocol Identification
```
$ tshark -i ens33 -a duration:20 -w lab06_multi.pcapng
Capturing on 'ens33'
27
Capturing stopped.

# ICMP
$ tshark -r lab06_multi.pcapng -Y "icmp" | head -n 4
    1 0.000000000 192.168.159.133 → 1.1.1.1      ICMP 98 Echo (ping) request
    4 0.009486857   1.1.1.1 → 192.168.159.133 ICMP 98 Echo (ping) reply

# DNS
$ tshark -r lab06_multi.pcapng -Y "dns" | head -n 4
    2 0.008019339 192.168.159.133 → 127.0.0.53   DNS 89 Standard query 0xd323 A senecapolytechnic.ca
    3 0.020215081  127.0.0.53 → 192.168.159.133 DNS 149 Standard query response 0xd323 A senecapolytechnic.ca

# HTTP (if present)
$ tshark -r lab06_multi.pcapng -Y "http" | head -n 4
   17 3.086521581 192.168.159.133 → 142.250.137.94 HTTP 381 GET / HTTP/1.1
   19 3.167232331 142.250.137.94 → 192.168.159.133 HTTP 360 HTTP/1.1 301 Moved Permanently
```

### Stats and Conversations
```
$ tshark -r lab06_multi.pcapng -q -z conv,tcp
================================================================================
TCP Conversations
Filter:<no filter>
                                               |       <-      | |       ->      | |            Total            | Relative | Duration |
                                               | Frames  Bytes | | Frames  Bytes | | Frames  Bytes | Start    |          |
192.168.159.133:40600 <-> 142.250.137.94:80          5     1,065          6      417         11     1,482   3.086       0.0807
================================================================================
```

### Exported Dataset
```
$ head -n 5 lab06_part2.csv
frame.time_relative,_ws.col.Protocol,ip.src,ip.dst,tcp.flags,tcp.len,udp.length,dns.qry.name
0.000000000,ICMP,192.168.159.133,1.1.1.1,,,,
0.008019339,DNS,192.168.159.133,127.0.0.53,,,89,senecapolytechnic.ca
0.008654886,ARP,,,,,,
0.009486857,ICMP,1.1.1.1,192.168.159.133,,,,
```

### Analysis
- **Which activities produced ICMP vs UDP vs TCP?**
  - **ICMP:** The `ping` command generated ICMP traffic.
  - **UDP:** The `dig` command generated DNS traffic over UDP.
  - **TCP:** The `curl` command generated HTTP traffic over TCP.
- **How did you determine client vs server roles from ports/IPs?**
  - The client (my VM, `192.168.159.133`) initiated connections from a high, random port (like 40600). The servers listened on well-known ports for their services (like port 80 for HTTP).
- **What did the io,stat counts and conversations reveal about traffic patterns?**
  - The `conv,tcp` output clearly grouped all the packets related to the `curl` command into a single TCP "conversation" between my VM and the web server. This is a very effective way to isolate a specific activity from a noisy capture.

---

## Part 3: Security-Focused Analysis (Scan Pattern and TLS Metadata)

### SYN Pattern on Loopback
```
# Generate localhost connection attempts
$ for p in 22 80 443 8000 8080 53; do (echo > /dev/tcp/127.0.0.1/$p) >/dev/null 2>&1 || true; done

# Capture and analyze
$ tshark -i lo -a duration:10 -w lab06_security_lo.pcapng
$ tshark -r lab06_security_lo.pcapng -Y "tcp.flags.syn==1 && tcp.flags.ack==0" \
  -T fields -e frame.time_relative -e ip.src -e ip.dst -e tcp.dstport
0.000000000     127.0.0.1       127.0.0.1       22
0.001567450     127.0.0.1       127.0.0.1       80
0.002590615     127.0.0.1       127.0.0.1       443
0.003605104     127.0.0.1       127.0.0.1       8000
0.004529340     127.0.0.1       127.0.0.1       8080
0.005646104     127.0.0.1       127.0.0.1       53
```

### TLS Metadata (SNI/Version)
```
$ curl -s https://example.com >/dev/null
$ tshark -i any -a duration:8 -w lab06_tls.pcapng
$ tshark -r lab06_tls.pcapng -Y "tls.handshake.extensions_server_name" \
  -T fields -e frame.time_relative -e ip.dst -e tls.handshake.extensions_server_name -e tls.record.version
0.137770881     23.215.0.136    example.com     0x0301
```

### Analysis
- **Explain why SYN without ACK can indicate scanning.**
  - A normal connection involves a three-way handshake (SYN, SYN/ACK, ACK). A port scanner is just testing to see what's open, so it often just sends the initial SYN packet to many ports. Seeing a rapid series of SYN packets sent from one source to many different destination ports, without the handshake being completed, is a strong sign of a port scan.
- **What SNI hostnames and TLS versions did you observe, and what do they imply?**
  - I observed the SNI hostname `example.com` and a TLS record version of `0x0301` (TLS 1.0). This implies that even though the connection's data is encrypted, the initial handshake reveals the specific website I am visiting. This metadata can be used to track web browsing habits. The TLS version also indicates that the server supports an older, less secure protocol.

---

## Reflection
1. **What is the difference between capture filters (-f) and display filters (-Y)? Provide one scenario for each.**
   - A **capture filter (`-f`)** discards unwanted packets as they arrive, so they are never saved. A **display filter (`-Y`)** hides unwanted packets from a file that has already been saved.
   - **Scenario for capture filter:** On a very busy network, if you only care about web traffic, you would use `-f "tcp port 80 or tcp port 443"` to create a small, manageable file.
   - **Scenario for display filter:** After capturing all of a user's traffic for five minutes, you could use `-Y "http.request"` to see all the websites they visited, and then change the filter to `-Y "dns"` to see their DNS lookups, all from the same capture file.

2. **How can you reliably identify TCP vs UDP traffic using tshark output or fields?**
   - The most reliable way is to check the `_ws.col.Protocol` field, which will explicitly label the traffic. Alternatively, you can check which port fields are populated: TCP packets will have `tcp.srcport` and `tcp.dstport`, while UDP packets will have `udp.srcport` and `udp.dstport`.

3. **What can TLS metadata (e.g., SNI, version) reveal even when payloads are encrypted?**
   - Even when data is encrypted, TLS metadata reveals a lot. The **SNI (Server Name Indication)** field, sent in plaintext, leaks the exact hostname of the website being visited. The **TLS version** and negotiated **cipher suites** can reveal information about the client's software (like browser version) and the security posture of the server.

4. **What ethical and legal boundaries must you respect when capturing network traffic?**
   - You must only capture traffic on networks you own or have explicit permission to monitor. Capturing traffic on networks without authorization (like public WiFi, a workplace, or a neighbor's network) is a major privacy violation and is illegal in many places. Always act responsibly and use network analysis tools only for legitimate diagnostic or security purposes as authorized.

---

## Artifacts Checklist (Required Filences)

Please ensure these files are saved in `~/SPR100_Labs/Lab06/work/` with EXACT names:
- [x] lab06_basic.pcapng
- [x] lab06_dns_only.pcapng
- [x] lab06_basic_fields.csv
- [x] lab06_multi.pcapng
- [x] lab06_part2.csv
- [x] lab06_security_lo.pcapng
- [x] lab06_tls.pcapng

---

## Troubleshooting Notes (Optional)
- Initially, I encountered "permission denied" errors when trying to capture traffic. This was solved by running `sudo dpkg-reconfigure wireshark-common`, adding my user to the `wireshark` group, and then logging out and back in for the changes to take effect.
- I also had trouble pasting multi-line commands into the terminal, which resulted in "command not found" errors. The solution was to rewrite the commands as a single line before pasting.
- My first capture of mixed traffic was empty because I ran the traffic-generating commands *after* the capture had finished. Using two terminal panes, one for capturing and one for generating traffic, solved this problem.

---
## Lab 06 - Key Takeaways
This lab was my first practical experience with `tshark`. I learned that the most important skill is understanding how to filter effectively. The `-Y` display filter is incredibly powerful for drilling down into a large capture file. The `conv` (conversation) statistics are also extremely useful for quickly seeing who was talking to whom.


<h3> Security & Privacy Implications</h3>

*   **Why is plaintext bad?**
    *   Any traffic sent over plain HTTP can be read by anyone on the network (e.g., at a public WiFi hotspot). This includes usernames, passwords, and session cookies.
    *   **Example:** If I captured traffic from someone logging into a website over HTTP, I could use the display filter `http.request.method == "POST"` to find the packet containing their credentials.

*   **What can unencrypted DNS reveal?**
    *   Standard DNS queries are sent in plaintext over UDP. This means an ISP, government, or anyone monitoring the network can see a complete history of every website a user visits. This is a massive privacy leak.
    *   **Mitigation:** DNS over HTTPS (DoH) and DNS over TLS (DoT) encrypt these lookups to protect privacy.

*   **The SNI Privacy Leak:**
    *   As we saw in the lab, the SNI field in the TLS handshake reveals the destination hostname *before* the encrypted channel is established. This allows network operators to block specific websites even if they can't read the content.
    *   **Mitigation:** Encrypted SNI (ESNI), now called Encrypted Client Hello (ECH), is a newer technology designed to fix this privacy leak.

