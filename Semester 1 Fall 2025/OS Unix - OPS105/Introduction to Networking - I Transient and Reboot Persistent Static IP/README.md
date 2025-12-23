````md
# Introduction to Networking - I  
## Transient and Reboot Persistent Static IP

## Objective
The objective of this lab is to introduce you to the concepts of network addressing, specifically setting up a dynamic and static address. You will learn how to set a transient static IP address from the command line (which will only be available until the machine next reboots). In addition, this lab will also show you HOWTO set a network adapter to a static IP that sticks (persists even after rebooting).

---

## Overview

- Get IP address associated with an interface.
- HOWTO detect the type of IP assigned (dynamic or static) using the `ip` command.
- What type of IP did the VirtualBox VM get? How does this dynamic IP connect the VM to the Internet?
- HOWTO assign a static IP address to an interface:
  - using the `ip` command to assign a temporary or transient static IP
  - to assign a permanent or reboot-persistent static IP:
    - On Ubuntu, edit `/etc/netplan/99_config.yaml`
    - On Debian, edit `/etc/network/interfaces`

---

## What to do

### 1. Display useful networking information

Display useful networking information as follows:

```bash
ip address show dev enp0s3
````

The initial output (before adding the second network interface) from my DS (Debian Stable) machine is:

```text
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 08:00:27:98:e0:c0 brd ff:ff:ff:ff:ff:ff
    inet 10.0.2.15/24 brd 10.0.2.255 scope global dynamic noprefixroute enp0s3
       valid_lft 81690sec preferred_lft 81690sec
    inet6 fe80::a00:27ff:fe98:e0c0/64 scope link noprefixroute
       valid_lft forever preferred_lft forever
```

Notice the word `dynamic` in the output above indicates `enp0s3` received a dynamic IP address.

---

### 2. Add the secondary interface

1. Shut down the virtual machine
2. Add a secondary network adapter (select **Internal Network**)
3. Restart the virtual machine

---

### 3. HOWTO set transient IP

After your virtual machine has booted up you may set the IP address of `enp0s8` as follows (you need to be superuser (administrator) to run the following commands):

```bash
# On Ubuntu, become root using
sudo -i

# On Debian, become root using
su -

# 1. install dhclient
apt install isc-dhcp-client

# 2. stop and disable NetworkManager
systemctl status NetworkManager
systemctl stop NetworkManager
systemctl disable NetworkManager
systemctl status NetworkManager

# On Ubuntu use systemd-networkd instead
systemctl status systemd-networkd
systemctl start systemd-networkd
systemctl enable systemd-networkd
systemctl status systemd-networkd

# 3. DHCP address to enp0s3
ip address show dev enp0s3
dhclient enp0s3
ip address show dev enp0s3

# 4. static address to enp0s8
ip address show dev enp0s8
ip address add 192.168.99.19/24 dev enp0s8
ip address show dev enp0s8
```

The interface `enp0s8` is set to IP `192.168.99.19` but the trouble is after rebooting `enp0s8` no longer has that IP. This happens because the IP address setup was transient meaning those settings are not reboot-persistent.

---

### 4. HOWTO set (reboot-persistent) static IP and dynamic (DHCP) IP

In this section we shall see how to setup a reboot persistent IP address. For things to be setup correctly, we need to assign `enp0s3` a DHCP (Dynamic Host Configuration Protocol or in other words a dynamic IP) address and we need to assign `enp0s8` a static IP.

---

## Ubuntu (reboot-persistent)

Reference: Network Configuration in Ubuntu

At minimum, these lines work when added to `/etc/netplan/99_config.yaml`:

```yaml
# Created by MF on Sep 29, 2022
#
network:
  version: 2
  renderer: networkd
  ethernets:
    enp0s3:
      # HINT: dhcp4 shown below should change to reflect network setup desired,
      #       the values given below work ONLY in Networking - I (not Networking - III)
      dhcp4: true

    enp0s8:
      addresses:
        - 192.168.99.2/30
      # HINT: route IP shown below should change to reflect network setup desired,
      #       the values given below work ONLY in Networking - I (not Networking - III)
      routes:
        - to:   default
          via:  10.0.2.15
```

Run:

```bash
sudo netplan apply
```

Read `man 5 netplan` for details on the file format used to set IP addresses in Ubuntu and `man -k netplan` for additional man pages to setup networks in Ubuntu.

---

## Debian (reboot-persistent)

**WARNING:** Instead of `allow-hotplug` as given in the linked examples below, use `auto` instead of `allow-hotplug` otherwise you might windup facing networking issues at boot.

* Read and understand HOWTO set a dynamic IP
* Read and understand HOWTO set a static IP

At minimum, these lines work when added the existing contents of `/etc/network/interfaces`:

```text
auto enp0s3
iface enp0s3 inet dhcp

auto enp0s8
iface enp0s8 inet static
  address 192.168.99.19/24
  # gateway goes here

  # if required, tweak order or add additional nameservers but
  # only first three are put into /etc/resolv.conf by resolvconf
  # default
  dns-nameserver 10.102.100.21
  dns-nameserver 1.1.1.1
  dns-nameserver 10.103.100.22

  # alternate
  dns-nameserver 8.8.8.8
  dns-nameserver 10.102.100.22
  dns-nameserver 192.168.0.1

  # desperate: put nameservers that work within your network
  dns-nameserver 192.168.0.1
  dns-nameserver 10.0.0.241
  dns-nameserver 10.101.100.21
  dns-nameserver 10.101.100.22
  dns-nameserver 10.102.100.22
```

Run (if you get errors, install package `resolvconf`):

```bash
resolvconf --enable-updates
resolvconf -u
ifdown enp0s8
ifup enp0s8
nslookup -type=ns debian.org
```

Read `man 8 resolvconf` for details on enabling nameserver resolution in Debian.

---

## 5. Reference Output

Compare your output after rebooting with these values on Seneca Campus:

### `ip address`

```text
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
      valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
      valid_lft forever preferred_lft forever
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 08:00:27:98:e0:c0 brd ff:ff:ff:ff:ff:ff
    inet 10.0.2.15/24 brd 10.0.2.255 scope global dynamic enp0s3
      valid_lft forever preferred_lft forever
    inet6 fe80::a00:27ff:fe98:e0c0/64 scope link
      valid_lft forever preferred_lft forever
3: enp0s8: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 08:00:27:e7:3b:f2 brd ff:ff:ff:ff:ff:ff
    inet 192.168.99.19/24 brd 192.168.99.255 scope global enp0s8
      valid_lft forever preferred_lft forever
    inet6 fe80::a00:27ff:fee7:3bf2/64 scope link
      valid_lft forever preferred_lft forever
```

### `ip route`

```text
default via 10.0.2.2 dev enp0s3
10.0.2.0/24 dev enp0s3 proto kernel scope link src 10.0.2.15
192.168.99.0/24 dev enp0s8 proto kernel scope link src 192.168.99.18
```

### `cat /etc/resolv.conf`

**NOTE:** The output of your `/etc/resolv.conf` may be different. On Seneca campus, I got these values but yours may vary depending on the nameservers your node received when getting its dynamic IP.

```text
# Dynamic resolv.conf(5) file for glibc resolver(3) generated by resolvconf(8)
#     DO NOT EDIT THIS FILE BY HAND -- YOUR CHANGES WILL BE OVERWRITTEN
nameserver 10.102.100.21
nameserver 1.1.1.1
nameserver 10.103.100.22
nameserver 1.1.1.1
```

---

## Hints (Debian)

* On Debian: read `man 5 interfaces` to get help configuring network interfaces.
* Before setting values for `address`, `netmask`, `gateway`, `dns-domain`, and `dns-nameservers`, understand what each of them mean. Read `man interfaces` and the Debian Wiki on Network Configuration.
* For this static IP network interface, do not set a gateway IP (comment out or remove the entire line) because the dynamic interface (which uses DHCP) automatically sets the gateway IP for this node and only one gateway should be set per node.
* Modify the IP values in the reference information for the subnet `192.168.99.0/24` used in this example (see Questions #6 and #7 in the practice questions below for the IP and netmask values used in this example).

---

## Only show IP address and MAC address for a network interface

* Using any command line commands how would you only display the IP address `10.0.2.15/24` in the example above.
* Using any command line commands how would you only display the MAC address `08:00:27:98:e0:c0` in the example above.

---

## Useful command lines

| command                            | purpose                                                         |
| ---------------------------------- | --------------------------------------------------------------- |
| `ip`                               | manage routing, network devices, interfaces, and tunnels        |
| `ip address show`                  | shows ip address                                                |
| `ip -brief address`                | alternate method to show ip address                             |
| `ip -brief -color address`         | colorful method to show ip address                              |
| `ip -4 address show up`            | another method to show IPv4 address on active interfaces only   |
| `sudo ip link set`                 | enable/disable ip interface                                     |
| `ip route`                         | show routing table                                              |
| `sudo dhclient`                    | to get a dynamic address                                        |
| `ping 1.1.1.1`                     | to test network availability                                    |
| `ping senecacollege.ca`            | do a network friendly name lookup (DNS query)                   |
| `getent ahosts senecacollege.ca`   | another way to do DNS lookup                                    |
| `getent ahosts debian.org`         | another way to do DNS lookup                                    |
| `wget -O- debian.org`              | better method of testing Internet connectivity                  |
| `sudo ip address add .. dev ...`   | assign static IP                                                |
| `sudo systemctl stop`              | stop a service like networking/NetworkManager                   |
| `sudo systemctl start`             | start a service like networking/NetworkManager                  |
| `sudo vi /etc/network/interfaces`  | file to edit for setting up network interfaces                  |
| `sudo resolvconf -u`               | overwrite existing `/etc/resolv.conf` with nameserver (careful) |
| `sudo resolvconf --enable-updates` | overwrite existing `/etc/resolv.conf` with nameserver           |
| `nslookup -type=ns debian.org`     | show which nameserver has responded to your request             |
| `host debian.org a.b.c.d`          | query DNS record for debian.org from nameserver a.b.c.d         |

---

## Practice Questions

1. What one line command displays the IP address of an interface?

2. What one line command displays the MAC address of an interface?

3. What is the difference between static and dynamic IP address?

4. What type of address (static or dynamic) was displayed when you display the IP address (in Practice Question #1)? Can you find out what type of address (dynamic or static) it was? If so how do you find out and does the type of address given (static or dynamic) matter?

5. What is required to setup a dynamic address?

6. **IMPORTANT** How do you set the secondary interface to have static IP `192.168.99.98/30` using the `ip` command from the command line? How can you confirm that the IP address was setup correctly?

7. **IMPORTANT** Reboot and check whether the IP address, on the secondary interface, continues to persist beyond the reboot. What file would you edit so the secondary interface gets a reboot-persistent static IP? What settings would you put into that file so the secondary interface gets static address `192.168.99.98/30` that's reboot-persistent?

8. After setting the IP to `192.168.99.98/30` your secondary interface for static addressing correctly, how would you disable your primary interface using the `ip` command? Attempt to connect to the Internet. Were you able to connect to the Internet work? If not? why not?

9. Now enable your primary interface and disable the secondary interface? Are you able to connect to the Internet? Were you able to connect?

10. **IMPORTANT** What commands would you use, from the command line, to do the following:

    * Check whether you have Internet connectivity or not. Show at least 2 different ways of doing this (use two different commands).
    * Enable a network interface (bring a link up).
    * Disable a network interface (bring a link down).
    * Show the IP address with the network address assigned to a network interface.
    * What command displays the gateway IP of your node and why is the default gateway important for your machine? What is the default gateway IP of your DS (Debian Stable) machine?

---

## OPS105 Home

* **Last Updated:** 2025-Sep-02 (Tue) 21:47

```
```
