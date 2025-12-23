# Lab05 - File System Persistence, Hiding, and Detection

**Student Name:** Soroush Bastani

**Student ID:** sbastani1

**Course Section:** SPR100NBB

**Date:** 2025-11-13

---

## Part 1: Persistence and Concealment

### 1) Hidden Names and Locations (dotfiles)
#### Evidence (outputs/excerpts) and Notes
```
ubuntu@ubuntu:~/SPR100_Labs/Lab05/work$ mkdir -p .cache/.thumbs
ubuntu@ubuntu:~/SPR100_Labs/Lab05/work$ mv note.txt .cache/.thumbs/.note
ubuntu@ubuntu:~/SPR100_Labs/Lab05/work$ ls -la .cache/.thumbs/
total 8
drwxrwxr-x 2 ubuntu ubuntu 4096 Nov 14 01:54 .
drwxrwxr-x 3 ubuntu ubuntu 4096 Nov 14 01:54 ..
-rw-rw-r-- 1 ubuntu ubuntu   25 Nov 14 01:54 .note
```
#### Analysis
- The `note.txt` file became hidden after being renamed to `.note` and moved into a directory structure (`.cache/.thumbs`) where both directories also start with a dot. In Linux, files and directories with names beginning with a dot (`.`) are considered "dotfiles." Standard listing commands like `ls` will not show them by default, requiring a special flag (`ls -a` or `ls -la`) to be viewed. This makes it a simple but effective technique for hiding artifacts from casual observation.

### 2) Extended Attributes (xattrs)
#### Evidence (outputs/excerpts) and Notes
```
ubuntu@ubuntu:~/SPR100_Labs/Lab05/work$ setfattr -n user.tag -v "hidden:lab05" ./.cache/.thumbs/.note
ubuntu@ubuntu:~/SPR100_Labs/Lab05/work$ getfattr -d ./.cache/.thumbs/.note
# file: .cache/.thumbs/.note
user.tag="hidden:lab05"
```
#### Analysis
- The data is stored as a key-value pair in a metadata space associated with the file's inode, known as an extended attribute (xattr). This information does not appear in standard `ls` outputs and is not part of the file's content. The main implication is that many standard tools (like `cp` without the `--preserve=xattr` flag or older backup utilities) may not copy or even recognize this metadata, making it a stealthy way to tag files or store hidden information that can be easily overlooked.

### 3) Immutable Bit Demonstration
#### Evidence (before/after)
```
ubuntu@ubuntu:~/SPR100_Labs/Lab05/work$ echo "do not edit" > lockme.txt
ubuntu@ubuntu:~/SPR100_Labs/Lab05/work$ lsattr lockme.txt
------------------ lockme.txt
ubuntu@ubuntu:~/SPR100_Labs/Lab05/work$ sudo chattr +i lockme.txt
ubuntu@ubuntu:~/SPR100_Labs/Lab05/work$ lsattr lockme.txt
----i------------- lockme.txt
ubuntu@ubuntu:~/SPR100_Labs/Lab05/work$ echo x >> lockme.txt || echo "append denied"
bash: lockme.txt: Permission denied
append denied
```
#### Analysis
- Before setting the immutable bit, the file `lockme.txt` could be written to normally. After setting the immutable bit (`+i`), the file became read-only for *all* users, including the root user. Any attempt to modify, delete, or rename the file resulted in a "Permission denied" error. To safely reverse this, one must use `sudo chattr -i lockme.txt`, which requires root privileges to remove the immutable flag and restore normal write permissions.

### 4) Shell RC Login Hook
#### Evidence
```
# Line added to the end of ~/.bashrc
echo "[Labp5 demo] User login hook executed: $(date)" >> ~/SPR100_Labs/Lab05/work/hook.log

# Output in hook.log after opening a new terminal
ubuntu@ubuntu:~$ tail -n 1 ~/SPR100_Labs/Lab05/work/hook.log
[Labp5 demo] User login hook executed: Fri Nov 14 02:22:04 AM UTC 2025
```
#### Analysis
- A command was appended to the `~/.bashrc` file. This command runs automatically every time a new interactive shell is launched for the user. The risk of modifying RC files is that they provide a simple and often overlooked persistence mechanism. Malicious code placed here will execute with the user's privileges upon login, which can be used to steal data, establish reverse shells, or perform other unauthorized actions.

### 5) systemd User Service (preferred)
#### Unit File Content
```
~/.config/systemd/user/lab05-demo.service
-----------------------------------------
[Unit]
Description=Lab05 benign demo (user)

[Service]
Type=oneshot
ExecStart=/bin/bash -lc 'echo "[Lab05 demo] systemd user service ran: $(date)" >> ~/SPR100_Labs/Lab05/work/hook.log'

[Install]
WantedBy=default.target
```
#### Verification Evidence
```
ubuntu@ubuntu:~$ tail -n 3 ~/SPR100_Labs/Lab05/work/hook.log
[Labp5 demo] User login hook executed: Fri Nov 14 02:22:04 AM UTC 2025
[Labp5 demo] User login hook executed: Fri Nov 14 02:40:37 AM UTC 2025
[Lab05 demo] systemd user service ran: Fri Nov 14 02:48:08 AM UTC 2025

ubuntu@ubuntu:~$ systemctl --user status lab05-demo.service --no-pager
♦ lab05-demo.service - Lab05 benign demi (user)
     Loaded: loaded (/home/ubuntu/.config/systemd/user/lab05-demo.service; enabled; vendor preset: enabled)
     Active: inactive (dead) since Fri 2025-11-14 02:48:08 UTC; 1min 11s ago
    Process: 1273 ExecStart=/bin/bash -lc echo "[Lab05 demo] systemd user service ran: $(date)" >> ~/SPR100_Labs/Lab05/work/hook.log (code=exited, status=0/SUCCESS)
   Main PID: 1273 (code=exited, status=0/SUCCESS)
```
#### Analysis
- A user service persists by being "enabled" via `systemctl --user enable`. This creates a symbolic link in a systemd directory that causes the service to be started automatically when the user's session begins. The execution was confirmed by the new log line in `hook.log` and the `SUCCESS` status from the `systemctl --user status` command. Using the `--user` flag is critical because it specifies that the operation should be performed for the current user's services, not the system-wide services, thus not requiring root privileges and keeping the scope limited.

### 6) Crontab @reboot (if systemd user unavailable)
#### Evidence
```
This step was skipped as the systemd user service method was successful.
```
#### Analysis
- N/A

---

## Part 2: Detection and Mitigation

### 1) Enumerate Hidden Files
#### Evidence
```
# Initial attempt only searched 3 levels deep and failed to find the file
ubuntu@ubuntu:~$ find ~ -maxdepth 3 -name '.*' -type f 2>/dev/null | head -20
/home/ubuntu/.sudo_as_admin_successful
/home/ubuntu/.profile
/home/ubuntu/.bashrc
/home/ubuntu/.bash_history

# Corrected find command searching the entire lab directory
ubuntu@ubuntu:~$ find ~/SPR100_Labs/ -name '.note'
/home/ubuntu/SPR100_Labs/Lab05/work/.cache/.thumbs/.note
```
#### Analysis
- The path `/home/ubuntu/SPR100_Labs/Lab05/work/.cache/.thumbs/.note` looked suspicious because a user-created `.note` file is in an unusual and deeply nested hidden directory, far from the user's home or documents folder. The initial `find` command with `-maxdepth 3` failed to locate it, demonstrating how attackers can evade simple detection scripts by burying files deeper in the filesystem.

### 2) Inspect Metadata, ACLs, and xattrs
#### Evidence
```
ubuntu@ubuntu:~$ stat ~/SPR100_Labs/Lab05/work/.cache/.thumbs/.note
  File: /home/ubuntu/SPR100_Labs/Lab05/work/.cache/.thumbs/.note
  Size: 25              Blocks: 8          IO Block: 4096   regular file
Device: 802h/2050d      Inode: 1835039     Links: 1
Access: (0664/-rw-rw-r--)  Uid: ( 1000/  ubuntu)   Gid: ( 1000/  ubuntu)

ubuntu@ubuntu:~$ getfattr -d ~/SPR100_Labs/Lab05/work/.cache/.thumbs/.note
# file: home/ubuntu/SPR100_Labs/Lab05/work/.cache/.thumbs/.note
user.tag="hidden:lab05"
```
#### Analysis
- The metadata from `stat` showed standard file information. The most revealing discovery came from `getfattr`, which exposed the extended attribute `user.tag="hidden:lab05"`. This is a clear indicator that extra, non-standard information has been attached to the file, which is a common technique for steganography or covertly flagging files.

### 3) Detect Startup Hooks
#### Evidence
```
# Initial grep missed the hook due to a typo ("Labp5" vs "Lab05")
ubuntu@ubuntu:~$ grep -n 'Lab05 demo' ~/.bashrc
# No output

# Corrected, case-insensitive grep finds the hook
ubuntu@ubuntu:~$ grep -i 'labp5' ~/.bashrc
echo "[Labp5 demo] User login hook executed: $(date)" >> ~/SPR100_Labs/Lab05/work/hook.log

# Detecting the systemd service
ubuntu@ubuntu:~$ systemctl --user list-unit-files --type=service | grep -i lab05
lab05-demo.service                            enabled
```
#### Analysis
- Two persistence mechanisms were active: a line in `~/.bashrc` and a `systemd` user service. I would prioritize investigating the `.bashrc` hook first, as it is a very common and simple method, followed immediately by checking for systemd user services, which are a more modern and powerful method for user-level persistence.

### 4) Live Monitoring with inotifywait
#### Evidence
```
# Output from inotifywait running in one terminal
Setting up watches.
Watches established.
/home/ubuntu/SPR100_Labs/Lab05/work/ CREATE lockme.txt
/home/ubuntu/SPR100_Labs/Lab05/work/ ATTRIB lockme.txt
/home/ubuntu/SPR100_Labs/Lab05/work/ MODIFY hook.log
/home/ubuntu/SPR100_Labs/Lab05/work/ MODIFY hook.log
```
#### Analysis
- The events showed a file `lockme.txt` being created and its attributes being changed (from the `chattr` command). It also showed two `MODIFY` events on `hook.log`. These events directly indicated that processes were actively creating and writing to files within the monitored directory, providing a real-time trace of the malicious scripts' activity.

### 5) Mitigation Steps (Before/After Evidence)
#### Evidence
```
# Before .bashrc cleanup
ubuntu@ubuntu:~$ grep -i 'labp5' ~/.bashrc
echo "[Labp5 demo] User login hook executed: $(date)" >> ~/SPR100_Labs/Lab05/work/hook.log
# After .bashrc cleanup
ubuntu@ubuntu:~$ grep -i 'labp5' ~/.bashrc || echo "(bashrc hook removed)"
(bashrc hook removed)

# Before systemd cleanup
ubuntu@ubuntu:~$ systemctl --user list-unit-files --type=service | grep -i lab05
lab05-demo.service                            enabled
# After systemd cleanup
ubuntu@ubuntu:~$ systemctl --user list-unit-files --type=service | grep -i lab05 || echo "(service removed)"
(service removed)

# Before xattr cleanup
ubuntu@ubuntu:~$ getfattr -d ~/SPR100_Labs/Lab05/work/.cache/.thumbs/.note
# file: home/ubuntu/SPR100_Labs/Lab05/work/.cache/.thumbs/.note
user.tag="hidden:lab05"
# After xattr cleanup and moving the file
ubuntu@ubuntu:~$ getfattr -d note.txt 2>/dev/null || echo "(no xattrs)"
(no xattrs)
```
#### Analysis
- **`.bashrc` Hook:** Detected by using `grep` to search for suspicious strings. Removed by editing the `~/.bashrc` file with `nano` (or `sed`) to delete the malicious line.
- **`systemd` Service:** Detected using `systemctl --user list-unit-files`. Removed by first `disabling` the service to break the startup link, then deleting the unit file from `~/.config/systemd/user/`, and finally running `systemctl --user daemon-reload`.
- **`xattr`:** Detected with `getfattr -d`. Removed safely with `setfattr -x user.tag` on the specific file.
- **Immutable Bit:** Detected with `lsattr`. Removed with `sudo chattr -i`.

---

## Reflection
1.  **Where should defenders look first for user-level persistence on Linux?**
    A defender should first look in the user's home directory for modifications to shell startup files like `.bashrc`, `.profile`, and `.bash_login`. The next immediate places to check are the user's crontab (`crontab -l`) and the user's systemd service directory (`~/.config/systemd/user/`). These locations are the most common and easiest ways for an attacker to gain user-level persistence.

2.  **What are strengths/limits of ACLs and xattrs for concealment and for defense?**
    For concealment, their strength is obscurity; standard tools like `ls` do not display them, making them easy to miss. Their limit is that they are easily discovered by attribute-aware tools (`getfacl`, `getfattr`) and are often not preserved by backup or file transfer utilities, causing the hidden data to be lost. For defense, they are powerful for labeling; systems like SELinux use xattrs to enforce mandatory access control. This allows defenders to tag files with security contexts and monitor or block access based on these tags.

3.  **Why is execute (`x`) on directories relevant for detection (traversal)?**
    The execute (`x`) permission on a directory allows a user to traverse it—that is, to access files and subdirectories within it. Without execute permission, a defender's scanning tools cannot `cd` into the directory or access its contents, effectively hiding everything inside. Therefore, ensuring detection tools have traversal permissions is critical to performing a complete and thorough scan of the filesystem for hidden threats.

4.  **What operational risks should you consider before deleting suspicious files (e.g., immutable, ownership, backups)?**
    Before deleting a suspicious file, one must consider several risks. First, the file could be a legitimate system file that has been tampered with; deleting it could break the system. Second, the file may be write-protected with the immutable bit, requiring `sudo` to remove the flag before deletion. Third, deleting the file removes it as evidence, preventing further forensic analysis. The best practice is often to quarantine the file first: move it to a secure location, change its ownership to root, and remove all permissions (`chmod 000`). This neutralizes the threat while preserving the file for investigation.

---

## Appendix (Optional)
- No additional materials.