````md
# File and Directory Permissions

## Objective

The objective of this lab is to understand file and directory permissions.

---

## Users and Groups

### Get Existing Users and Groups

Let us start by looking at users and groups that exist on a Linux system after installation.

### Check Groups on Linux System

To list groups on your Linux system (showing the last three groups):

```bash
cat /etc/group | tail -3
````

Example output:

```text
lightdm:x:122:
mark:x:1000:
mfernand-stu:x:1001:
```

---

### Check Users on Linux System

To list users on your Linux system (showing the last four users):

```bash
cat /etc/passwd | tail -4
```

Example output:

```text
Debian-exim:x:103:105::/var/spool/exim4:/usr/sbin/nologin
lightdm:x:116:122:Light Display Manager:/var/lib/lightdm:/bin/false
mark:x:1000:1000:Mark Fernandes,,,:/home/mark:/bin/bash
mfernand-stu:x:1001:1001:MySeneca user:/home/mfernand-stu:/bin/bash
```

#### Observations

* Each user gets their **own group**
* Each user gets their **own home directory**

Check detailed user information:

```bash
id mark
id mfernand-stu
```

Example output:

```text
uid=1000(mark) gid=1000(mark) groups=1000(mark),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev),108(netdev),112(bluetooth),116(scanner)
uid=1001(mfernand-stu) gid=1001(mfernand-stu) groups=1001(mfernand-stu)
```

Check home directories:

```bash
ls -ld /home/*
```

Example output:

```text
drwx------  2 root         root         16384 Sep 14 14:30 /home/lost+found
drwxr-xr-x 14 mark         mark          4096 Nov  5 17:00 /home/mark
drwxr-xr-x 27 mfernand-stu mfernand-stu  4096 Nov  9 08:04 /home/mfernand-stu
```

---

## Add a New Group

```bash
su -
addgroup developer
```

Example output:

```text
Adding group `developer' (GID 1002) ...
Done.
```

---

## Add an Existing User to the New Group and Verify

```bash
id mfernand-stu
usermod -g developer mfernand-stu
id mfernand-stu
```

Example output:

```text
uid=1001(mfernand-stu) gid=1001(mfernand-stu) groups=1001(mfernand-stu)
uid=1001(mfernand-stu) gid=1002(developer) groups=1002(developer)
```

---

## User and Group Permissions

### Permissions Table

This table shows how read (`r`), write (`w`), and execute (`x`) permissions correspond to binary and octal values:

```text
Decimal  Binary  Octal  rwx
0        000     0      ---
1        001     1      --x
2        010     2      -w-
3        011     3      -wx
4        100     4      r--
5        101     5      r-x
6        110     6      rw-
7        111     7      rwx
```

---

## Worked Example

### Create a Directory Structure

```bash
cd /tmp
rm -rf /tmp/rough_work
mkdir -p rough_work/secrets
cd /tmp/rough_work/secrets
pwd
```

---

### Recreate Directory as Root

```bash
su -
rm -rf /tmp/rough_work
mkdir -p /tmp/rough_work/secrets
ls -ld /tmp/rough_work
ls -ld /tmp/rough_work/secrets
```

Example output:

```text
drwxr-xr-x 3 root root 4096 Nov  9 14:01 /tmp/rough_work
drwxr-xr-x 2 root root 4096 Nov  9 14:01 /tmp/rough_work/secrets
```

---

### Transfer Ownership and Login as User

```bash
chown -R mfernand-stu:developer /tmp/rough_work
ls -ld /tmp/rough_work
ls -ld /tmp/rough_work/secrets
su - mfernand-stu
```

Example output:

```text
drwxr-xr-x 2 mfernand-stu developer 4096 Nov  9 14:01 /tmp/rough_work
drwxr-xr-x 2 mfernand-stu developer 4096 Nov  9 14:01 /tmp/rough_work/secrets
```

---

### Add Files and Modify Permissions

```bash
touch afile secrets/bfile
ls -l afile secrets/bfile
```

Initial permissions:

```text
-rw-r--r-- 1 mfernand-stu developer 0 Nov  9 14:11 afile
-rw-r--r-- 1 mfernand-stu developer 0 Nov  9 14:11 secrets/bfile
```

Write content:

```bash
echo 'OPS105 in afile' > afile
```

Remove permissions:

```bash
chmod u-w afile
chmod 244 secrets/bfile
```

Results:

```text
-r--r--r-- 1 mfernand-stu developer 16 Nov  9 14:11 afile
--w-r--r-- 1 mfernand-stu developer 21 Nov  9 14:43 secrets/bfile
```

---

### Permission Consequences

```bash
cat afile secrets/bfile
```

Output:

```text
OPS105 in afile
cat: secrets/bfile: Permission denied
```

Attempt to write without permission:

```bash
echo 'another line for afile' > afile
```

Output:

```text
-bash: afile: Permission denied
```

Restore permissions:

```bash
chmod 644 afile
chmod u=rw,go=r secrets/bfile
```

Final verification:

```bash
cat afile secrets/bfile
```

---

## Practice Questions

### Permissions Conversion Table

```text
No  Present       Desired        Octal Command       Symbolic Command
1   rwxr-xr--     ---------      chmod 000 aFile     chmod a= aFile
2   ---------     rwx------      
3   rwx------     rw-r--r--      
4   rw-r--r--     rwxr-xr-x      
5   rwxr-xr-x     rw-rw-r--      
6   rw-rw-r--     -w--w----      
7   -w--w----     --------x     
8   --------x     rwxr-x--x     
9   rwxr-x--x     r---w---x     
10  r---w---x     -------w-     
```

---

### Permissions and Utilities

```text
Object     Read        Write       Execute
File
Directory
```

Explain how permissions affect the following utilities:

* `cat`
* `nano`
* `ls`
* `cd`

---

### Advanced Scenarios

* Create a file and a directory and remove all permissions.
* Move the file into the directory.
* Determine minimum directory permissions required.
* Determine minimum permissions needed to:

  * Edit the file
  * Delete the file
* Test group vs non-group access.
* Configure permissions so non-group users can edit but not delete files.

---

### Execute Permission on Directories

Directory structure:

```text
/tmp/
└── ops105/
    └── puzzleDir/
        └── secretFile
```

Questions:

* What does execute permission on a directory allow?
* What minimum permissions are required on `ops105` and `puzzleDir` so:

  * Anyone can read `secretFile`
  * Only the owner can modify it
* Define **pass-through permissions**
* Show how to set them using:

  * Octal
  * Symbolic

---

## OPS105 Home

* **Last Updated:** 2025-Sep-02 (Tue) 22:09

```
```
