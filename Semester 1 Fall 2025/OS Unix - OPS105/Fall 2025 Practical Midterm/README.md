\# OPS105 Fall 2025 Practical Midterm



\## What’s New



\- \*\*Week 8\*\*

\- \*\*Oct 26\*\* — Initial announcement



---



\## Download VMs



\- The link to download the VMs required for this test was sent to your \*\*MySeneca email\*\*.

\- \*\*MySeneca authentication\*\* is required to complete the download.

\- When prompted for a password during download, use: `ubuntu`.



\### VM Login Credentials



For \*\*both virtual machines (VMs)\*\*:



\- `root` account password: `ubuntu`

\- `ubuntu` account password: `ubuntu`



---



\## Practical Test



\### User Setup (Both VMs: GW + ND)



1\. Become `root` and create an \*\*unprivileged (non-root) user\*\*:

&nbsp;  - Username must match your \*\*MySeneca username\*\*.

2\. Ensure the MySeneca-named user exists on \*\*both VMs\*\*.

3\. Log in as the MySeneca-named user on \*\*both VMs\*\* and run:

&nbsp;  - `whoami`

&nbsp;  - `id`

&nbsp;  - `pwd`

&nbsp;  - `date`

4\. Log out of the MySeneca-named user and log back in as `root`.



---



\### Package Management



\- Bring packages \*\*up to date\*\* on both VMs.



\#### Node (ND)



Install:

\- `dnsutils`

\- `tldr`

\- `tree`



\#### Gateway (GW)



Install:

\- `dnsutils`

\- `nftables`

\- `tldr`

\- `tree`



> You may install additional packages on both VMs as long as the \*\*total disk usage does not exceed 10GB\*\*.



---



\## Network Configuration



\### Gateway (GW)



\- Enable \*\*two network interfaces\*\*:

&nbsp; - One set to \*\*NAT\*\*

&nbsp; - One set to \*\*Internal Network\*\*



\### Node (ND)



\- Enable \*\*one network interface\*\*:

&nbsp; - Set to \*\*Internal Network\*\*



\### Internal Network Setup



\- Configure a \*\*CIDR /30\*\* network using both VMs.

\- Hostnames:

&nbsp; - Gateway VM: `gw`

&nbsp; - Node VM: `nd`

\- Network address format:

&nbsp; - `192.168.Y.32/30`



\#### Calculating `Y`



\- `Y` is derived from the \*\*2nd and 5th digits\*\* of your Student ID.

&nbsp; - Example: Student ID `123-456-789`

&nbsp;   - Digits: `2` and `5`

&nbsp;   - `Y = 25`

\- \*\*Leading zeros are removed\*\*:

&nbsp; - `03` → `3`

&nbsp; - `00` → `0`

&nbsp; - `10` → `10`



\### Routing Requirements



\- Gateway (`gw`) is \*\*reboot-persistent\*\*.

\- Node (`nd`) is \*\*transient\*\*.

\- Gateway acts as a \*\*router\*\* for the node.

\- Node has Internet connectivity \*\*only when the gateway is running\*\*.

\- Verify the MySeneca-named user can:

&nbsp; - Query IP addresses of `ubuntu.com`

&nbsp; - SSH to `matrix.senecapolytechnic.ca`



\#### SSH Access Rules



\- \*\*On campus\*\*: SSH to `matrix.senecapolytechnic.ca` \*\*without VPN\*\*

\- \*\*Off campus\*\*: Student VPN \*\*must be running and connected\*\* on the host OS (Windows/macOS/Linux)



---



\## Practical Test Completion Checklist



\- \[ ] All activity occurred on \*\*professor-provided VMs\*\* downloaded during class time on campus.

\- \[ ] All packages were brought \*\*up to date\*\* before submission.

\- \[ ] Node installed packages: `dnsutils`, `tldr`, `tree`.

\- \[ ] Gateway installed packages: `dnsutils`, `tldr`, `tree`, `nftables`.

\- \[ ] Internal network address: `192.168.Y.32/30`.

\- \[ ] Node has Internet access \*\*only when gateway is running\*\*.

\- \[ ] MySeneca-named user logged in on both VMs and ran:

&nbsp; - `whoami`, `id`, `pwd`, `date`

&nbsp; - `ssh` to matrix after internal network setup

\- \[ ] Node is transient and can SSH to matrix \*\*only when gateway is running\*\*.

\- \[ ] Gateway is reboot-persistent and forwards Internet traffic.

\- \[ ] Verified reboot persistence by observing ping stop/start during gateway reboot.

\- \[ ] Understood the \*\*Grading Policy\*\* and \*\*Grading Rubric\*\*.

\- \[ ] Did not tamper with system or user log files.

\- \[ ] Final submission occurred only after all node traffic was routed through gateway.



---



\## Submission



1\. Configure the internal network as specified.

2\. On \*\*Node (ND)\*\*, log in as `root`.

3\. Run:

&nbsp;  ```bash

&nbsp;  submit



