````md
# Introduction to Networking - II  
## Transient (In-Memory) Gateway-Node Network

## Objective
Objective is to introduce steps and concepts involved in setting up a transient (temporary, in-memory) network between two hosts from the command line.

This network is available as long as both hosts are setup to do their roles (either as node or as gateway) and running, however, when either one or both are rebooted this transient network between the two hosts wont be available.

---

## Two Host (CIDR/30) Gateway-Node Network

We will create a 2 host transient (in-memory) network with the following setup:

| Description | Value |
|---|---|
| Network Address (Fixed) | `192.168.99.0/30` |
| Host 1 (Gateway 2 NIC) | `192.168.99.1/30` |
| Host 2 (Node 1 NIC) | `192.168.99.2/30` |
| Broadcast Address (Fixed) | `192.168.99.3/30` |

### Notes

- This network is allowed to have two hosts only (see: CIDR/30 or glue network), so we configure one of them as a gateway and the other host as a node in order to understand the role and purpose of the node and the gateway in a typical network. In addition, we learn how to configure each host (gateway and node) on this transient (in memory and not boot-persistent) network from the command line.
- Unless the node is configured to look for a default gateway by adding a route to the gateway IP in the node's routing table, the node will not have Internet connectivity.
- Unless the gateway is configured to forward packets, it wont act as a gateway. This means the node which depends on the gateway to route node's network packets wont connect to the Internet even if the node was configured correctly. The gateway, however, will connect to the Internet whether configured correctly or not because the gateway gets a dynamic IP from VirtualBox (and so the gateway is able to route its packets) on the other NIC (network interface card).
- Since this network is transient, it only exists in memory of both the hosts when they are up and running, and configured to do their respective roles correctly. Upon rebooting any one of them, the network as described above no longer exists.
- The gateway is configured to packet forward (which means to pass network packets from one network segment to another network segment) and masquerade (see: How does IP Masquerade Work?) while the node is configured to add a default gateway. When both are configured, the gateway acts as the node's gateway of last resort.

This lab below shows how to, from the command line, add a (transient) route and how to forward packets coming in from one interface (representing one network segment) to another interface (representing the other network segment).

Both features: default gateway setup on the node and packet forwarding on the gateway are only available until either machine reboots. So, if any one of them reboots the network will no longer be active as described in this lab.

---

## Step 1: Node can ping Gateway

Do this step to ensure both Node and Gateway are on the same subnet.

### Node

Check existing setup and verify whether you have Internet connectivity or not:

```bash
ip --brief address
ip route
getent ahosts ubuntu.com
````

Stop NetworkManager and disable the DHCP (`enp0s3`) interface:

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
ip -4 address show up
```

Set `enp0s8` to IP `192.168.99.2/30`:

```bash
# (optional step) if interface has an existing IP address, delete it
ip address delete 192.168.99.19/24 dev enp0s8

# using CIDR notation, assign IP and broadcast to the interface
ip address add 192.168.99.2/30 broadcast 192.168.99.3 dev enp0s8

# verify the above address was added
ip --brief address

# node can ping the gateway (after the gateway as been set up)
ping 192.168.99.1
```

Verify:

* `enp0s8` has IP address assigned but no Internet.
* Node is not connected to the Internet.
* Node cannot reach Gateway (`192.168.99.1/30`) on the same subnet (since Gateway has not been setup yet).

---

### Gateway

Check existing setup and verify Internet connectivity.

Use the commands shown in the Node example above to check existing Gateway IP address and route setup. Verify Internet connectivity works in the Gateway before you proceed further.

Set secondary interface to have IP `192.168.99.1/30`:

```bash
# become root
sudo -i

# bring the link up
ip link set up dev enp0s8

# (optional step) if interface has an existing IP address, delete it
ip address delete 192.168.99.19/24 dev enp0s8

# using CIDR notation, assign IP and broadcast to the interface
ip address add 192.168.99.1/30 broadcast 192.168.99.3 dev enp0s8

# check ip address
ip --brief address
```

---

### Node and Gateway (Verification)

For the given network address (`192.168.99.0/30`), verify `enp0s8` assigned IP address correctly on Node and on Gateway.

Verify Gateway continues to have Internet connectivity after setting Gateway IP.

In addition, verify Node (`192.168.99.2/30`) can ping gateway (`192.168.99.1/30`) but Node cannot go outside the `192.168.99.0/30` subnet (Node should continue to have no Internet connectivity at this step).

From Node run:

```bash
ping 192.168.99.1
```

---

## Step 2: Enable Packet Forward and Masquerade on Gateway

Do this step to ensure packets originating from, and destined for, Node can hop across the two gateway network segments (`enp0s3` on Gateway is connected to the Internet whereas `enp0s8` on Gateway is connected to Node).

### Gateway

```bash
# setup packet forwarding
cat /proc/sys/net/ipv4/ip_forward
echo 1 > /proc/sys/net/ipv4/ip_forward
cat /proc/sys/net/ipv4/ip_forward

# setup MASQUERADING on enp0s3
# legacy iptables command to setup POSTROUTING
#   iptables -t nat -A POSTROUTING -o enp0s3 -j MASQUERADE

# nft equivalent (all commands below this line are necessary)
nft list tables
nft list chains

nft add table ip nat
nft list table nat
nft list chains

nft add chain ip nat POSTROUTING '{ type nat hook postrouting priority 100; policy accept; }'
nft list table nat

nft add rule ip nat POSTROUTING oifname "enp0s3" counter masquerade
nft list table nat

nft list ruleset
```

---

## Step 3: Add route rule on Node to use Gateway as default

Do this step to ensure Node always knows where to send its packets.

### Node

```bash
ip route add default via 192.168.99.1 dev enp0s8
```

---

## Step 4: Enable name resolution lookup on Node

Do this step to ensure Node knows which nameservers to contact when it needs to translate domain names (such as `debian.org`) to their IP values.

### Node

Create (or edit) the domain name server lookup file and put these lines into `/etc/systemd/resolved.conf`:

```text
# Update /etc/systemd/resolved.conf and included this line
FallbackDNS=1.1.1.1 8.8.8.8 9.9.9.9
```

Edit `/etc/hosts` to include this line:

```text
10.102.108.5   matrix.senecapolytechnic.ca matrix.senecacollege.ca matrix
```

Restart resolved:

```bash
systemctl restart systemd-resolved
```

---

## Step 5: Verify Internet connectivity available on Node

```bash
# Verify you have domain name resolution working on Node
getent ahosts debian.org
getent ahosts ubuntu.com

# Verify you can connect to matrix (replace user with your MySeneca username)
ssh user@matrix.senecapolytechnic.ca
```

---

## Practice Questions

**NOTE:** Answers to the configuration questions are to be based on what you would enter on the command line only, i.e. without making any changes to any files in `/etc` irrespective of whether you are working on the node or on the gateway.

1. What does the CIDR acronym mean? What problem does CIDR solve and how does CIDR solve that problem?

2. What is the smallest multi-host network using the CIDR notation? How many additional hosts does this smallest multi-host CIDR network have in comparison to CIDR's glue network?

3. What does the term network routing mean? In the lab above which of the two hosts was configured to route its packets to the other? Why?

4. Using a one-line `ip` command, display the routing table. In the output of the routing table, how would you identify the gateway IP?

5. Examine the sample output shown below of `ip route`:

   ```text
   192.168.0.0/24 dev wlan0 proto kernel scope link src 192.168.0.221
   ```

   In the output shown, is there a gateway IP assigned? If so, what is its value? If no gateway IP was assigned, write an `ip route` command to assign a gateway IP (HINT: You may use any IP you want for the gateway provided its value is usable on the same subnet as the sample output).

6. Minimal Ubuntu VM has two network interface cards: `enp0s3` and `enp0s8`. On VirtualBox `enp0s3` uses NAT while `enp0s8` uses Internal Network. `enp0s3` gets its IP address configured automatically from host operating system through DHCP. `enp0s8` has to be enabled and set its IP address to `192.168.99.1/30`. Write the command lines to enable `enp0s8` and set its IP address to `192.168.99.1/30`. Next write all the command lines needed to set this minimal Ubuntu VM as a gateway on `192.168.99.0/30` CIDR/30 network.

7. After you ran the two commands in question #6 above, what two different commands will you use to confirm that host `192.168.99.1/30` has become a gateway? Where would you run those commands (on the gateway or on the node)? Why? What commands will you use on the node to confirm that the gateway is setup correctly and running? What command will you use on the gateway to confirm that it is the gateway and forwarding packets?

8. You are asked to configure a small ad hoc intranet `192.168.3.0/28` having one gateway with four nodes, briefly describe the steps you would take to create that network. What values will you use for the four nodes and the gateway and write the commands you would execute on each node and gateway.

9. What does term packet forwarding mean? How will you confirm packet forwarding has been implemented? Why was it necessary to be done on the gateway and not the node? What would happen if packet forwarding was implemented on the node as well as the gateway - would the node still be able to connect to the Internet? Now what happens if packet forwarding was only done on the node, not the gateway, would the node be able to connect to the Internet?

10. In the iptables command used above, what does `POSTROUTING` and `MASQUERADE` mean? Why was that step necessary to make `192.168.99.1/30` a gateway? What is the `iptables` command generally used for?

---

## OPS105 Home

* **Last Updated:** 2025-Sep-02 (Tue) 21:36

```
```
