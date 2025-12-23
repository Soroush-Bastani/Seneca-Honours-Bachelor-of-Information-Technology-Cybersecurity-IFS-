\# OPS105 Practice Test



\## What’s New



\- \*\*Oct 26\*\* — Updated broken download link  

\- \*\*Oct 19\*\* — Initial release



---



\## Download VMs



\- Download the VMs (\*\*MySeneca authentication required\*\*).

\- Link password: `ubuntu`



\### VM Login Credentials



For \*\*both virtual machines (VMs)\*\*:



\- `ubuntu` account password: `ubuntu`

\- `root` account password: `ubuntu`



---



\## Practice



\### Package Management



\- Bring packages on \*\*both VMs\*\* up to date.



\#### Install Packages



\*\*On Node:\*\*

\- `curl`

\- `dnsutils`

\- `iputils-ping`

\- `tree`

\- `vim`

\- `wget`

\- Any other command-line based packages you like



\*\*On Gateway:\*\*

\- `curl`

\- `dnsutils`

\- `iputils-ping`

\- `nftables`

\- `tree`

\- `vim`

\- `wget`

\- Any other command-line based packages you like



> You may install additional packages on each VM as long as the \*\*total disk size does not exceed 10GB\*\* (disk size is restricted to 10GB max).



---



\## Networking Practice



\### Network Interfaces



\- On \*\*both VMs\*\*, add \*\*secondary network interface cards\*\*.

\- Configure the secondary interfaces with \*\*static IPs\*\* for a \*\*CIDR /30\*\* network.



\### Hostnames



\- Gateway VM hostname: `gwp`

\- Node VM hostname: `ndp`



\### Routing Requirements



\- Configure the network so the \*\*node depends on the gateway\*\* for all Internet traffic.

\- Configure the \*\*gateway to act as the router\*\* for the node.



\### Network Address



\- Use network address: `192.168.25.32/30`



Your network setup should support:



\- \*\*Transient network\*\*

&nbsp; - Existing network configuration does \*\*not persist after reboot\*\*

\- \*\*Reboot-persistent network\*\*

&nbsp; - Existing network configuration \*\*persists after reboot\*\*



---



\## User Setup



\- Create an \*\*unprivileged (non-root) user\*\*:

&nbsp; - Username must match your \*\*MySeneca username\*\*

\- Create this user on \*\*both VMs\*\*.

\- Log in as the MySeneca-named user on \*\*both VMs\*\*.



---



\## Connectivity Verification



After the network is set up, ensure:



\- \*\*Student VPN\*\* is running on your host operating system (Windows).

\- Your MySeneca-named user can:

&nbsp; - SSH to `matrix.senecapolytechnic.ca` from \*\*node\*\*

&nbsp; - SSH to `matrix.senecapolytechnic.ca` from \*\*gateway\*\*

\- SSH access to matrix from \*\*node\*\* is possible \*\*only when the gateway is running\*\*.



---



\## Practice Test Completion Checklist



\- Off-campus:

&nbsp; - Student VPN is started and connected \*\*before booting the VMs\*\*

\- Using the MySeneca-named user:

&nbsp; - Logged in at least once on \*\*both VMs\*\*

\- Verified:

&nbsp; - Node has \*\*no Internet access when gateway is switched off\*\*

\- Using SSH:

&nbsp; - Can log in to matrix from \*\*both node and gateway\*\* when Student VPN is running

\- Downloaded directory \*\*`notes`\*\* from user `mark.fernandes` on matrix  

&nbsp; - (`notes` is a subdirectory of `ops105`)



---



\## Suggested Additional Practice



\- Experiment with different \*\*CIDR /30\*\* networks (multiples of 4), for example:

&nbsp; - `192.168.25.4/30`

&nbsp; - `192.168.25.40/30`

&nbsp; - `192.168.25.56/30`

&nbsp; - `192.168.25.64/30`

\- Practice mixing \*\*transient and persistent\*\* configurations:

&nbsp; - Node persistent, gateway transient

&nbsp; - Gateway persistent, node transient



---



\## OPS105 Home



\- \*\*Last Updated:\*\* 2025-Oct-27 (Mon) 14:11



