# 🛡️ Lab07 – Firewall Configuration with UFW, Packet Tracing, and AI-Assisted Rule Design

**Course:** SPR100 - Introduction to Computer Systems and Security  
**Lab Number:** Lab07  
**Weight:** 6% of final grade  
**Duration:** Until Final Test Date  
**Due Date:** 11:59 PM of the Final Test Date 

---

## 📚 Recommended References

Please skim or keep these open while you work. Use them to understand what each command is doing and why.

- UFW (Uncomplicated Firewall) user guide:  
  - `man ufw`  
  - Ubuntu docs: [`https://help.ubuntu.com/community/UFW`](https://help.ubuntu.com/community/UFW)
- iptables & netfilter background (optional but helpful):  
  - [`https://www.netfilter.org/documentation/`](https://www.netfilter.org/documentation/)
- VMware Workstation Pro networking overview:  
  - Bridged/NAT/Host-only networking docs from VMware
- tshark manual (for packet inspection):  
  - [`https://www.wireshark.org/docs/man-pages/tshark.html`](https://www.wireshark.org/docs/man-pages/tshark.html)
- (Optional) AI prompt-writing basics:  
  - Any reputable “prompt engineering” guide focusing on *step-by-step instructions* and *constraints*

---

## 🎯 Learning Objectives

By the end of this lab, you will be able to:

1. Configure Ubuntu’s `ufw` firewall to allow, deny, and limit traffic on specific ports and IP ranges.
2. Design and test firewall rule sets using **two Ubuntu VMs** on VMware Workstation Pro with an appropriate virtual network.
3. Use `tshark` to observe how packets are handled (accepted, blocked, or dropped) by firewall rules.
4. Formulate effective AI prompts to generate and refine complex firewall rule sets safely and clearly.
5. Document firewall configurations and explain the security rationale behind each rule.

This lab builds on your Ubuntu VM from earlier labs, your networking skills from Lab06, and your understanding of services/ports from previous exercises.

---

## 📋 Pre-Lab Requirements

### Required Software and Setup

- Two Ubuntu VMs in VMware Workstation Pro:
  - **VM1:** “Firewall VM” – where you will configure `ufw`
  - **VM2:** “Client VM” – where you will generate test traffic
- `ufw` installed and enabled on **VM1** (Ubuntu usually includes it by default):

```bash
sudo apt update
sudo apt install -y ufw
```

- `tshark` installed on **VM1** (and optionally on VM2):

```bash
sudo DEBIAN_FRONTEND=noninteractive apt install -y tshark
```

### VMware Networking

- In VMware Workstation Pro, configure **both** VMs to be on the **same virtual network**, for example:
  - Same **NAT** network, or  
  - Same **Host-only** network
- Verify that:
  - Both VMs receive IP addresses in the same subnet.
  - You can `ping` from VM2 (Client) to VM1 (Firewall) *before* enabling restrictive firewall rules.

> **Reminder:** Only test on your own VMs and networks you control. Do **not** scan or firewall-block networks you are not authorized to manage.

---

## 🚀 Lab Activities

0) **Create a workspace and work from there on each VM (especially VM1):**

```bash
mkdir -p ~/SPR100_Labs/Lab07/work
cd ~/SPR100_Labs/Lab07/work
```

- Keep notes and configuration snippets in this folder as you go.

---

### Part 1: Configure UFW Firewall Rules on Ubuntu (VM1) (40 minutes)

Goal: Enable and configure `ufw` on VM1 and test connectivity from VM2.

> **CRITICAL WARNING:**
> 1. **IP Addresses:** The examples below use `192.168.56.x`. You **MUST** replace these with your actual VM IP addresses (check using `ip addr`).
> 2. **Interfaces:** Examples use `eth0`. Your interface might be `ens33` or `ens160`. Check using `ip addr` or `tshark -D` and use the correct name.

#### 1) Define basic rules (Prevent Lockout)

**Crucial Step:** You must define your "allow" rules **before** enabling the firewall. If you enable the firewall first while using SSH, you will be locked out immediately.

On **VM1**, add rules to control SSH (if needed), HTTP, and ICMP:

```bash
# Set default policies first
sudo ufw default deny incoming
sudo ufw default allow outgoing

# Allow SSH (CRITICAL if you are connected remotely!)
sudo ufw allow 22/tcp

# Allow HTTP (for testing later)
sudo ufw allow 80/tcp

# Block telnet (bad practice example)
sudo ufw deny 23/tcp
```

- Think:
  - Why is `deny 23/tcp` considered a best practice?
  - What is the difference between `allow 80/tcp` and `allow from 192.168.1.50 to any port 80 proto tcp`?

#### 2) Enable UFW

Now that you have allowed SSH, it is safe to enable the firewall.

```bash
sudo ufw enable
# Press 'y' to confirm if prompted
```

Inspect the status:

```bash
sudo ufw status numbered
```

- Record:
  - The status output showing your active rules.

#### 3) Source-specific rules and best practices

Design some **source-specific** rules on VM1, assuming:

- VM1 (Firewall) IP: e.g., `192.168.56.10`
- VM2 (Client) IP: e.g., `192.168.56.11`

Examples:

```bash
# Allow HTTP only from VM2
sudo ufw allow from 192.168.56.11 to any port 80 proto tcp

# Block everything from an example “untrusted” IP
sudo ufw deny from 192.168.56.99
```

Best practices to discuss and apply:

- Start from a **default deny** stance and explicitly allow what is needed:

```bash
sudo ufw default deny incoming
sudo ufw default allow outgoing
```

- Avoid duplicate/conflicting rules; periodically review with:

```bash
sudo ufw status numbered
```

- Remove rules you no longer need:

```bash
sudo ufw delete <rule-number>
```

- Record:
  - At least **3–5 rules** you created and why (what risk or requirement each addresses).

#### 4) Test rules from VM2 (Client VM)

On **VM2**, use `ping`, `curl`, or other tools to verify your rules:

```bash
# Replace IP with VM1's IP
ping -c 4 192.168.56.10

curl -v http://192.168.56.10/        # if you have a web server or simple Python HTTP server
```

**Required Setup:** On VM1, you must run a simple HTTP server for testing to distinguish between "Connection Refused" (Service Down) and "Filtered" (Firewall Blocked).

**Note:** Port 80 is a privileged port, so you need `sudo`.

```bash
cd ~/SPR100_Labs/Lab07/work
sudo python3 -m http.server 80
```

- Test scenarios:
  - From VM2 (allowed IP) to port 80: does it succeed?
  - Change the rule to allow only a **different** IP and see the effect.
  - Try accessing a port that is not allowed.

- Record:
  - Which tests **succeeded** and which **failed**, and how that matches your `ufw` rules.
  - Any surprising results (e.g., something allowed that you thought was blocked).

Reflection for Part 1:

- How does `ufw` simplify firewall management compared to raw `iptables`?
- Why is “default deny incoming, allow outgoing” a common baseline?
- What could go wrong if you enable `ufw` on a remote server without planning SSH rules?

---

### Part 2: Use TShark to Observe Packets and Firewall Effects (35 minutes)

Goal: Use `tshark` on VM1 to see which packets arrive and whether your firewall rules are effective.

#### 1) Capture traffic with and without restrictive rules

On **VM1**:

1. Pick the network interface used between VM1 and VM2 (e.g., `eth0`, `ens33`, or similar):

```bash
tshark -D
```

2. Start a short capture **before** adding a new restrictive rule:

```bash
sudo tshark -i eth0 -a duration:15 -w lab07_before_ufw.pcapng  # adjust interface
```

3. During those 15 seconds, on **VM2**:

```bash
ping -c 5 <VM1_IP>
curl -s -o /dev/null -w "%{http_code}\n" http://<VM1_IP>/
```

- Record:
  - Whether ping and HTTP succeed.
  - Basic stats from:

```bash
tshark -r lab07_before_ufw.pcapng -q -z io,stat,1
```

#### 2) Apply a new blocking rule and capture again

On **VM1**, block all incoming traffic from VM2’s IP:

```bash
sudo ufw deny from <VM2_IP>
sudo ufw status numbered
```

Now run another capture:

```bash
sudo tshark -i eth0 -a duration:15 -w lab07_after_ufw.pcapng
```

During this time, on **VM2**:

```bash
ping -c 5 <VM1_IP>
curl -s -o /dev/null -w "%{http_code}\n" http://<VM1_IP>/
```

- Compare:
  - Does `ping` still get replies?
  - Does HTTP still work?

Use `tshark` display filters to study packets:

```bash
# ICMP packets
tshark -r lab07_after_ufw.pcapng -Y "icmp" -T fields -e frame.number -e ip.src -e ip.dst | head

# HTTP (TCP/80)
tshark -r lab07_after_ufw.pcapng -Y "tcp.port==80" \
  -T fields -e frame.number -e ip.src -e ip.dst -e tcp.flags | head
```

- Think:
  - Do you still see ICMP echo *requests* from VM2 but no *replies* from VM1?
  - How does this pattern reflect the firewall’s behavior?
  - What differences do you see in the HTTP traffic before vs after the rule?

#### 3) Export structured fields to CSV

Create a CSV summarizing packets for analysis:

```bash
tshark -r lab07_after_ufw.pcapng \
  -T fields -E header=y -E separator=, \
  -e frame.time_relative -e _ws.col.Protocol \
  -e ip.src -e ip.dst -e icmp.type -e tcp.srcport -e tcp.dstport \
  > lab07_after_ufw_fields.csv
```

- Open the CSV and identify:
  - Which rows show blocked ICMP (e.g., only requests, no replies)?
  - Which rows show allowed TCP/80 traffic?

Reflection for Part 2:

- How can `tshark` demonstrate that a firewall rule is working, *even if you only see one side* of the conversation?
- Why is it useful to export to CSV for later analysis (e.g., with spreadsheets or scripts)?
- What patterns (e.g., missing replies, RSTs) might indicate blocked or refused connections?

---

### Part 3: Using AI to Design Complex Firewall Rule Sets (35 minutes)

Goal: Learn how to describe requirements clearly to an AI assistant so it can propose a safe, coherent `ufw` rule set.

> **Important:** In the *real* final and midterm, AI assistants may be **disallowed**. This part is about learning **how** to communicate with AI *when allowed* in real-world work, not during closed-book assessments.

#### 1) Principles of good AI prompts for firewall rules

To get reliable code from AI, it is helpful to follow "Prompt Engineering" best practices. A widely cited framework involves defining:
1. **Persona** (Who is the AI acting as?)
2. **Context** (What is the environment?)
3. **Task** (What exactly needs to be done?)
4. **Constraints** (What must NOT happen? What limits exist?)
5. **Format** (How should the output look?)

*Reference: [OpenAI Prompt Engineering Guide - Tactics](https://platform.openai.com/docs/guides/prompt-engineering/tactics)*

**Example "Rigorous" Prompt:**

> **Persona:** Act as a Senior Linux System Administrator.
> 
> **Context:** I am configuring a firewall on an Ubuntu 22.04 server using `ufw` (Uncomplicated Firewall). My server IP is `192.168.56.10`. The client IP is `192.168.56.11`.
> 
> **Task:** Generate the exact `ufw` commands to configure the firewall to meet these requirements:
> - Default policy: Deny all incoming, allow all outgoing.
> - SSH (Port 22/tcp): Allow ONLY from the client IP (`192.168.56.11`).
> - HTTP (Port 80/tcp) and HTTPS (Port 443/tcp): Allow from ANY IP.
> - Block all other incoming traffic.
> 
> **Constraints:**
> - Do NOT use raw `iptables` commands; use only `ufw`.
> - Include comments explaining each rule.
> - Ensure the commands do not flush existing SSH connections if run in sequence.
> 
> **Format:** Provide the commands in a single bash script block.

- Think:
  - Why is it safer to specify "Do NOT use raw iptables"?
  - How does adding the "Context" (IP addresses) prevent the AI from giving you generic `0.0.0.0/0` rules that might be too permissive?

#### 2) Translate AI suggestions into a safe test plan

Even if AI gives you a rule set, you must:

- **Review** each rule line by line.
- Ensure you **do not remove your own access** (e.g., SSH).
- Apply rules step by step, testing between steps.

Practice task (on paper / in your README, not by actually using AI in the lab):

1. Write a detailed prompt for the following scenario using the **Persona/Context/Task/Constraints/Format** structure:
   - **Context:** VM1 (Server) and VM2 (Client) are on the same subnet.
   - **Task:** Configure VM1 to:
     - Allow SSH on port 22 (only from VM2).
     - Allow HTTP on port 8080 (from the whole subnet).
     - Allow DNS server on port 53/udp (from subnet `192.168.56.0/24` only).
   - **Constraints:** Default deny incoming, allow outgoing; log all denied packets.
2. In your own words, draft what you **expect** the AI’s response to include:
   - Example `ufw` commands.
   - Any logging or rate-limiting rules.
3. (Optional, outside test conditions) Later, you can try this prompt with an AI and compare the results to your expectations.

#### 3) Design your own complex rule set

For your **final task** in this lab, design a more complex rule set **yourself**, as if you were the AI:

Scenario:

- You are protecting a small internal application server (VM1) with IP `192.168.56.10`.
- Requirements:
  - SSH (22/tcp) only from `192.168.56.11` (admin VM2).
  - HTTP (80/tcp) only from `192.168.56.0/24`.
  - Block all access from IP `192.168.56.50`.
  - Allow DNS queries (53/udp) from local subnet, but **rate-limit** repeated attempts from any single host.
  - Default: deny incoming, allow outgoing, log denied traffic.

Tasks:

1. In your README, write the **prompt** you would give an AI for this scenario.
2. Then, **without** using AI, write the actual `ufw` commands you would expect to see.
3. Optionally, implement and test a subset of these rules on VM1 and verify with:
   - `sudo ufw status numbered`
   - `ping`, `curl`, `dig` from VM2
   - `tshark` captures similar to Part 2

Reflection for Part 3:

- How does writing a good AI prompt force you to think clearly about requirements?
- What are the risks of blindly copy-pasting firewall rules from any assistant (human or AI)?
- How can you combine AI assistance with your own `tshark` and testing skills to safely deploy rules?

---

## 🧪 Deliverables

Submit a `README.md` in `Labs/Lab07/` that includes:

- Commands you ran on VM1 and VM2 (trim outputs to the most relevant lines).
- Text snippets showing:
  - `ufw status numbered` before and after your rules.
  - `tshark` output / CSV excerpts demonstrating allowed vs blocked traffic.
- Clear explanations (in your own words) of:
  - Your final `ufw` rule set and what each major rule does.
  - How you verified rule behavior using VM2 and `tshark`.
  - One example of a good AI prompt for firewall rules, plus your analysis of why it is good.

### Files to Save in `~/SPR100_Labs/Lab07/work/` (Suggested Names)

- `lab07_before_ufw.pcapng`
- `lab07_after_ufw.pcapng`
- `lab07_after_ufw_fields.csv`
- Any additional captures or scripts you created for testing

> Keep files reasonably small (short capture durations) so your repository stays under size limits.

---

## 📤 Submission Instructions

Follow the same submission flow as previous labs and the Labs root guidelines:

1. Place your lab `README.md` and any artifacts in `Labs/Lab07/`
2. Commit and push before the deadline

Suggested commit message:  
“Complete Lab07 – UFW Firewall and Packet Analysis”

---


