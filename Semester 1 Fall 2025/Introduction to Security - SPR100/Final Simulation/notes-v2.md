This is the final, polished **Master Cheat Sheet**.

I have removed the duplicate text, organized it logically, and added a **Table of Contents (Index)** at the top.

**How to use this tomorrow:**
1.  Copy **ALL** of the text below.
2.  Paste it into your `EXAM_NOTES.md` file on GitHub.
3.  Use **Ctrl+F** and type the **Index Keyword** (e.g., "LAB 04") to jump to that section instantly.

***

# 📖 SPR100 FINAL EXAM MASTER INDEX

**Use `Ctrl+F` to search for these Section Headers:**

1.  **🚨 CRITICAL SUBMISSION** (The required Git command to finish)
2.  **🐍 TASK 1: PYTHON & BANDWIDTH** (Math logic & Script)
3.  **🕵️ TASK 2: NETWORK SPY** (The Workflow: Push/Pull/Tshark)
4.  **📂 LAB 04: PERMISSIONS** (chmod, ACLs, Immutable files)
5.  **👻 LAB 05: HIDING & PERSISTENCE** (Dotfiles, Cron, Systemd)
6.  **🌐 LAB 06: TSHARK COMMANDS** (Capture & Analysis Filters)
7.  **💻 UTILITIES & FILE MGMT** (Linux commands, Tmux, Git fixes)
8.  **💣 TRICKY SCENARIOS** (What if he changes the question?)

---
---

# 1. 🚨 CRITICAL SUBMISSION

**DO NOT LEAVE THE EXAM WITHOUT RUNNING THIS.**
*Only run this after you have `git add` and `git commit` your actual answers.*

**Linux/Ubuntu Terminal:**
```bash
git commit --allow-empty -m "Final" && git commit --allow-empty -m "Completed" && git push
```

**Windows PowerShell:**
```powershell
git commit --allow-empty -m "Final" ; git commit --allow-empty -m "Completed" ; git push
```

---

# 2. 🐍 TASK 1: PYTHON & BANDWIDTH

**Goal:** Calculate data transfer rate.
**Formula:** `(Total Bytes) / (Total Seconds)`

### The Script Logic (Copy/Paste this into function)
```python
def calculate_bandwidth_gbps(hard_drives, data_size_tb, days):
    # 1. Total Bytes
    # If Decimal (1000): (drives * size) * (1000**4)
    # If Binary  (1024): (drives * size) * (1024**4)
    total_bytes = (hard_drives * data_size_tb) * (1000**4)

    # 2. Total Seconds
    # If Days:  days * 24 * 60 * 60
    # If Hours: hours * 60 * 60
    seconds = days * 24 * 60 * 60

    # 3. Calculate Speed
    bytes_per_second = total_bytes / seconds

    # 4. Final Conversion
    # To GB/s: bytes_per_second / (1000**3)
    # To MB/s: bytes_per_second / (1000**2)
    # To Mbps (Bits): (bytes_per_second * 8) / (1000**2)
    
    return bytes_per_second / (1000**3)
```

**How to Run it:**
```bash
python3 bandwidth.py --hard-drives 100 --data-size 16 --days 3
```

---

# 3. 🕵️ TASK 2: NETWORK SPY (WORKFLOW)

**Goal:** Identify what a script does without reading code.

### The "Push-Pull" Strategy (Avoid Typing)
1.  **Windows:** Create `final.py` -> Git Push.
2.  **Ubuntu:** `git pull`.

### The "Spy" Command (Capture & Run)
Run this single line in Ubuntu to capture traffic and run the script:
```bash
tshark -i any -a duration:5 -w task2.pcap & sleep 2; python3 final.py
```

### The Analysis (Getting Answers)
*   **Find URL:** `tshark -r task2.pcap -Y "dns"`
*   **Find Protocol:** `tshark -r task2.pcap -Y "tls"`

---

# 4. 📂 LAB 04: PERMISSIONS & SECURITY

### 🟢 Basic Permissions (chmod)
*   **Check:** `ls -la filename`
*   **Make Private (Owner only):** `chmod 600 filename`
*   **Make Public (Everyone read):** `chmod 644 filename`
*   **Make Runnable (Script):** `chmod +x filename`
*   **Fix "Permission Denied" on Folder:** `chmod o+x foldername/`

### 🔴 Specific User Access (ACLs)
*   **Check:** `getfacl filename`
*   **Give User Read:** `setfacl -m u:username:r-- filename`
*   **Give Group Read/Write:** `setfacl -m g:groupname:rw- filename`
*   **Remove User:** `setfacl -x u:username filename`
*   **Reset/Wipe ACLs:** `setfacl -b filename`

### 🟣 Immutable Files (Un-deletable)
*   **Check:** `lsattr filename` (Look for `i`)
*   **Lock:** `sudo chattr +i filename`
*   **Unlock (Fix):** `sudo chattr -i filename`

### ⚫ Encryption (OpenSSL)
*   **Encrypt:** `openssl enc -aes-256-cbc -salt -in data.zip -out data.zip.enc`
*   **Decrypt:** `openssl enc -d -aes-256-cbc -in data.zip.enc -out data.zip`

---

# 5. 👻 LAB 05: HIDING & PERSISTENCE

### 🔎 Hiding Files
*   **Hide a file:** Rename it to start with a dot (`mv file .file`).
*   **Find hidden files:** `ls -la` OR `find . -name ".*"`
*   **Hide metadata (Steganography):**
    *   Hide: `setfattr -n user.secret -v "password" file`
    *   Read: `getfattr -d file`

### 🔄 Persistence (Startup Hacks)
*   **Bash Hook (Login):**
    *   Check: `tail ~/.bashrc`
    *   Remove: Edit file and delete line at bottom.
*   **Cron Job (Reboot):**
    *   Check: `crontab -l`
    *   Remove: `crontab -r` (Delete all)
*   **Systemd Service:**
    *   Check: `systemctl --user list-unit-files`
    *   Stop: `systemctl --user disable bad.service`

### 👁️ Monitoring
*   **Watch folder for changes:** `inotifywait -m ~/folder`

---

# 6. 🌐 LAB 06: TSHARK COMMANDS

### 1. Capture Command
```bash
sudo tshark -i any -a duration:15 -w capture.pcap
```

### 2. Analysis Filters (The "-Y" Flag)
| Question | Filter Command |
| :--- | :--- |
| **Find URL** | `tshark -r capture.pcap -Y "dns"` |
| **Check HTTPS** | `tshark -r capture.pcap -Y "tls"` |
| **Check HTTP** | `tshark -r capture.pcap -Y "http"` |
| **Check Ping** | `tshark -r capture.pcap -Y "icmp"` |
| **Detect Port Scan** | `tshark -r capture.pcap -Y "tcp.flags.syn==1 && tcp.flags.ack==0"` |
| **Extract SNI (URL)**| `tshark -r capture.pcap -Y "tls.handshake.extensions_server_name" -T fields -e tls.handshake.extensions_server_name` |

### 3. Extract Clean Data (CSV)
```bash
tshark -r capture.pcap -T fields -e ip.src -e ip.dst -e _ws.col.Protocol -E separator=,
```

---

# 7. 💻 UTILITIES & FILE MGMT

### File Operations
*   **Move/Rename:** `mv old new`
*   **Copy Folder:** `cp -r old new`
*   **Delete Folder:** `rm -rf folder`
*   **Go Home:** `cd ~`

### Tmux (Split Screen)
*   **Start:** `tmux`
*   **Split Top/Bottom:** `Ctrl+b` then `"`
*   **Switch Pane:** `Ctrl+b` then `Arrows`
*   **Exit:** Type `exit`

### Git Fixes
*   **If "Merge Conflict" / "Rejected":**
    1.  Rename bad folder: `mv final final_broken`
    2.  Pull fresh: `git pull`
    3.  Copy files back: `cp final_broken/* final/`

---

# 8. 💣 TRICKY SCENARIOS

### 1. Python: Read from File
If exam says: *"Read inputs from `input.txt` instead of arguments"*:
```python
with open("input.txt", "r") as f:
    # Assumes "100 16 3" is in the file
    data = f.read().split()
    hard_drives = int(data[0])
    size = float(data[1])
    days = float(data[2])
```

### 2. ACL Mask Trap
If you grant permission but it doesn't work (`effective:r--`):
*   **Fix:** `setfacl -m m::rwx filename`

### 3. "Command Not Found"
*   Use `python3` instead of `python`.
*   Use `sudo tshark` instead of `tshark`.
*   Use `./script.sh` to run bash scripts.