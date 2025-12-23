# Lab04 - File System Security & Access Control

**Student Name:** Soroush Bastani
**Student ID:** SBastani1  
**Course Section:** NBB 
**Date:** 2025-11-06

---

## Part 1: File Metadata and Permissions

### Commands and Outputs
```
$ ls -la
total 20
drwxrwxr-x 3 ubuntu ubuntu 4096 Nov  6 20:55 .
drwxr-x--- 5 ubuntu ubuntu 4096 Nov  6 20:43 ..
-rw-r--r-- 1 ubuntu ubuntu   11 Nov  6 20:55 notes.txt
drwxr-x--- 3 ubuntu ubuntu 4096 Nov  6 20:55 projects
-rw-r-----+ 1 ubuntu ubuntu   46 Nov  6 20:47 secret.txt

$ stat secret.txt
File: secret.txt
Size: 46              Blocks: 8          IO Block: 4096   regular file
Device: 802h/2050d      Inode: 1835023     Links: 1
Access: (0640/-rw-r-----)  Uid: ( 1000/  ubuntu)   Gid: ( 1000/  ubuntu)
Access: 2025-11-06 23:42:36.697110158 +0000
Modify: 2025-11-06 20:47:11.542338431 +0000
Change: 2025-11-06 22:49:12.792291789 +0000
Birth: 2025-11-06 20:47:11.542338431 +0000
```

### Analysis
- **Explain ownership, mode (symbolic and octal), and timestamps you observed.**
  The `stat` command shows that the `secret.txt` file is owned by the user `ubuntu` and the group `ubuntu`. The access mode is `0640` (symbolic: `-rw-r-----`), which means the owner `ubuntu` has read/write permissions, and members of the `ubuntu` group have read-only permissions. The timestamps (Access, Modify, Change) track when the file was last read, its content changed, or its metadata updated, respectively.

- **Why is directory execute (x) required for traversal?**
  The execute (`x`) permission on a directory acts like a key to a hallway. It grants a user the ability to pass through the directory to access files or subdirectories within it. Without execute permission, you cannot `cd` into the directory or access any of its contents, even if you have read permissions on the files inside. It is essential for navigating the filesystem path.

---

## Part 2: POSIX ACLs — Finer-Grained Access

### Commands and Outputs
```
$ getfacl secret.txt
# file: secret.txt
# owner: ubuntu
# group: ubuntu
user::rw-
group::---
other::---

$ setfacl -m u:fsuser:r-- secret.txt && getfacl secret.txt
# file: secret.txt
# owner: ubuntu
# group: ubuntu
user::rw-
user:fsuser:r--
group::---
mask::r--
other::---
```

### Analysis
- What does the ACL mask do? Which entries does it affect?
The ACL mask acts as a permission ceiling. It defines the maximum permissions that can be granted to any named user, the owning group, and any named group. It does not affect the permissions of the file owner or "other." The effective permission for an entry is the logical AND of what was granted and the mask. For instance, if a user is granted rwx but the mask is r--, their effective permission is only r--.

- Why did fsuser read succeed and write fail?
The read succeeded because a specific ACL entry (u:fsuser:r--) was added, explicitly granting fsuser read permission. After fixing the directory traversal permissions with chmod o+x, fsuser was able to path to the file and read it. The write failed because that same ACL entry did not grant write (w) permission. The system correctly enforced the principle of least privilege defined in the ACL.

---

## Part 3: Extended Attributes and Encryption

### Commands and Outputs
```
$ setfattr -n user.note -v "tag:confidential" notes.txt && getfattr -d notes.txt
# file: notes.txt
user.note="tag:confidential"

$ zip -r secure_bundle.zip projects && \
  openssl enc -aes-256-cbc -salt -in secure_bundle.zip -out secure_bundle.zip.enc
[Commands executed successfully and I was prompted for a password to encrypt the file.]
```

### Analysis
- Security considerations of xattrs (visibility, backup, portability).
Extended attributes (xattrs) are insecure for storing sensitive data because they are easily readable metadata (getfattr). Furthermore, they pose an operational risk because many standard tools (like cp, tar, or some backup software) do not preserve them by default, leading to silent data loss. They are also not portable across all filesystems (e.g., FAT32), so attributes can be stripped when moving files.

- Key/password handling and recovery risks for encrypted archives.
When using openssl for ad-hoc encryption, the password is the only key to the data. It is not stored anywhere. This creates a critical single point of failure: if the password is lost or forgotten, the encrypted data is irrecoverable. There is no "forgot password" option. This poses a significant operational risk without a centralized key management policy, as data can be permanently lost if an employee leaves or forgets the password.



---

## Reflection
1. When would ACLs be preferred over group changes or multiple groups?
ACLs are preferred for handling complex, one-off permission scenarios. For example, if you need to grant a single user from a different team access to one specific file, using an ACL is much cleaner than creating a whole new group just for that one user and one file. ACLs are for managing exceptions to the standard, role-based group permission model.

2. How does the ACL mask affect effective permissions?
The ACL mask acts as a global filter on permissions for all named users and groups. The final, effective permission is the intersection (logical AND) of the permissions granted to the user/group and the permissions allowed by the mask. It provides a way to globally restrict permissions without having to edit every single ACL entry.

3. Why is execute (x) on directories required for traversal?
The execute permission on a directory allows a user to enter it and access the metadata of the files and subdirectories within. Without it, the directory is like a locked room—you cannot pass through it to get to the content inside, even if you have permission on the content itself. It governs the ability to resolve a path.

4. What operational risks do extended attributes and ad‑hoc encryption introduce?
They both introduce risks of data loss and mismanagement. Extended attributes are often not preserved during backups or file transfers, leading to silent loss of important metadata. Ad-hoc encryption creates a massive key management problem; if the user who encrypted a file forgets the password or leaves the organization, the data is permanently lost. It creates unmanaged, inaccessible data silos.
