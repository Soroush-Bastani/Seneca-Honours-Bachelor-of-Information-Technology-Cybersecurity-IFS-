# SPR100 Lab01B — Introduction to Our Toolbox (Linux)
**Student Name:** Soroush (Sasha) Bastani

**Student ID:** sbastani1 (119983252)

**Completion Date:** 2025-09-12

## Lab Overview
This lab practices core Linux commands, Markdown documentation, and Git/GitHub submission
workflow using Ubuntu or the Matrix server.
## Learning Objectives
- [x] Navigate the Linux command line
- [x] Create and format Markdown documentation
- [x] Use Git and GitHub for submission
- [x] Follow the course submission process
## Tools Covered
- Linux shell: `pwd`, `ls`, `cd`, `mkdir`, `echo`, `cat`, `nano`
- Markdown basics: headings, emphasis, lists, links, code
- Git/GitHub: init, add, commit, push
## Folder Structure
SPR100_Labs/
└── Lab01B/
├── README.md
├── documents/
├── images/
└── code/
## Reflection
I had authentication and commiting issues. I tried the github PAT but no luck. 
I switched to SSH and it worked fine. 
Since this is Lab01 part 2 (B), I couldn't push to the repo before pulling and setting upstream. 
I'll leave the terminal log below. 
I'll hide parts of the SSH data like a good student!

ubuntu@ubuntu:~/SPR100_Labs$ git init
Reinitialized existing Git repository in /home/ubuntu/SPR100_Labs/.git/
ubuntu@ubuntu:~/SPR100_Labs$ git add .
ubuntu@ubuntu:~/SPR100_Labs$ git commit -m "Initial commit: Lab01B setup"
On branch main
nothing to commit, working tree clean
ubuntu@ubuntu:~/SPR100_Labs$ git branch -M main
ubuntu@ubuntu:~/SPR100_Labs$ git remote add origin https://github.com/sbastani1_seneca/SPR100_Labs
fatal: remote origin already exists.
ubuntu@ubuntu:~/SPR100_Labs$ git remote add origin https://github.com/sbastani1_seneca/SPR100_Labs.git
fatal: remote origin already exists.
ubuntu@ubuntu:~/SPR100_Labs$ git push -u origin main
Username for 'https://github.com': sbastani1_seneca
Password for 'https://sbastani1_seneca@github.com': 
remote: Write access to repository not granted.
fatal: unable to access 'https://github.com/sbastani1_seneca/SPR100_Labs.git/': The requested URL returned error: 403
ubuntu@ubuntu:~/SPR100_Labs$ ^C
ubuntu@ubuntu:~/SPR100_Labs$ git remote -v
origin	https://github.com/sbastani1_seneca/SPR100_Labs.git (fetch)
origin	https://github.com/sbastani1_seneca/SPR100_Labs.git (push)
ubuntu@ubuntu:~/SPR100_Labs$ 
ubuntu@ubuntu:~/SPR100_Labs$ git remote -v
origin	https://github.com/sbastani1_seneca/SPR100_Labs.git (fetch)
origin	https://github.com/sbastani1_seneca/SPR100_Labs.git (push)
ubuntu@ubuntu:~/SPR100_Labs$ git remote -v
origin	https://github.com/sbastani1_seneca/SPR100_Labs.git (fetch)
origin	https://github.com/sbastani1_seneca/SPR100_Labs.git (push)
ubuntu@ubuntu:~/SPR100_Labs$ ^C
ubuntu@ubuntu:~/SPR100_Labs$ cd ~
ubuntu@ubuntu:~$ ssh-keygen -t ed25519 -C "sbastani1@myseneca.ca" 
Generating public/private ed25519 key pair.
Enter file in which to save the key (/home/ubuntu/.ssh/id_ed25519): 
Created directory '/home/ubuntu/.ssh'.
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/ubuntu/.ssh/id_ed25519
Your public key has been saved in /home/ubuntu/.ssh/id_ed25519.pub
The key fingerprint is:
SHA256:0TnV1gxjl/cJo+pILOghFGf2i6QiI2UkUJ+JXn3**** sbastani1@myseneca.ca
The key's randomart image is:
+--[ED25519 256]--+
|o..         ++++o|
|...* +   . + +o++|
| o* * . o = o.o +|
| ooo . . o =   ..|
|.o+ o o S . o    |
|=o + o o . .     |
|+.o . o o   E    |
|   .   . . .     |
|                 |
+----[SHA256]-----+
ubuntu@ubuntu:~$ eval "$(ssh-agent -s)"
Agent pid 5608
ubuntu@ubuntu:~$ ssh-add ~/.ssh/id_ed25519
Enter passphrase for /home/ubuntu/.ssh/id_ed25519: 
Identity added: /home/ubuntu/.ssh/id_ed25519 (sbastani1@myseneca.ca)
ubuntu@ubuntu:~$ cat ~/.ssh/id_ed25519.pub
ssh-ed25519 *****3NzaC1lZDI1NTE5AAAAIF**haYEcN7jDAkffIb+f95IaF8PRcHrHa8VQ***/*** sbastani1@myseneca.ca
ubuntu@ubuntu:~$ l
Desktop/    Music/     SPR100_Labs/
Documents/  Pictures/  Templates/
Downloads/  Public/    Videos/
ubuntu@ubuntu:~$ cd SPR100_Labs/
ubuntu@ubuntu:~/SPR100_Labs$ git remote set-url origin git@github.com:sbastani1_seneca/SPR100_Labs.git
ubuntu@ubuntu:~/SPR100_Labs$ 
ubuntu@ubuntu:~/SPR100_Labs$ git remove -v
git: 'remove' is not a git command. See 'git --help'.

The most similar command is
	remote
ubuntu@ubuntu:~/SPR100_Labs$ git remote -v
origin	git@github.com:sbastani1_seneca/SPR100_Labs.git (fetch)
origin	git@github.com:sbastani1_seneca/SPR100_Labs.git (push)
ubuntu@ubuntu:~/SPR100_Labs$ git push -u origin main
The authenticity of host 'github.com (140.82.114.3)' can't be established.
ECDSA key fingerprint is SHA256:p2QAMXNIC1TJYWeIOt**********.
Are you sure you want to continue connecting (yes/no/[fingerprint])? y
Please type 'yes', 'no' or the fingerprint: yes
Warning: Permanently added 'github.com,140.82.114.3' (ECDSA) to the list of known hosts.
To github.com:sbastani1_seneca/SPR100_Labs.git
 ! [rejected]        main -> main (fetch first)
error: failed to push some refs to 'git@github.com:sbastani1_seneca/SPR100_Labs.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
ubuntu@ubuntu:~/SPR100_Labs$ git pull
warning: no common commits
remote: Enumerating objects: 19, done.
remote: Counting objects: 100% (19/19), done.
remote: Compressing objects: 100% (10/10), done.
remote: Total 19 (delta 1), reused 16 (delta 1), pack-reused 0 (from 0)
Unpacking objects: 100% (19/19), 3.35 KiB | 342.00 KiB/s, done.
From github.com:sbastani1_seneca/SPR100_Labs
 * [new branch]      main       -> origin/main
There is no tracking information for the current branch.
Please specify which branch you want to merge with.
See git-pull(1) for details.

    git pull <remote> <branch>

If you wish to set tracking information for this branch you can do so with:

    git branch --set-upstream-to=origin/<branch> main

ubuntu@ubuntu:~/SPR100_Labs$ git push
fatal: The current branch main has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin main

ubuntu@ubuntu:~/SPR100_Labs$ git push --set-upstream origin main
Warning: Permanently added the ECDSA host key for IP address '140.82.112.3' to the list of known hosts.
To github.com:sbastani1_seneca/SPR100_Labs.git
 ! [rejected]        main -> main (non-fast-forward)
error: failed to push some refs to 'git@github.com:sbastani1_seneca/SPR100_Labs.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
ubuntu@ubuntu:~/SPR100_Labs$ git pull origin main --allow-unrelated-histories
Warning: Permanently added the ECDSA host key for IP address '140.82.113.4' to the list of known hosts.
From github.com:sbastani1_seneca/SPR100_Labs
 * branch            main       -> FETCH_HEAD
hint: Waiting for your editor to close the fileMerge made by the 'recursive' strategy.
 Lab01A/README.md            | 41 ++++++++++++
 Lab01A/code/code.exe        |  0
 Lab01A/documents/blank.docx |  0
 Lab01A/images/blank.bmp     |  0
 Lab01A/test.txt             |  1 +
 README.md                   |  1 +
 6 files changed, 43 insertions(+)
 create mode 100644 Lab01A/README.md
 create mode 100644 Lab01A/code/code.exe
 create mode 100644 Lab01A/documents/blank.docx
 create mode 100644 Lab01A/images/blank.bmp
 create mode 100644 Lab01A/test.txt
 create mode 100644 README.md
ubuntu@ubuntu:~/SPR100_Labs$ git oush
git: 'oush' is not a git command. See 'git --help'.

The most similar command is
	push
ubuntu@ubuntu:~/SPR100_Labs$ git push
fatal: The current branch main has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin main

ubuntu@ubuntu:~/SPR100_Labs$ git push --set-upstream origin main
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (6/6), 661 bytes | 661.00 KiB/s, done.
Total 6 (delta 0), reused 0 (delta 0)
To github.com:sbastani1_seneca/SPR100_Labs.git
   c353b1d..cc87a7a  main -> main
Branch 'main' set up to track remote branch 'main' from 'origin'.
ubuntu@ubuntu:~/SPR100_Labs$ git push
Everything up-to-date
ubuntu@ubuntu:~/SPR100_Labs$ 


