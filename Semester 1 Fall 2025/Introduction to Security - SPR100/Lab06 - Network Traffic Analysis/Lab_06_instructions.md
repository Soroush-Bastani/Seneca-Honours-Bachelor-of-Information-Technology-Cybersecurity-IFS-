# 🌐 Lab06 - Network Traffic Analysis with tshark (Wireshark CLI)

**Course:** SPR100 - Introduction to Computer Systems and Security  
**Lab Number:** Lab06  
**Weight:** 6% of final grade  
**Duration:** Two weeks: this lab runs over two lab sessions, each lasting 90 minutes  
**Due Date:** [Insert due date] (11:59 PM before the start of the next lab session)

---

## 📚 Recommended References

Please skim or keep these open while you work. Use them to understand what each command is doing and why.
- tshark manual (official): [https://www.wireshark.org/docs/man-pages/tshark.html](https://www.wireshark.org/docs/man-pages/tshark.html)
- Wireshark Display Filter Reference (official): [https://www.wireshark.org/docs/dfref/](https://www.wireshark.org/docs/dfref/)
- Wireshark User’s Guide: [https://www.wireshark.org/docs/wsug_html_chunked/](https://www.wireshark.org/docs/wsug_html_chunked/)
- Capture filters (BPF) primer: [https://wiki.wireshark.org/CaptureFilters](https://wiki.wireshark.org/CaptureFilters)
- Display filters basics: [https://wiki.wireshark.org/DisplayFilters](https://wiki.wireshark.org/DisplayFilters)
- (Optional) TCP/IP/TLS reference: [https://www.rfc-editor.org/rfc/rfc793](https://www.rfc-editor.org/rfc/rfc793), [https://hpbn.co/transport-layer-security-tls/](https://hpbn.co/transport-layer-security-tls/)

---

## 🎯 Learning Objectives

By the end of this lab, you will be able to:

1. Install and configure `tshark` on Ubuntu, including safe non-root capture setup
2. Capture and filter live network traffic using capture and display filters
3. Extract structured fields and generate protocol/flow statistics from captures
4. Recognize TCP vs UDP traffic patterns across simultaneous activities
5. Perform a basic security analysis: detect scan-like patterns and inspect TLS metadata

This lab builds on your Ubuntu VM from Lab02B and your command-line skills from Labs 03–05.

---

## 📋 Pre-Lab Requirements

### Required Software
- Ubuntu VM from previous labs
- `tshark` (Wireshark CLI)
- `curl`, `iputils-ping`, `dnsutils` (for test traffic)
- Optional: You can install `Wireshark` GUI for a graphical interface to `tshark` (not required for this lab) on Windows.

Install tools:
```bash
sudo apt update
# Non-interactive install to avoid prompts
sudo DEBIAN_FRONTEND=noninteractive apt install -y tshark curl iputils-ping dnsutils
```

### Important Notes
- Capturing on live interfaces may require privileges. Prefer adding your user to the `wireshark` group instead of running as root.
- Only capture on your own VM and network segments where you are permitted to do so. Do not intercept traffic you are not authorized to monitor.
- If group membership changes are applied, you may need to log out/in (or `newgrp`) for them to take effect.
- After installing `tshark`, please type the command `tshark`, and the following output (or similar) might display, DO NOT IGNORE IT and you need to THINK ABOUT WHAT TO DO WITH IT:
```
$tshark
Capturing on 'eth0'
tshark: The capture session could not be initiated on capture device "eth0" (You don't have permission to capture on that device).
Please check to make sure you have sufficient permission$s.

On Debian and Debian derivatives such as Ubuntu, if you have installed Wireshark from a package, try running

    sudo dpkg-reconfigure wireshark-common

selecting "<Yes>" in response to the question

    Should non-superusers be able to capture packets?

adding yourself to the "wireshark" group by running

    sudo usermod -a -G wireshark {your username}

and then logging out and logging back in again.
```

---

## 🚀 Lab Activities

0) Create a workspace and work from there:
```bash
mkdir -p ~/SPR100_Labs/Lab06/work
cd ~/SPR100_Labs/Lab06/work
```
- All capture and CSV files in this lab must be saved in this `work` folder with the exact filenames specified below.

### Part 1: Install and Explore tshark (30 minutes)

References (skim as needed):
- `man tshark`, `man pcap-filter`
- Wireshark Display Filter Reference: [https://www.wireshark.org/docs/dfref/](https://www.wireshark.org/docs/dfref/)

1) Verify installation and view interfaces:
```bash
tshark -v
tshark -D
```
- Record: `tshark` version and the list of available interfaces (note names like `eth0`, `ens33`, `lo`, `any`).
- Think:
  - What is an “interface” here? Which one carries traffic between your VM and the outside network?
  - Which interface is loopback and why do packets appear there?
  - What is the difference between `any` and a specific interface like `eth0`?

2) Enable non-root capture (safer than sudo):
```bash
sudo usermod -aG wireshark "$USER"
newgrp wireshark  # or log out and back in
# Test capturing a few seconds on loopback:
tshark -i lo -a duration:15
```

- Common question: Why have I *NOT* captured any packets?
- Answer: You need to do something during the 15 seconds on your VM to generate some network traffic  
- HINT: For example, you can do something like this:
  ![capture_example](./capture.png)
  Use tmux to separate the terminal into two panes, and run the commands in the two panes:
  - In the right pane, run the command `tshark -i lo -a duration:15`
  - Quickly switch to the left pane, and run the command `ping google.com`
  - Think: what did the above commands do?



- Record: Whether packets were captured without `sudo`. If not, document the error and continue using `sudo` for captures.
- Think:
  - What permission or capability is required to capture packets?
  - Why is using the `wireshark` group preferred over running everything with `sudo`?
  - What does `newgrp` do and why might a full log out/in be needed?

1) Capture to file, then read and summarize:
```bash
# Capture 10 seconds on your primary interface (replace eth0 as needed)
tshark -i eth0 -a duration:10 -w lab06_basic.pcapng  # REQUIRED filename
```
- You need to do something during the 10 seconds on your VM to generate some network traffic
- Think about what you can do, and how to do it during the 10 seconds that tshark capturing packets.  

```bash
# Read with summary stats
tshark -r lab06_basic.pcapng -q -z io,stat,1
```
- Record: Number of packets captured and any visible protocol mix in `io,stat`.
- Think:
  - What are source and destination IP addresses? How do they relate to your VM and the remote endpoints?
  - What information does a transport header (TCP/UDP) add beyond IP?
  - How would you tell if a packet is TCP or UDP just from header fields?

4) Capture vs Display filters:
```bash
# Capture filter (BPF) — only DNS on port 53 (applies at capture time)
tshark -i any -f "udp port 53" -a duration:8 -w lab06_dns_only.pcapng  # REQUIRED filename

# Display filter — show only HTTP from an existing file
tshark -r lab06_basic.pcapng -Y "http"
```
- Explain the difference: capture filter reduces what is saved; display filter narrows what is shown after capture.
- Think:
  - When would you use a capture filter to reduce noise on a busy link?
  - When is it better to capture broadly and refine later with display filters?
  - What happens if your capture filter is too restrictive?

5) Extract structured fields (CSV-friendly):
```bash
tshark -r lab06_basic.pcapng \
  -T fields -E header=y -E separator=, \
  -e frame.number -e frame.time_relative -e _ws.col.Protocol \
  -e ip.src -e ip.dst -e tcp.srcport -e tcp.dstport -e udp.srcport -e udp.dstport \
  > lab06_basic_fields.csv  # REQUIRED filename
```
- Open the CSV and note how TCP vs UDP are represented via their port fields.
- Think:
  - Which rows have TCP ports vs UDP ports populated? Why do the other port columns appear blank?
  - How does `frame.time_relative` help sequence events?
  - If you wanted to add the TCP SYN flag to this CSV, which field would you use?

---

### Part 2: Recognize TCP vs UDP Across Concurrent Activities (35 minutes)

Goal: Generate several kinds of traffic at the same time and use `tshark` to identify and distinguish them.

Setup (run these in separate terminals or one after another during a timed capture):
```bash
# Terminal A (ICMP):
ping -c 6 1.1.1.1

# Terminal B (DNS):
dig +short senecapolytechnic.ca

# Terminal C (HTTP):
curl -s -o /dev/null -w "%{http_code}\n" http://example.com

# Optional extra DNS:
dig A www.google.com
```
- Think (before capturing):
  - How to run different commands in different terminals while in the same Ubuntu VM?
  - Which of these activities will generate ICMP? Which will generate UDP? Which will generate TCP?
  - For DNS, which port(s) are typically used and on which protocol? What about HTTP?
  - What do you expect the IP destination addresses to be for each activity?

1) Capture during activities, save to file:
```bash
# Replace eth0 with your active interface or use -i any
tshark -i eth0 -a duration:20 -w lab06_multi.pcapng  # REQUIRED filename
```

1) Identify protocols via display filters:
```bash
# ICMP (ping)
tshark -r lab06_multi.pcapng -Y "icmp" -T fields -e frame.number -e ip.src -e ip.dst | head

# DNS (UDP/53 typically)
tshark -r lab06_multi.pcapng -Y "dns" -T fields -e frame.number -e ip.src -e ip.dst -e dns.qry.name | head

# HTTP (may be rare if redirected to HTTPS)
tshark -r lab06_multi.pcapng -Y "http" -T fields -e frame.number -e ip.src -e ip.dst -e http.request.method -e http.host | head
```
- Record: Which activities produced UDP vs TCP, and which produced ICMP.
- Think:
  - For your DNS queries, what were the query names and the responding IPs?
  - Did `curl` to `http://example.com` use TCP? Did it redirect to HTTPS? How could you tell?
  - How would you identify client vs server roles by looking at ports and IPs?

3) Summarize TCP vs UDP counts and conversations:
```bash
# Overall protocol counts (per second bins)
tshark -r lab06_multi.pcapng -q -z io,stat,1,"COUNT(tcp) TCP","COUNT(udp) UDP","COUNT(icmp) ICMP","COUNT(dns) DNS"

# TCP/UDP conversations (endpoints and byte counts)
tshark -r lab06_multi.pcapng -q -z conv,tcp -z conv,udp
```
- Record: Total TCP vs UDP packet counts; note how DNS (UDP) and HTTP (TCP) appear.
- Think:
  - Which conversations (IP:port pairs) carried the most bytes?
  - How would you differentiate long-lived TCP connections from short request/response traffic?
  - What network-layer and transport-layer fields would you cite to support your analysis?

4) Export a tidy dataset for analysis:
```bash
tshark -r lab06_multi.pcapng \
  -T fields -E header=y -E separator=, \
  -e frame.time_relative -e _ws.col.Protocol -e ip.src -e ip.dst \
  -e tcp.flags -e tcp.len -e udp.length -e dns.qry.name \
  > lab06_part2.csv  # REQUIRED filename
```
- Open `lab06_part2.csv` and identify at least 3 rows for ICMP, 3 for DNS, and 3 for HTTP (if present). If HTTP is missing (due to HTTPS redirect), document that and proceed.
- Think:
  - Which field(s) would you use to filter rows to just TCP SYNs? Just DNS queries?
  - How can you tell payload presence from `tcp.len` or `udp.length`?
  - What distinguishes ICMP messages from TCP/UDP in the exported fields?

Reflection prompts for Part 2:
- How did you confirm whether traffic was TCP or UDP?
- Which fields or stats were most helpful to distinguish concurrent activities?
- What pitfalls did you encounter (e.g., HTTP redirect to HTTPS)?

---

### Part 3: Security-Focused Analysis with tshark (25 minutes)

You will perform two short analyses: detect scan-like patterns and inspect TLS metadata. Do this only on your own VM and loopback or your permitted lab network.

1) Detect SYN scan–like behavior on loopback (safe, local):
```bash
# In one terminal, generate connection attempts to your own localhost:
for p in 22 80 443 8000 8080 53; do (echo > /dev/tcp/127.0.0.1/$p) >/dev/null 2>&1 || true; done

# In another terminal, capture loopback and look for SYNs without ACK:
tshark -i lo -a duration:10 -w lab06_security_lo.pcapng  # REQUIRED filename

# Analyze SYNs (SYN=1, ACK=0)
tshark -r lab06_security_lo.pcapng -Y "tcp.flags.syn==1 && tcp.flags.ack==0" \
  -T fields -e frame.time_relative -e ip.src -e ip.dst -e tcp.dstport | sort -n | head -20
```
- Record: Destination ports targeted and why this pattern resembles a basic port-scan footprint.
- Think:
  - What is the normal TCP three-way handshake? Which flags appear in each step?
  - Why do SYNs without corresponding ACKs suggest scanning?
  - Which ports on localhost responded differently? Why might that be?

Optional (if you have permission to run `nmap` on your own VM against `127.0.0.1`):
```bash
sudo apt install -y nmap
# Use sudo for SYN scan (requires privileges), or fall back to -sT without sudo
sudo nmap -sS 127.0.0.1
# or (non-root alternative):
nmap -sT 127.0.0.1
# Re-capture on lo and re-run the SYN filter to compare volume/pattern
```
- If you cannot or prefer not to run `nmap`, the simple loop above is sufficient to demonstrate the idea.

2) Inspect TLS handshake metadata (privacy and security posture):
```bash
# Generate HTTPS traffic
curl -s https://example.com >/dev/null

# Capture briefly (active interface or any)
tshark -i any -a duration:8 -w lab06_tls.pcapng  # REQUIRED filename

# Extract Server Name Indication (SNI) and TLS version from the capture
tshark -r lab06_tls.pcapng -Y "tls.handshake.extensions_server_name" \
  -T fields -e frame.time_relative -e ip.dst -e tls.handshake.extensions_server_name -e tls.record.version | head
```
- Record: Observed SNI hostnames and TLS versions. Discuss how SNI exposure can impact privacy and why TLS versions/ciphers matter for security.
- Think:
  - What does SNI reveal about the destination you are visiting?
  - Why can TLS metadata be visible even when payloads are encrypted?
  - Which TLS versions are considered modern vs deprecated? Why does it matter?

Reflection prompts for Part 3:
- What `tshark` patterns suggest scan-like behavior?
- What sensitive information can be inferred from TLS metadata, even if payloads are encrypted?
- Ethical reminder: Where is it legal and appropriate to capture traffic?

---

## 🧠 Mindset Reminder

For every command you run, write down:
- What the command does (in your own words)
- Which network layer(s) it relates to (link, network/IP, transport/TCP-UDP, or application)
- What you learned from its output and how it connects to concepts like IP addressing, ports, headers, and flags

---

## 🧪 Deliverables

Submit a `README.md` in `Labs/Lab06/` that includes:
- Commands you ran (trim outputs to the most relevant lines)
- CSV snippets showing:
  - Part 1: `tshark -D`, `io,stat` output, and a few extracted fields
  - Part 2: Filters for ICMP/DNS/HTTP and protocol counts vs time; a short annotated excerpt from `lab06_part2.csv`
  - Part 3: SYN pattern evidence and TLS SNI/version extraction
- Explanations in your own words of:
  - Capture vs display filters and when to use each
  - How you determined TCP vs UDP for the concurrent activities
  - Security/privacy implications observed in Part 3

Use the provided submission template and save your completed report correctly:
- Start from `Labs/Lab06/lab06_submission_template.md`
- Save your completed report as `Labs/Lab06/README.md` (do not include the word "template" in the filename)

### Files to Submit (save all in `~/SPR100_Labs/Lab06/work/` with exact names)
- lab06_basic.pcapng
- lab06_dns_only.pcapng
- lab06_basic_fields.csv
- lab06_multi.pcapng
- lab06_part2.csv
- lab06_security_lo.pcapng
- lab06_tls.pcapng

Notes:
- Keep files reasonably small (short durations as shown) so your repository stays under size limits.
- Do not rename files; we will auto-check for these exact filenames.

### Reflection Prompts
1. What is the difference between capture filters (`-f`) and display filters (`-Y`)? Provide one scenario for each.  
2. How can you reliably identify TCP vs UDP traffic using `tshark` output or fields?  
3. What can TLS metadata (e.g., SNI, version) reveal even when payloads are encrypted?  
4. What ethical and legal boundaries must you respect when capturing network traffic?

---

## 📤 Submission Instructions

Follow the same submission flow as previous labs and the Labs root guidelines:
1. Place your lab `README.md` and any artifacts in `Labs/Lab06/`
2. Commit and push before the deadline

Suggested commit message:  
"Complete Lab06 - Network Traffic Analysis with tshark"

For general submission rules and rubric, see the root `Labs/readme.md`.

---


