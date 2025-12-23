````md
# Introduction to Networking - III  
## Reboot Persistent Gateway-Node Network

## Objective
The objective of this lab is to introduce the steps and the concepts involved in setting up a permanent (reboot-persistent) network between two hosts.

This network is available as soon as both hosts are setup to do their roles (either as node or as gateway) and running but unlike *Introduction to Networking - II (Transient Gateway-Node Network)* this setup persists despite reboot on either one or both hosts.

---

## Two Host (CIDR/30) Gateway-Node Network

We will create a 2 host transient network with the following setup:

| Description | Value |
|---|---|
| Network Address (Fixed) | `192.168.99.0/30` |
| Host 1 (Gateway 2 NIC) | `192.168.99.1/30` |
| Host 2 (Node 1 NIC) | `192.168.99.2/30` |
| Broadcast Address (Fixed) | `192.168.99.3/30` |

This network is allowed to have two hosts only (see: CIDR/30 or glue network), so we configure one of them as a gateway and the other host as a node in order to understand the role and purpose of the node and the gateway in a typical network. In addition, we learn how to configure this network (both the gateway and the node) so the network, as configured, persists despite reboots on either the gateway or the node.

Unless the node is configured to look for a default gateway by adding a route to the gateway IP in the node's routing table, the node will not have Internet connectivity. When using:

- **Debian:** the files needed to setup node are:
  - `/etc/network/interfaces` (static IP on node)
  - `/etc/resolv.conf` (to set domain name server, DNS, lookup)

- **Ubuntu:** the files needed to setup node are:
  - `/etc/netplan/99_config.yaml` (static IP on node)
  - `/etc/systemd/resolved.conf` (to set domain name server, DNS, lookup)

Unless the gateway is configured to forward packets, it wont act as a gateway. This means the node which depends on the gateway to route node's network packets wont connect to the Internet even if the node was configured correctly. The gateway, however, will connect to the Internet whether configured correctly or not because the gateway gets a dynamic IP from VirtualBox (and so the gateway is able to route its packets) on the other NIC (network interface card). The files needed to setup the gateway correctly are:

- **Debian:**
  - `/etc/network/interfaces` (to set static IP for gateway)
  - `/etc/sysctl.conf` (to setup IP packet forwarding between the two network interface cards on the gateway)
  - `/etc/nftables.ruleset` or `/etc/iptables.ruleset` (to enable MASQUERADE on gateway for node packets)
  - `/etc/network/if-pre-up.d/nftables` (script to automatically load NFTABLES ruleset at bootup)

- **Ubuntu:**
  - `/etc/netplan/99_config.yaml` (to set static IP for gateway)
  - `/etc/sysctl.conf` (to setup IP packet forwarding between the two network interface cards on the gateway)
  - `/etc/nftables.ruleset` or `/etc/iptables.ruleset` (to enable MASQUERADE on gateway for node packets)
  - `/etc/networkd-dispatcher/routable.d/50-ifup.hooks` (script to automatically load NFTABLES ruleset at bootup)

Since this network will be permanent, it persists beyond reboots on both the node and the gateway, however, the node wont connect to the Internet should the gateway go offline and will only connect to the Internet when the gateway comes back online.

The gateway is configured to packet forward (which means to pass network packets from one network segment to another network segment) and masquerade (see: How does IP Masquerade Work?) while the node is configured to add a default gateway. When both are configured, the gateway acts as the node's gateway of last resort.

This lab below shows how to setup a (boot-persistent or permanent) network between the node and the gateway. This means the roles of node (configured to add gateway host IP as node's default gateway and domain name server resolver) and gateway (forward packets between the internal network containing the node and the external network containing the Internet) are stored in configuration files that are read whenever each of them reboots thereby ensuring the network, as configured, becomes boot-persistent.

---

## Step 1: Ping gateway from node

### Node

Check existing setup and verify Internet connectivity:

```bash
ip --brief address
ip route
getent ahosts debian.org
````

Stop NetworkManager and disable DHCP (`enp0s3`) interface:

```bash
# in case of minimal desktop (no GUI) you can skip the next two steps
systemctl status NetworkManager
systemctl stop NetworkManager
systemctl disable NetworkManager
systemctl status NetworkManager
```

On Ubuntu use systemd-networkd:

```bash
systemctl status systemd-networkd
systemctl start systemd-networkd
systemctl enable systemd-networkd
systemctl status systemd-networkd
```

Disable DHCP on `enp0s3`:

```bash
ip link set dev enp0s3 down
dhclient -r enp0s3
ip --brief address
ip -4 address show up
```

For Debian only remove existing `/etc/resolv.conf`:

```bash
mv /etc/resolv.conf /etc/resolv.conf.original
```

Set `enp0s8` on node to IP `192.168.99.2/30`:

* See *Introduction to Networking - I* on how to set a reboot-persistent static IP.
* Ensure gateway IP `192.168.99.1/30` is set on the node so the default gateway is automatically setup on the node when the node boots up.

Setup DNS resolution on node for Internet:

**On Debian create or edit `/etc/resolv.conf`:**

```bash
cat /etc/resolv.conf
```

Expected content:

```text
nameserver 1.1.1.1
nameserver 8.8.8.8
# nameservers for Seneca VPN (FOR REFERENCE ONLY. DO NOT ADD)
# nameserver 10.101.100.21
# nameserver 10.101.100.22
```

**On Ubuntu edit `/etc/systemd/resolved.conf` to give the following output:**

```bash
grep "^FallbackDNS=" /etc/systemd/resolved.conf
```

Expected output:

```text
FallbackDNS=1.1.1.1 8.8.8.8 9.9.9.9
```

Setup DNS resolution on node for matrix by editing `/etc/hosts`:

Include this line in `/etc/hosts`:

```text
10.102.108.5   matrix.senecapolytechnic.ca matrix.senecacollege.ca matrix
```

Reboot node and verify:

* `enp0s8` has IP address assigned but no Internet.
* Verify node is not connected to the Internet.
* Verify node cannot reach gateway (`192.168.99.1/30`) on the same subnet after gateway has been setup and configured correctly.
* After gateway was configured to be on the same subnet (`192.168.99.0/30`) as node will node (`192.168.99.2/30`) be able to ping gateway (`192.168.99.1/30`).

### Gateway

Check existing setup and verify Internet connectivity.

Use the commands shown in the Node example above to check existing Gateway IP address and route setup. Verify Internet connectivity works in the Gateway before you proceed further.

Set `enp0s8` on gateway to IP `192.168.99.1/30` using:

* `/etc/netplan/99-config.yaml` on Ubuntu
  or
* `/etc/network/interfaces` on Debian

See *Introduction to Networking - I* on how to set a reboot-persistent static IP.

Reboot and verify:

* `enp0s8` has assigned IP address
* Gateway continues to have Internet connectivity after reboot
* Node (`192.168.99.2/30`) can ping gateway (`192.168.99.1/30`) but node cannot go outside the `192.168.99.0/30` subnet

  * This is expected at this step.

---

## Step 2: Enable packet forwarding on gateway

### Gateway

```bash
cp /etc/sysctl.conf /etc/sysctl.conf.original

# edit /etc/sysctl.conf to remove the '#' from the start of:
# net.ipv4.ip_forward=1
# so output from this command is as shown below
grep "^net.ipv4.ip_forward" /etc/sysctl.conf
```

Expected output:

```text
net.ipv4.ip_forward=1
```

---

## Step 3: Enable packet masquerading on gateway

### Gateway

#### Using nftables (nft) only

```bash
nft flush ruleset
nft add table ip nat
nft add chain ip nat POSTROUTING '{ type nat hook postrouting priority 100; policy accept; }'
nft add rule ip nat POSTROUTING oifname "enp0s3" counter masquerade
nft list ruleset > /etc/nftables.ruleset
cat /etc/nftables.ruleset
```

Example output (example only):

```text
table ip nat {
     chain POSTROUTING {
         type nat hook postrouting priority srcnat; policy accept;
         oifname "enp0s3" counter packets 15 bytes 900 masquerade
     }
}
```

Skip the step below if you have output similar to the above and go to loading of `/etc/nftables.ruleset` for Ubuntu or Debian.

#### Alternatively, if iptables was used to generate `/etc/nftables.ruleset`

```bash
iptables -t nat -A POSTROUTING -o enp0s3 -j MASQUERADE
iptables-save > /etc/iptables.ruleset
cat /etc/iptables.ruleset
```

Example output (timestamp will differ):

```text
# generated by iptables-save v1.8.7 on wed oct 13 11:18:46 2021
*nat
:prerouting accept [0:0]
:input accept [0:0]
:output accept [0:0]
:postrouting accept [0:0]
-a postrouting -o enp0s3 -j masquerade
commit
# completed on wed oct 13 11:18:46 2021
```

To see the equivalent nftables ruleset:

```bash
iptables-restore-translate -f /etc/iptables.ruleset > /etc/nftables.ruleset
cat /etc/nftables.ruleset
```

Example output (timestamp will differ):

```text
# Translated by iptables-restore-translate v1.8.7 on Wed Oct 13 11:21:01 2021
add table ip nat
add chain ip nat PREROUTING { type nat hook prerouting priority -100; policy accept; }
add chain ip nat INPUT { type nat hook input priority 100; policy accept; }
add chain ip nat OUTPUT { type nat hook output priority -100; policy accept; }
add chain ip nat POSTROUTING { type nat hook postrouting priority 100; policy accept; }
add rule ip nat POSTROUTING oifname "enp0s3" counter masquerade
# Completed on Wed oct 21 11:21:01 2021
```

---

## Automatically load nftables rules at startup

### Ubuntu

```bash
# create /etc/networkd-dispatcher/routable.d if it does not exist
touch /etc/networkd-dispatcher/routable.d/50-ifup.hooks
chmod a+x /etc/networkd-dispatcher/routable.d/50-ifup.hooks
cat /etc/networkd-dispatcher/routable.d/50-ifup.hooks
```

**NOTE:** Edit the contents of `/etc/networkd-dispatcher/routable.d/50-ifup.hooks` to be exactly:

```bash
#!/bin/sh
#

/usr/sbin/nft --file /etc/nftables.ruleset
exit 0

# Entire contents added by MF on Thu Oct 06 2022
```

### Debian

```bash
touch /etc/network/if-pre-up.d/nftables
chmod a+x /etc/network/if-pre-up.d/nftables
cat /etc/network/if-pre-up.d/nftables
```

**NOTE:** Edit the contents of `/etc/network/if-pre-up.d/nftables` to be exactly:

```bash
#!/bin/bash
#

/usr/sbin/nft --file /etc/nftables.ruleset

# Entire contents added by MF on Thu Feb 17 2022
```

---

## Step 4: On Node: verify Internet depends on gateway being up

Verify domain name resolution works on Node:

```bash
getent ahosts ubuntu.com
getent ahosts debian.org
```

---

## Step 5: On Node: verify matrix connectivity (Student VPN required)

Verify you can connect to matrix (replace `use` with your MySeneca username):

```bash
ssh use@matrix.senecapolytechnic.ca
```

---

## Reference Screen Capture

Proof of a working reboot-persistent 2-Host CIDR/30 `192.168.99.0` subnet should be done as follows:

1. Power off both gateway and node VMs.
2. Power on the node (Ubuntu GUI) VM.
3. On node login and run:

   * `ping 1.1.1.1`
4. Observe output from ping shows:

   * `"Destination Host Unreachable"`
   * This happens because gateway (Ubuntu Minimal Server) VM is not up yet.
5. Power on gateway VM.
6. When gateway VM has powered on, do not login. Keep observing ping output on node VM.
7. Notice as soon as gateway VM booted up:

   * ping error messages stop
   * ping responses from `1.1.1.1` begin
8. Check DNS resolution:

   * Run `getent ahosts ubuntu.com` and check for output containing IPv4 and IPv6 addresses.

Proof of a working GW (gateway) and ND (node) setup.

---

## Practice Questions

**NOTE:** Answers to the configuration questions are to be based on making changes to files in `/etc/` irrespective of whether you are working on the node or on the gateway but it is important know which file to edit on which host to complete that question.

1. What is a name server? When is a name server needed on a network? Using absolute pathnames, state which file has the default name server and what are some of the data options stored in the file that contains the default name server.

2. Compare the contents of the file containing the name server on the node and on the gateway. Are the two files different? Why? If they are different, what are the differences between the file containing the name server on the node and the gateway.

3. On Ubuntu: what was the contents of `/etc/netplan/99_config.yaml` on the node? How was that content different from `/etc/netplan/99_config.yaml` on the gateway?

4. On Debian: what was the contents of `/etc/network/interfaces` on the node? How was that content different from `/etc/network/interfaces` on the gateway?

5. On Ubuntu: what was the contents of `/etc/netplan/99_config.yaml` on the gateway? How was that content different from `/etc/netplan/99_config.yaml` on the node?

6. On Debian: what was the contents of `/etc/network/interfaces` on the gateway? How was that content different from `/etc/network/interfaces` on the node?

7. How did you enable packet forwarding to happen automatically on the gateway? What file(s) did you edit and what changes did you make in that file? How is the enabling of packet forwarding different when done from the command line and when done from the file?

8. How will you turn off packet forwarding on the gateway for its current live session only (changes to packet forwarding made during this session should not persist a reboot). Give the full command line on both the gateway and the node to verify changes made to packet forwarding in this session were turned off.

9. What happens if you turn on packet forwarding but have not enabled IP masquerading? Will the node have Internet connectivity? If you answered yes then why would IP masquerading be needed? If you answered no then what does IP masquerading do?

10. What does the command `iptables` do? How can you persist the state of iptables so it is available on the next reboot? Show the entire command line to do that?

11. What does `<` and `>` written on a command line do? Give examples of using `<` and `>` in this lab. HINT: You could edit `/etc/iptables.ruleset` in an editor and read the results back in.

12. Overall, how is setting up a network from the command line (transient) different from setting up a network so it is reboot persistent (permanent). When would you use each method to setup a network?

---

## OPS105 Home

* **Last Updated:** 2025-Sep-02 (Tue) 21:36

```
```
