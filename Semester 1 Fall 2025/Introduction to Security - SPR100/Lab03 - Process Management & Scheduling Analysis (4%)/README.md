# Lab03 - Process Management & Scheduling Analysis Report

**Student Name:** Soroush Bastani

**Student ID:** sbastani1

**Course Section:** SPR100NBB

**Completion Date:** 2025-10-16

**Lab Duration:** 2 hours

---

## Part 1: Process Creation and Lifecycle Analysis

### 1.1 Linux Process Management Results

#### Process Information Commands Analysis

**Command 1: ps aux Analysis**
- **What this command does:** The `ps aux` command provides a detailed snapshot of all currently running processes on the system. The `a` flag lists processes from all users, `u` provides a user-oriented format with details like the process owner, and `x` includes processes not attached to a terminal.
- **Total process count:** The command `ps aux | wc -l` returned **205**. This command works by "piping" (sending) the entire multi-line output of `ps aux` into the `wc -l` command, which then counts the total number of lines. This count includes the header line, so the actual number of running processes was 204.
- **Top 5 CPU users:** According to `htop` sorted by CPU usage, the top processes were `htop`, `/sbin/init`, `/lib/systemd/systemd-journald`, `/lib/systemd/systemd-udevd`, and `/lib/systemd/systemd-networkd`.
- **Top 5 memory users:** According to `htop` sorted by memory usage, the top processes were multiple instances of `/usr/lib/snapd/snapd`, `/usr/bin/python3`, `/usr/lib/packagekit/packagekitd`, and `/lib/systemd/systemd-journald`.

**Command 2: pstree Analysis**
- **What this command does:** The `pstree` command displays processes in a hierarchical tree format, which is different from `ps` that shows a flat list. This makes it much easier to visualize the parent-child relationships between processes.
- **Root process observation:** The very top process, and the ancestor of all other processes shown, is **`systemd`**.
- **Tree depth:** The deepest branch in the tree goes down approximately 4 levels (e.g., `systemd` -> `login` -> `bash` -> `pstree`).
- **Parent-child relationships:** Two notable relationships observed were: 1) The `login` process is a child of the main `systemd` process. 2) The user's shell, `bash`, is a child of the `login` process.

**Command 3: ps -u $USER Analysis**
- **What this command does:** The `$USER` variable is automatically replaced by the shell with the name of the currently logged-in user (in this case, `ubuntu`). Therefore, the command lists only the processes owned by the current user.
- **Your process count:** There were **4** processes running under the `ubuntu` username.
- **Resource usage:** From this specific command's output, resource usage is not shown. However, in a typical terminal session, the most resource-intensive processes are the shell itself (`bash`) or any command the user is actively running.

**Command 4: ps -ef | grep -E "(PID|bash)" Analysis**
- **What this command does:** This command demonstrates the use of a pipeline. The pipe symbol `|` sends the complete output of `ps -ef` (list all processes in full format) to the `grep` command. `grep` then filters this output, showing only the lines that contain either "PID" (the header) or "bash".
- **Bash instances found:** There was **1** active `bash` process running.
- **Bash process details:** USER: `ubuntu`, PID: `1139`, PPID: `693`, COMMAND: `bash`
- **Your current bash:** The `bash` process with PID `1139` was the current interactive session.

#### htop Detailed Analysis Results

**a) Initial htop Overview:**
- **Total Number of Tasks:** 26 tasks, 31 threads
- **CPU Usage per Core:** Core 1: 0.0%, Core 2: 0.7%
- **Total Memory Usage:** 296M / 3.79G
- **Swap Usage:** 0K / 3.79G
- **System Uptime:** 00:12:28 (12 minutes, 28 seconds)
- **Load Averages:** 0.07, 0.07, 0.09
- **Top 5 CPU Processes:** `htop`, `/sbin/init`, `/lib/systemd/systemd-journald`, `/lib/systemd/systemd-udevd`, `/lib/systemd/systemd-networkd`
- **Top 5 Memory Processes:** `/usr/lib/snapd/snapd`, `/usr/bin/python3`, `/usr/lib/packagekit/packagekitd`, `/lib/systemd/systemd-journald`, `udisksd`

**b) Process Tree Analysis (F5 tree mode):**
- **Init Process:** The process with PID 1 is `/sbin/init`.
- **Bash Shell Process:** The `bash` shell has a PID of **1139** and its parent's PID (PPID) is **736** (`/bin/login`).
- **Htop Process Parent:** The `htop` process was a child of the `bash` process (PID 1139).
- **System Process Relationships:** A clear example is `/lib/systemd/systemd-journald` (PID 491), which is a child of the main `/sbin/init` process (PID 1).

**c) Interactive htop Testing Results:**
- **F4 Filter Test:** After pressing F4 and typing "bash", the process list was filtered to show **only the `bash` process**. All other processes were hidden from view.
- **F3 Search Test:** [What systemd processes were found]
- **Top 3 Memory Users:** `/usr/lib/snapd/snapd`, `/usr/lib/snapd/snapd`, `/usr/lib/snapd/snapd`
- **Top 3 CPU Users:** `/usr/bin/vmtoolsd`, `/sbin/init`, `/lib/systemd/systemd-journald`
- **F2 Settings:** [What settings did you explore in htop]
- **Additional Functions Explored:** [2-3 other htop functions you tried from help menu]

#### Process Creation Test Results
- **Script Content Created:** A simple bash script was created named `test_process.sh`. The script was designed to print its own Process ID (`$$`) and its Parent's Process ID (`$PPID`), wait for 20 seconds using the `sleep` command, and then print a finishing message.
- **Script Process ID:** When the script was running, it was identified with a Process ID, for instance, **1948** as shown in the `ps` command output.
- **Parent Process:** The parent process was the user's interactive shell, `bash`, which had a PID of **1139**.
- **Background Execution:** The `&` symbol at the end of the `./test_process.sh &` command instructs the shell to run the script in the background. This freed up the terminal prompt immediately for new commands, while the script continued its 20-second lifecycle. The `jobs` command confirmed this, listing the script with a status of "Running".
- **Script Execution Difference:** Running a script with `./test_process.sh` requires the file to have execute permission (set by `chmod +x`). The system uses the shebang line (`#!/bin/bash`) to determine which interpreter to use. In contrast, running it with `sh test_process.sh` explicitly tells the `sh` interpreter to execute the script, and does not require the script file to have execute permissions.
- **Sleep Duration:** The script ran for exactly 20 seconds because of the `sleep 20` command within the script. This command pauses the execution for the specified number of seconds.
- **Process Lifecycle:** The script was created as a child of the main `bash` process. It ran independently in the background for 20 seconds, during which it was visible in the process list. After the sleep duration, it printed its final message and terminated, at which point its status in the `jobs` list changed to "Done".

# Process Creation Command Output:

ubuntu 1948 1139 0 01:33 tty1 00:00:00 /bin/bash ./test_process.sh

ubuntu 1951 1139 0 01:33 tty1 00:00:00 grep --color=auto test_process

# Jobs Command Output:
Stopped htop

Done ./test_process.sh

Running ./test_process.sh

**Explanation of Findings:** The results clearly demonstrate the process lifecycle in Linux. A child process (`test_process.sh`) was spawned from a parent (`bash`). Running it in the background with `&` allowed for concurrent operations. The `ps` and `jobs` commands are effective tools for monitoring the state of these background processes, confirming their existence while active and their completion after their designated task (the 20-second sleep) was finished.

---

## Part 2: Process Scheduling and Multithreading

### 2.1 Linux Process Scheduling Analysis

#### Process Priority Management Results
- **Default Nice Values Observed:** When checking processes with `ps -eo pid,ppid,ni,comm`, it was observed that most user-level processes start with a default "nice" value (NI) of 0. This value indicates a standard priority for CPU scheduling.
- **Priority Change Test:** The `nice` and `renice` commands were used to manipulate process priority.
    1.  A `sleep` process (PID 1187) was started with a lower priority using `nice -n 10`, which successfully assigned it a nice value of 10.
    2.  The `renice 15 -p 1187` command was then used to modify the priority of this already running process.
    3.  The command successfully changed the nice value from 10 to 15, further lowering its scheduling priority. A higher nice value means the process is "nicer" to other processes and will receive less preferential CPU time.

# Priority Management Command Output:
```
ubuntu@ubuntu:~$ nice -n 10 sleep 60 &
[5] 1187
ubuntu@ubuntu:~$ ps -eo pid,ppid,ni,comm | grep sleep
1187   1158  10 sleep
ubuntu@ubuntu:~$ renice 15 -p 1187
1187 (process ID) old priority 10, new priority 15
ubuntu@ubuntu:~$ ps -eo pid,ppid,ni,comm | grep sleep
1187   1158  15 sleep
```

#### Python Multithreading Analysis
- **Main Process PID:** The Python script started and identified its main process with a PID of **1506**.
- **Number of Threads Created:** The script was designed to create **4** worker threads to run tasks concurrently.
- **Thread Creation Observation:** The script's output showed that all four threads were created sequentially by the main process before any of the CPU-intensive tasks began. Crucially, the output also showed that all threads shared the same Process ID (1506) as their parent, confirming they are not separate processes.
- **CPU Utilization During Threading:** In `htop`, the `python3 threading_analysis.py` process immediately jumped to the top of the process list, consuming a very high percentage of CPU resources. The CPU usage was well over 100%, indicating that the threads were running in parallel across multiple CPU cores. The `htop` view also showed multiple entries for the same python script, representing the individual threads that were active.
- **Thread Execution Pattern:** The threads appeared to execute in parallel. The operating system's scheduler distributed the four threads across the available CPU cores to maximize performance, which is the primary benefit of multithreading for CPU-bound tasks.

### 2.2 Advanced Process Monitoring Results

#### Process Monitor Script Output
- **Monitoring Duration:** The script was allowed to run for approximately one minute to gather several snapshots of system activity.
- **Activities Performed:** While the monitor was running, other activities such as running `htop` were performed in a separate terminal. The monitoring script successfully detected these user-initiated processes when they consumed CPU resources.

# Top Process Monitoring Results:
```
📊 Snapshot at 02:45:26
Top 5 CPU-consuming processes:
1. PID:   2814, Name: vmtoolsd       , CPU:   0.8%, Memory:   0.2%
2. PID:   3036, Name: python3        , CPU:   0.8%, Memory:   0.3%
3. PID:   2775, Name: kworker/1:1-events, CPU:   0.2%, Memory:   0.0%
4. PID:     14, Name: rcu_sched      , CPU:   0.2%, Memory:   0.0%
5. PID:   2779, Name: kworker/0:2-events, CPU:   0.2%, Memory:   0.0%

📊 Snapshot at 02:46:51
Top 5 CPU-consuming processes:
1. PID:   2814, Name: vmtoolsd       , CPU:   0.8%, Memory:   0.2%
2. PID:   3036, Name: python3        , CPU:   0.4%, Memory:   0.3%
3. PID:   3047, Name: htop           , CPU:   0.4%, Memory:   0.1%
4. PID:     21, Name: migration/1    , CPU:   0.2%, Memory:   0.0%
5. PID:   1473, Name: kworker/u256:0-events_power_efficient, CPU:   0.2%, Memory:   0.0%

📊 Snapshot at 02:46:56
Top 5 CPU-consuming processes:
1. PID:   2814, Name: vmtoolsd       , CPU:   0.4%, Memory:   0.2%
2. PID:   3036, Name: python3        , CPU:   0.4%, Memory:   0.3%
3. PID:   3047, Name: htop           , CPU:   0.4%, Memory:   0.1%
4. PID:     14, Name: rcu_sched      , CPU:   0.2%, Memory:   0.0%
5. PID:   1342, Name: tmux: server   , CPU:   0.2%, Memory:   0.1%
```

#### Performance Patterns Observed
- **CPU Usage Trends:** The overall CPU usage on the system was generally low, which is expected for a VM that is mostly idle. The CPU percentages for the top processes fluctuated slightly between each 5-second snapshot, demonstrating the dynamic nature of process scheduling.
- **Memory Usage Trends:** The memory usage for the top CPU-consuming processes remained stable and very low, indicating that no memory-intensive tasks were running.
- **Process Behavior:** The script successfully identified a mix of system and user processes. `vmtoolsd` (VMware Tools service) and various `kworker` (kernel worker) threads consistently appeared, which is normal for a virtualized environment. The monitor also correctly identified user processes like `python3`, `htop`, and `tmux` as they became active. This shows the script is an effective tool for real-time system monitoring.
---

## Part 3: Security Implications and Process Analysis

### 3.1 Process Security Analysis Results

#### Linux Process Security Features
- **Process Capabilities:** The capabilities of the user's `bash` shell (PID 3055) were inspected in `/proc/3055/status`. The `CapEff` (Effective Capabilities) was `0000000000000000`, indicating that the shell process does not possess any elevated root-level capabilities and runs with standard user privileges.
- **Process Namespaces:** The namespaces for the `bash` process were viewed in `/proc/3055/ns`. The output showed that the process belongs to a set of namespaces (cgroup, ipc, mnt, net, etc.) that are shared with many other processes on the system, which is typical for a standard user session.
- **Process Limits:** The file `/proc/3055/limits` showed the resource limits imposed on the `bash` process. Many limits, such as 'Max cpu time' and 'Max data size', were set to 'unlimited', while others, like 'Max processes' and 'Max open files', were set to specific, finite numbers to prevent resource exhaustion.

# Process Security Command Output:
```
ubuntu@ubuntu:~$ cat /proc/3055/status | grep Cap
CapInh: 0000000000000000
CapPrm: 0000000000000000
CapEff: 0000000000000000
CapBnd: 000001ffffffffff
CapAmb: 0000000000000000
```

#### Process Isolation Testing
- **Test User Creation:** The `adduser` command was used to successfully create a new user named `testuser`.
- **Process Ownership:** A `sleep` process was started in the background as `testuser`. The command `ps -eo pid,user,comm | grep sleep` correctly identified the process (e.g., PID 3117) and showed its owner as `testuser`.
- **Permission Denial Test:** When an attempt was made to terminate the `testuser`'s process using the `kill 3117` command from the `ubuntu` user's shell, the system immediately blocked the action and returned the error: **`-bash: kill: (3117) - Operation not permitted`**.
- **Isolation Effectiveness:** This test demonstrates a fundamental and critical security feature of Linux. The operating system strictly enforces process isolation between users. A regular user (like `ubuntu`) does not have the permission to interfere with or terminate processes owned by another user (like `testuser`), even though they are on the same system.

### 3.2 Process Security Monitoring Results

#### Security-Focused Analysis
- **High Resource Processes:** The command `ps aux | awk '$3 > 50.0 || $4 > 50.0'` was run to search for processes consuming over 50% of CPU or memory. The command produced no output, indicating the system was healthy and not under excessive load.
- **Process Creation Monitoring:** A `while` loop was used to monitor the creation of new processes in real-time. The script successfully detected the launch of user commands like `htop`, as well as the `ps` and `tail` commands generated by the script itself, proving its effectiveness as a simple monitoring tool.
- **Privilege Separation:** The difference between a regular user and root privileges was clearly demonstrated. Running the `id` command shows the user's identity as `ubuntu` (uid=1000). However, running `sudo id` shows the identity `root` (uid=0). This illustrates the principle of least privilege, where a user operates with limited rights and only elevates them temporarily for specific administrative tasks.

# Security Monitoring Output:
```
ubuntu@ubuntu:~$ ps -u $USER -o pid,comm,ni,pri
   PID COMMAND          NI PRI
  1151 systemd           0  19
  1152 (sd-pam)          0  19
...
ubuntu@ubuntu:~$ sudo ps -u root -o pid,comm,ni,pri | head -10
[sudo] password for ubuntu:
   PID COMMAND          NI PRI
     1 systemd           0  19
     2 kthreadd          0  19
     3 rcu_gp          -20  39
     4 rcu_par_gp      -20  39
...
ubuntu@ubuntu:~$ sudo id
uid=0(root) gid=0(root) groups=0(root)
```

---

## Analysis and Conclusions

### Key Findings
1.  **Process Management:** Linux provides powerful command-line tools like `ps`, `pstree`, and `htop` to view, manage, and understand the entire lifecycle of processes, from their creation as children of parent processes to their termination.
2.  **Scheduling Behavior:** Process scheduling is heavily influenced by "nice" values. It was demonstrated that a user can lower the priority of their own processes (`nice`) and that a superuser can raise the priority of processes. Critical system kernel processes run with a much higher priority than user-level processes.
3.  **Multithreading Impact:** A single process can spawn multiple threads that share the same PID and memory space. These threads can execute in parallel on multi-core systems, leading to significant CPU utilization and faster completion of CPU-bound tasks.
4.  **Security Features:** Linux has robust, built-in security mechanisms. The most fundamental of these is strict process isolation between users, where one user is explicitly denied permission to interfere with another user's processes.

### Technical Insights
- **Process Lifecycle Understanding:** The hands-on labs made the theoretical concepts of PIDs, PPIDs, and parent-child relationships tangible. Watching a background script get created and then terminate was a clear illustration of the process lifecycle.
- **Scheduling Concepts:** The ability to directly change a process's nice value with `renice` and immediately see its `NI` and `PRI` values change provided a clear understanding of how scheduling priorities are managed.
- **Multithreading Benefits:** Observing a single Python script utilize over 100% CPU in `htop` was a powerful demonstration of how multithreading enables true parallelism on modern hardware.
- **Security Considerations:** The failed `kill` command was a simple but profound demonstration of the user-based security model that is fundamental to the stability and security of multi-user operating systems like Linux.

### Challenges and Solutions
- **Challenges Faced:** A minor challenge was encountered when a background `sleep` process terminated before the `renice` command could be applied. Another challenge involved background processes entering a "Stopped" state.
- **Solutions Applied:** The solution was simple troubleshooting: the command sequence was re-run to create a new process, which was then successfully modified. This is a common practice in command-line work.
- **Linux-Specific Learning:** A key takeaway was the power and flexibility of the Linux command line and the `/proc` filesystem. Tools like `ps`, `htop`, and even simple `cat` commands on `/proc` files provide an incredible depth of insight into the inner workings of the operating system.

### Understanding Questions
- **Process vs Thread:** Based on the observations, a **process** is an independent program with its own unique PID and separate memory space (e.g., the `test_process.sh` script). A **thread**, however, is a smaller unit of execution that exists *within* a process. Multiple threads share the same PID and memory space as their parent process, as seen with the `threading_analysis.py` script.
- **Nice Values Impact:** Nice values directly impact how the OS scheduler allocates CPU time. A higher nice value (e.g., 15) means the process has a *lower* priority and is "nicer" to others; it will be given CPU time less frequently when other, higher-priority processes are waiting. A lower nice value (e.g., -5) gives a process a *higher* priority, making the scheduler favor it over standard-priority tasks.
- **Security Isolation:** Linux isolates processes between users by assigning a unique User ID (UID) to every process. The kernel's security model enforces a rule that a process can only send signals (like `kill`, which requests termination) to other processes that have the same UID. The only exception is the superuser (root, UID 0), which can send signals to any process. This was proven when the `ubuntu` user's `kill` command failed with "Operation not permitted" against a process owned by `testuser`.

---

**Report Completion Time:** 3 hours

**Confidence Level:** 10/10

**Questions for Instructor:** None at this time. Thanks for reading.
