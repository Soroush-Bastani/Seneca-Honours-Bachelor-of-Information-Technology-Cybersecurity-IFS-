# 🕵️ Lab05 - File System Persistence, Hiding, and Detection

**Course:** SPR100 - Introduction to Computer Systems and Security  
**Lab Number:** Lab05  
**Weight:** 5% of final grade  
**Duration:** 90 minutes
**Due Date:** See date on Blackboard (11:59 PM before the start of the next lab session)

---

## 🎯 Learning Objectives

By the end of this lab, you will be able to:

1. Explain the difference between security policy (what) and mechanism (how) for file access and startup behavior
2. Demonstrate common user‑level persistence and concealment techniques (for awareness) in a controlled environment
3. Detect hidden files, attributes, ACLs, and startup hooks using standard Linux tools
4. Mitigate simple persistence by disabling/removing user‑level hooks and quarantining suspicious files

This lab builds directly on Lab04 (permissions, ACLs, xattrs) and prepares you for recognizing file‑system‑based persistence.

---

## 📋 Pre-Lab Requirements

### Required Software
- Ubuntu VM from previous labs (Lab02B, Lab03, Lab04)
- Git (for submission)
- Python 3.x (optional)
- The following packages (install them before starting):
```bash
sudo apt update
sudo apt install -y acl attr inotify-tools e2fsprogs nano
```

### Important Notes
- Work in your home directory and user scope only. Do not modify system files under `/etc` or `/usr`.
- Use these exercises only in the provided lab VM. Do not attempt on any production systems.
- Run all commands as your regular user with sudo privileges; do not switch to the `root` user.
- For systemd steps, always use the user manager (`systemctl --user`) — do not run `sudo systemctl` in this lab.
- **Very Important!** You are not just learning how to type in the commands, you are learning how to think about the commands and how they work. For example, you need to understand what `crontab` does and how it works, and in future tests, your task will be checking if you know how to use `crontab` to achieve a certain goal.
- If you attempt an action that requires sudo (e.g., `chattr +i`), use `sudo` from your regular user and supply your password; do not remain logged in as root. If sudo is unavailable, document the issue and continue with the rest of the lab.

---

## 🚀 Lab Activities

### Part 1: Persistence and Concealment (45 minutes)

References — please skim these before typing commands:
- man pages: `bash(1)` (startup files), `systemctl(1)`, `systemd.unit(5)`, `systemd.user(5)`, `crontab(1)`, `crontab(5)`
- man pages: `setfattr(1)`, `getfattr(1)`, `lsattr(1)`, `chattr(1)`, `ls(1)`
- Tutorials: `https://wiki.archlinux.org/title/Systemd/User` (user services)
- Background on dotfiles: `https://wiki.archlinux.org/title/Dotfiles`

Goal: Practice how information and simple actions could be hidden or made to persist at user scope. You will implement benign, clearly visible examples and then document exactly how to detect and remove them in Part 2.

Setup a workspace:
```bash
mkdir -p ~/SPR100_Labs/Lab05/work
cd ~/SPR100_Labs/Lab05/work
echo "secret token: $(date +%s)" > note.txt
```

1) Hidden names and locations (user scope):
```bash
mkdir -p .cache/.thumbs
mv note.txt .cache/.thumbs/.note
ls -la ~ ~/SPR100_Labs/Lab05/work ~/.cache ~/.config  # observe dotfiles
```
- Record: which items became hidden and why dotfiles are not listed by default.

2) Hide metadata via xattrs and observe (from Lab04 knowledge):
```bash
setfattr -n user.tag -v "hidden:lab05" ~/.cache/.thumbs/.note
getfattr -d ~/.cache/.thumbs/.note
```
- Record: where the data lives (xattr) and visibility caveats (backups, copy tools).

3) Make a file harder to casually edit (immutable bit demonstration):
```bash
echo "do not edit" > lockme.txt
lsattr lockme.txt
sudo chattr +i lockme.txt   # Requires sudo; if sudo not available, skip and explain
lsattr lockme.txt
echo x >> lockme.txt || echo "append denied"
```
- Record: behavior with and without the immutable bit; how to reverse it in mitigation.

4) Benign user‑level persistence with shell RC (login hook):
```bash
echo 'echo "[Lab05 demo] User login hook executed: $(date)" >> ~/SPR100_Labs/Lab05/work/hook.log' >> ~/.bashrc
tail -n 3 ~/.bashrc
# Open a new terminal (preferred) or run:
bash -ic 'exit'   # uses an interactive shell so ~/.bashrc is sourced
# If neither works, run: source ~/.bashrc
```
- Record: evidence in `hook.log`. Explain the risk of modifying RC files.

5) User‑level persistence via systemd user service (preferred over system scope for this lab):

- What and why: A systemd "user service" runs under your account (no root). Enabling it makes your command run on login/session. Safer than system‑wide changes and easy to inspect/disable.
  - Note: Do not prefix these commands with `sudo`; user services must be managed with `systemctl --user`. If `systemctl --user` fails with a “Failed to connect to bus” error, skip steps 5.x and document the issue, then complete the cron alternative in Step 6.

5.1. Create the per‑user unit directory (where user services live):
```bash
mkdir -p ~/.config/systemd/user
```
- This path is where systemd looks for your account’s service definitions.

5.2. Create and edit the user service unit file:
```bash
nano ~/.config/systemd/user/lab05-demo.service
```
Paste the following content into that file, then save and exit (in nano: Ctrl+O, Enter, Ctrl+X):
```
[Unit]
Description=Lab05 benign demo (user)

[Service]
Type=oneshot
ExecStart=/bin/bash -lc 'echo "[Lab05 demo] systemd user service ran: $(date)" >> ~/SPR100_Labs/Lab05/work/hook.log'

[Install]
WantedBy=default.target
```
- `[Unit]` describes the unit; `[Service]` defines how/what to run; `Type=oneshot` runs once and exits; `ExecStart` appends a line to `hook.log` so you can verify it ran; `[Install]` + `WantedBy=default.target` lets the service start automatically for your session when enabled.

5.3. Reload the user manager to discover the new unit:
```bash
systemctl --user daemon-reload
```
- systemd reads the new file you just created.

5.4. Enable the service for auto‑start at login/session:
```bash
systemctl --user enable lab05-demo.service
```
- This creates a symlink in your user unit wants/ directory so it runs next time your user session starts.

5.5. Start the service now (test run) and verify output:
```bash
systemctl --user start lab05-demo.service
tail -n 3 ~/SPR100_Labs/Lab05/work/hook.log
```
- You should see a new log line showing the service executed.

5.6. Inspect status and (optional) journal logs:
```bash
systemctl --user status lab05-demo.service --no-pager
journalctl --user -u lab05-demo.service -n 10 --no-pager
```
- Status shows the unit state; `journalctl` shows recent logs for the service.

- Record: enablement status, the new log line, and which commands confirmed it.

6) Crontab @reboot (useful when systemd user not available):
```bash
crontab -l 2>/dev/null || echo "(no crontab)"
(crontab -l 2>/dev/null; echo '@reboot echo "[Lab05 demo] cron @reboot: $(date)" >> ~/SPR100_Labs/Lab05/work/hook.log') | crontab -
crontab -l
```
- Record: where cron stores user jobs on your system; how this creates startup execution.

---

### Part 2: Detection and Mitigation (45 minutes)

References — please skim these before typing commands:
- man pages: `find(1)`, `stat(1)`, `grep(1)`, `getfacl(1)`, `setfacl(1)`, `getfattr(1)`, `setfattr(1)`
- tools: `inotifywait(1)` from `inotify-tools`, `systemctl(1)`, `crontab(1)`
- Tutorials: `https://man7.org/linux/man-pages/` (man page index), `https://wiki.archlinux.org/title/Access_Control_Lists`

Goal: Find what you did in Part 1 and clean it up safely. Explain both the “how” and the “why.”

1) List hidden files and strange names:
```bash
cd ~/SPR100_Labs/Lab05/work
ls -la
find ~ -maxdepth 3 -name '.*' -type f 2>/dev/null | head -20
```
- Record: hidden paths that contain lab artifacts.

2) Inspect metadata, ACLs, and xattrs (reuse Lab04 tools):
```bash
stat ~/.cache/.thumbs/.note
getfacl -p ~/.cache/.thumbs/.note || echo "getfacl not available"
getfattr -d ~/.cache/.thumbs/.note || echo "no xattrs"
```
- Record: which attributes/ACLs are present and what they imply for access.

3) Detect user‑level startup hooks:
```bash
grep -n 'Lab05 demo' ~/.bashrc || echo "no .bashrc hook"
systemctl --user list-unit-files --type=service | grep -i lab05 || echo "no systemd user service"
systemctl --user status lab05-demo.service --no-pager || true
crontab -l 2>/dev/null | nl | grep -i '@reboot' || echo "no @reboot entries"
```
- Record: which mechanisms are active on your system.

4) Monitor file events in real time (spot suspicious activity):
```bash
inotifywait -m ~/SPR100_Labs/Lab05/work -e create,modify,attrib,move,delete
```
- In another terminal, append to `hook.log` and observe the event stream.
- Press `Ctrl+C` to stop `inotifywait` after you collect a few events; leave one terminal running the watcher while you trigger changes from another.

5) Mitigation steps (cleaning up):
```bash
# Remove .bashrc hook (edit carefully; show your edit in report)
sed -i '/\[Lab05 demo\] User login hook executed/d' ~/.bashrc

# Disable and remove systemd user service
systemctl --user disable lab05-demo.service 2>/dev/null || true
rm -f ~/.config/systemd/user/lab05-demo.service
systemctl --user daemon-reload

# Remove cron @reboot line
crontab -l 2>/dev/null | grep -v '@reboot' | crontab - || true

# Remove xattrs and reveal file
setfattr -x user.tag ~/.cache/.thumbs/.note 2>/dev/null || true
mv ~/.cache/.thumbs/.note ~/SPR100_Labs/Lab05/work/note.txt

# Clear immutable flag if set (requires sudo)
sudo chattr -i lockme.txt 2>/dev/null || true

# Verify cleanup
grep -n 'Lab05 demo' ~/.bashrc || echo "(bashrc hook removed)"
systemctl --user list-unit-files --type=service | grep -i lab05 || echo "(service removed)"
crontab -l 2>/dev/null | grep -i '@reboot' || echo "(no @reboot)"
getfattr -d note.txt 2>/dev/null || echo "(no xattrs)"
```
- Record: before/after evidence for each mitigation action.

---

## 🧪 Deliverables

Use the provided submission template and submit the filled report:

- Start from `Labs/Lab05/lab05_submission_template.md`
- Save your completed report as `Labs/Lab05/README.md` (do not include the word "template" in the filename as you are not submitting a template, you are submitting your own report)  
- Your `README.md` must include:
  - Commands you ran and trimmed outputs (only the relevant lines)
  - Clear explanations of: dotfiles, xattrs, ACLs, immutable bit, and user‑level startup hooks
  - A concise “playbook” describing how to detect and remove each technique you created

### Reflection Prompts
1. Where should defenders look first for user‑level persistence on Linux?
2. What are strengths/limits of ACLs and xattrs for concealment and for defense?
3. Why is execute (`x`) on directories relevant for detection (traversal)?
4. What operational risks should you consider before deleting suspicious files (e.g., immutable, ownership, backups)?

---

## 📤 Submission Instructions

Follow the same submission flow as previous labs:
1. Place your lab `README.md` and any artifacts in `Labs/Lab05/`
2. Commit and push before the deadline

Suggested commit message:  
"Complete Lab05 - File System Persistence, Hiding, and Detection"

---

