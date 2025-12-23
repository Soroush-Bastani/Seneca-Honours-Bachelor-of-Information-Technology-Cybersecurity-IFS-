# 🔄 Lab03 - Process Management & Scheduling Analysis

**Course:** SPR100 - Introduction to Computer Systems and Security  
**Lab Number:** Lab03  
**Weight:** 4% of final grade  
**Duration:** 3 hours (this lab lasts two weeks: 2 lab sessions) 
**Due Date:** See Blackboard for due date (11:59 PM before the start of the next lab session)

---

## 🎯 Learning Objectives

By the end of this lab, you will be able to:

1. **Investigate process creation and lifecycle** using Linux system tools and commands
2. **Analyze process scheduling policies** and understand how the OS manages CPU time
3. **Examine multithreading concepts** through practical Python-based activities
4. **Identify security implications** of process management in Linux systems
5. **Apply process monitoring and analysis** techniques for system administration

---

## 📋 Pre-Lab Requirements

### Required Software
- **Ubuntu VM** from **Lab02B** (Must be completed first)
- **Python 3.x** (should already be installed on Ubuntu VM, if not, please search online how to install it using `apt`.)
- **Git** (for submission)

### Required Knowledge
- **Completion of Lab02B** (Linux Ubuntu VM Analysis) - **MANDATORY**
- Basic understanding of process concepts from lectures
- Familiarity with Linux command line
- Understanding of virtualization concepts from Lab02B

**Important:** 
- This lab builds directly on the Ubuntu VM environment you set up in Lab02B. Make sure Lab02B is completed before starting this lab.
- Whatever you document, please make sure you understand what they mean, don't just copy and paste without learning what they are -- they are going to appear again in your close-book tests and quizzes later. 
- 
---

## 🚀 Lab Activities

### Part 1: Process Creation and Lifecycle Analysis (60 minutes)

#### 1.1 Linux Process Management

**Use the same Ubuntu VM from Lab02B for all activities in this lab.**

1. **Process Information Commands Analysis:**
   
   **For each command below, document what it does and your specific observations:**
   
   ```bash
   # Command 1: Get all running processes
   ps aux
   ```
   - **What this command does:** [Explain what 'ps aux' shows]
   - **Total process count:** [Count the number of processes - use this command : `ps aux | wc -l` to count the number of processes and learn why it can count the number of processes]
   - **Top 5 CPU users:** [List processes with highest %CPU values]
     - Hint: You need to use the "Sort by" feature in `htop`, please find out how to use it. 
   - **Top 5 memory users:** [List processes with highest %MEM values]
   
   ```bash
   # Command 2: Get process tree structure  
   pstree
   ```
   - **What this command does:** [Explain what pstree shows and how it's different from ps]
   - **Root process observation:** [What's the very top process in the tree?]
   - **Tree depth:** [How many levels deep is the deepest branch?]
   - **Interesting parent-child relationships:** [List 2-3 notable parent-child relationships and write in your own words]
      
   ```bash
   # Command 3: Current user processes
   ps -u $USER 
   ```
   - **What this command does:** [Explain what this `$USER` does]
   - **Your process count:** [How many processes are running under your username?]
   - **Resource usage:** [Which of your processes uses the most CPU/memory? How did you find it?]
   
   ```bash
   # Command 4: Bash process details
   ps -ef | grep -E "(PID|bash)"
   ```
   - **What this command does:** [Explain the pipeline symbol `|` and `grep` filtering. To find out what `grep` is, please search online or read `man grep` in your terminal.]
   - **Bash instances found:** [How many bash processes are running?]
   - **Bash process details:** [List USER, PID, and command details for each bash]
   - **Your current bash:** [Identify which bash process is your current session]

2. **Detailed Process Analysis with `htop`:**
   - Open terminal and type `htop`
   - If not installed: `sudo apt update && sudo apt install htop`
   
   **Step-by-step htop analysis:**
   
   a) **Initial htop Overview (first 2 minutes):**
      - Record the **total number of tasks** shown at the top
      - Record **CPU usage percentages** for each core (colored bars at top)
      - Record **total memory usage** (Mem bar) and **swap usage** (Swp bar)
      - Record **system uptime** and **load averages** (shown at top right)
      - Take note of the **top 5 processes by CPU usage** (PID, name, CPU%)
      - Take note of the **top 5 processes by memory usage** (PID, name, MEM%)
   
   b) **Process Tree Analysis (press F5 to enable tree mode):**
      - Identify the **init process** (PID 1) - what is it called?
      - Find your **bash shell process** - what's its PID and PPID?
      - Locate the **htop process itself** - what's its parent process?
      - Identify **3 system processes** and their parent relationships
      - Document: "Process [name] with PID [number] is child of [parent name] with PPID [number]"
      
   c) **Interactive Testing:**
      - Press **F4** to filter - type "bash" and see what happens
      - Press **F3** to search - search for "systemd" and see what you find  
      - Press **F6** to sort by memory (MEM%) - what are the top 3 memory users?
      - Press **F6** again to sort by CPU% - what are the top 3 CPU users?
      - Press **h** for help - briefly explore 2-3 other functions
      - Press **F2** to play with some settings of `htop`
   
   **Document all findings with specific numbers, process names, and PIDs in your report.**

3. **Process Creation Test:**
- Create a simple shell script
   ```bash
   nano test_process.sh
   ```
   
- Add this content to your `test_process.sh` file:

   ```bash
   #!/bin/bash
   echo "Hello from Process $$"
   echo "Parent PID: $PPID"
   sleep 20
   echo "Process $$ finishing"
   ```
- Make executable
   ```bash
   chmod +x test_process.sh
   ```   

- Run and observe process creation
   ```bash
   ./test_process.sh &
   ```
   - Think: what does this `&` mean in the end of the command above? Find out by searching online. 
   - Find out what the different is between running the script using `./test_process.sh` and `sh test_process.sh`.

- Now check the background process before 20 seconds since you ran the last command. 
   ```bash
   ps -ef | grep test_process
   jobs
   ```

   - Please document what you have found and explain why (not just stating what appears on your screen.)

---

### Part 2: Process Scheduling and Multithreading (60 minutes)

#### 2.1 Linux Process Scheduling Analysis

1. **Process Priority Management:**
   ```bash
   # Check current process priorities
   ps -eo pid,ppid,ni,comm
   
   # Start a process with different nice values
   nice -n 10 sleep 30 &
   nice -n -5 sleep 30 &
   
   # Check the priority differences
   ps -eo pid,ppid,ni,comm | grep sleep
   
   # Change process priority (`renice` command)
   # First, find a PID from above command
   renice 15 -p [PID_OF_SLEEP_PROCESS]
   ```
   - Document what you have found and explain why (not just stating what appears on your screen.)

2. **Python Multithreading Analysis:**
   - Create/copy the python source file: `threading_analysis.py`:
   ```python
   import threading
   import time
   import os
   
   def cpu_intensive_task(name, duration):
       """Simulate CPU-intensive work"""
       print(f"Task {name} started (PID: {os.getpid()})")
       start_time = time.time()
       while time.time() - start_time < duration:
           # CPU-intensive calculation
           result = sum(i**2 for i in range(1000))
       print(f"Task {name} completed")
   
   def main():
       print(f"Main process PID: {os.getpid()}")
       
       # Create multiple threads
       threads = []
       for i in range(4):
           thread = threading.Thread(
               target=cpu_intensive_task, 
               args=(f"Thread-{i}", 8)
           )
           threads.append(thread)
           print(f"Created Thread-{i}")
       
       # Start all threads
       for thread in threads:
           thread.start()
       
       # Wait for all threads to complete
       for thread in threads:
           thread.join()
       
       print("All tasks completed")
   
   if __name__ == "__main__":
       main()
   ```

3. **Run and Monitor Threading:**
   ```bash
   # Terminal 1 （or Tmux Pane 1): Run the Python script
   python3 threading_analysis.py
   
   # Terminal 2 (or Tmux Pane 2): Monitor with htop while script runs
   htop
   
   # Terminal 3 (or Tmux Pane 3): Monitor specific process
   # Find the PID of python3 process and monitor it
   watch -n 1 "ps -p [PYTHON_PID] -o pid,ppid,pcpu,pmem,comm"
   ```
- If you are using Tmux to split your terminal as in Lab02B, a reference layout of your pane can  look like this, which is more convenient than opening multiple terminals:
   ![Tmux Layout](./thread-tmux.png)
- Document what you have found and explain why (not just stating what appears on your screen.)


#### 2.2 Advanced Process Monitoring

1. **Process Monitoring Script:**
   - Create or copy the python source file: `process_monitor.py`
   ```python
   import psutil
   import time
   from datetime import datetime
   
   def monitor_processes():
       print(f"🔍 Process Monitor Started at {datetime.now()}")
       print("-" * 60)
       
       try:
           while True:
               print(f"\n📊 Snapshot at {datetime.now().strftime('%H:%M:%S')}")
               print("Top 5 CPU-consuming processes:")
               
               processes = []
               for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
                   try:
                       processes.append(proc.info)
                   except (psutil.NoSuchProcess, psutil.AccessDenied):
                       pass
               
               # Sort by CPU usage
               top_processes = sorted(processes, key=lambda x: x['cpu_percent'], reverse=True)[:5]
               
               for i, proc in enumerate(top_processes, 1):
                   print(f"{i}. PID: {proc['pid']:>6}, Name: {proc['name']:<15}, "
                         f"CPU: {proc['cpu_percent']:>5.1f}%, Memory: {proc['memory_percent']:>5.1f}%")
               
               time.sleep(5)
       
       except KeyboardInterrupt:
           print("\n🛑 Monitoring stopped by user")
   
   if __name__ == "__main__":
       monitor_processes()
   ```

2. **Install and Run Process Monitor:**
   ```bash
   # Install psutil if not installed
   sudo apt update
   sudo apt install python3-pip
   pip3 install psutil
   
   # Run the monitor
   python3 process_monitor.py
   
   # Let it run for 2-3 minutes while you do other activities
   # Press Ctrl+C to stop the python program
   ```

- Document what you have found and explain why (not just stating what appears on your screen.)
---

### Part 3: Security Implications and Process Analysis (60 minutes)

#### 3.1 Process Security Analysis

1. **Linux Process Security Features:**
   ```bash
   # Check process capabilities
   cat /proc/[PID]/status | grep Cap
   
   # Check process namespaces
   ls -la /proc/[PID]/ns/
   
   # Check process limits
   cat /proc/[PID]/limits
   
   ```
   Search online for the meanings of process capabilities, namespaces, and limits. Get a general idea (you don't need details at this stage) about what they are and what they do. Document what you have found. 

2. **Process Isolation Testing:**
   ```bash
   # Create a test user process
   sudo adduser testuser --disabled-password --gecos ""
   ```
- What does `adduser` command do? 
   ```bash
   # Switch to test user and run a process
   sudo -u testuser bash -c 'sleep 60 &'
   ```
- What does this command do?

   ```bash
   # Check process ownership and isolation
   ps -eo pid,user,comm | grep sleep
   
   # Try to access the process from another user (should fail)
   kill [TESTUSER_SLEEP_PID] 
   ```
- You need to do this within 60 seconds. Why? 
- Document the result of the above `kill` command, and explain why.

#### 3.2 Process Security Monitoring

1. **Security-Focused Process Analysis:**
   ```bash
   # Monitor processes by security context
   ps -eo pid,user,comm,args | head -20
   
   # Check for suspicious processes
   ps aux | awk '$3 > 50.0 || $4 > 50.0' # High CPU/Memory processes
   
   # Monitor new process creation
   # Run this bash script in one terminal while doing activities in another
   while true; do 
       ps -eo pid,ppid,lstart,comm | tail -5
       sleep 2
   done
   ```
- Document what you have found and explain why (not just stating what appears on your screen.)

2. **Process Permissions and Rights:**
   ```bash
   # Check current user processes
   ps -u $USER -o pid,comm,ni,pri
   
   # Check system processes
   sudo ps -u root -o pid,comm,ni,pri | head -10
   
   # Demonstrate privilege separation
   id  # Show current user ID
   sudo id  # Show root privileges when using sudo
   ```
- Find out what each command above does.
- Document what you have found and explain why (not just stating what appears on your screen.)

---

## 📝 Documentation Requirements

### Required Documentation Template

Create a comprehensive lab report using the following template structure:

```markdown
# Lab03 - Process Management & Scheduling Analysis Report

**Student Name:** [Your Full Name]  
**Student ID:** [Your Student ID]  
**Course Section:** [Your Section Number]  
**Completion Date:** [YYYY-MM-DD]  
**Lab Duration:** [Actual time taken - this is a 3-hour lab over two sessions]

---

## Part 1: Process Creation and Lifecycle Analysis

### 1.1 Linux Process Management Results

#### Process Information Commands Analysis

**Command 1: ps aux Analysis**
- **What this command does:** [Your explanation of what ps aux shows]
- **Total process count:** [Number from ps aux | wc -l and explain why this command can count processes]
- **Top 5 CPU users:** [Processes with highest %CPU values - explain how you used htop's "Sort by" feature]
- **Top 5 memory users:** [Processes with highest %MEM values]

**Command 2: pstree Analysis**
- **What this command does:** [Your explanation of pstree vs ps difference]
- **Root process observation:** [The very top process name]
- **Tree depth:** [Deepest branch level count]
- **Parent-child relationships:** [2-3 notable relationships explained in your own words]

**Command 3: ps -u $USER Analysis**
- **What this command does:** [Your explanation of what $USER does]
- **Your process count:** [Number of processes under your username]
- **Resource usage:** [Your highest CPU/memory using process and how you found it]

**Command 4: ps -ef | grep -E "(PID|bash)" Analysis**
- **What this command does:** [Your explanation of pipeline symbol | and grep filtering - include what you learned from man grep]
- **Bash instances found:** [Number of bash processes running]
- **Bash process details:** [List USER, PID, and command details for each bash]
- **Your current bash:** [Which bash process is your current session]

#### htop Detailed Analysis Results

**a) Initial htop Overview:**
- **Total Number of Tasks:** [Number shown at top of htop]
- **CPU Usage per Core:** [List each core's usage percentage, e.g., Core 1: 15.2%, Core 2: 8.7%]
- **Total Memory Usage:** [Memory bar reading, e.g., 2.1GB/8GB (26%)]
- **Swap Usage:** [Swap bar reading, e.g., 0KB/2GB (0%)]
- **System Uptime:** [Time shown in htop header]
- **Load Averages:** [Three load average values]
- **Top 5 CPU Processes:** [List with PID, name, CPU% - e.g., PID 1234, firefox, 12.3%]
- **Top 5 Memory Processes:** [List with PID, name, MEM% - e.g., PID 5678, chrome, 8.2%]

**b) Process Tree Analysis (F5 tree mode):**
- **Init Process:** [Name of PID 1 process, e.g., systemd]
- **Bash Shell Process:** [Your bash PID and PPID, e.g., bash PID 2345 with PPID 1234]
- **Htop Process Parent:** [htop's parent process name and PID]
- **System Process Relationships:** [3 examples, e.g., "systemd-logind PID 567 is child of systemd PID 1"]

**c) Interactive htop Testing Results:**
- **F4 Filter Test:** [What happened when filtering for "bash"]
- **F3 Search Test:** [What systemd processes were found]
- **Top 3 Memory Users:** [Results after F6 memory sort]
- **Top 3 CPU Users:** [Results after F6 CPU sort]
- **F2 Settings:** [What settings did you explore in htop]
- **Additional Functions Explored:** [2-3 other htop functions you tried from help menu]

#### Process Creation Test Results
- **Script Content Created:** [Describe what you put in test_process.sh]
- **Script Process ID:** [PID when test_process.sh was created]
- **Parent Process:** [Parent process name and ID]
- **Background Execution:** [Explain what the & symbol does at the end of ./test_process.sh &]
- **Script Execution Difference:** [Explain the difference between ./test_process.sh and sh test_process.sh]
- **Sleep Duration:** [How long did the script run and why?]
- **Process Lifecycle:** [Describe from creation to termination - explain WHY these things happened]

# Process Creation Command Output:
[Paste the output of: ps -ef | grep test_process]

# Jobs Command Output:
[Paste the output of: jobs]

**Explanation of Findings:** [Explain what you found and WHY you think these results appeared, not just stating what appeared on screen]

---

## Part 2: Process Scheduling and Multithreading

### 2.1 Linux Process Scheduling Analysis

#### Process Priority Management Results
- **Default Nice Values Observed:** [List nice values from ps -eo command]
- **Priority Change Test:** [Describe what happened when you used nice and renice]

# Priority Management Command Output:
[Paste the output of: ps -eo pid,ppid,ni,comm | grep -E "(sleep|test)"]

#### Python Multithreading Analysis
- **Main Process PID:** [PID of the Python script]
- **Number of Threads Created:** [4 threads as per script]
- **Thread Creation Observation:** [What did you observe during thread creation?]
- **CPU Utilization During Threading:** [Describe CPU usage patterns in htop]
- **Thread Execution Pattern:** [Describe how threads executed]

### 2.2 Advanced Process Monitoring Results

#### Process Monitor Script Output
- **Monitoring Duration:** [How long did you run the monitor?]
- **Activities Performed:** [What activities did you do while monitoring?]

# Top Process Monitoring Results:
[Paste 5-10 lines of output from your process_monitor.py script]

#### Performance Patterns Observed
- **CPU Usage Trends:** [Describe CPU usage patterns over time]
- **Memory Usage Trends:** [Describe memory usage patterns over time]
- **Process Behavior:** [Describe interesting process behaviors you noticed]

---

## Part 3: Security Implications and Process Analysis

### 3.1 Process Security Analysis Results

#### Linux Process Security Features
- **Process Capabilities:** [What did you find in /proc/[PID]/status?]
- **Process Namespaces:** [What namespaces did you observe?]
- **Process Limits:** [Key limits from /proc/[PID]/limits]

# Process Security Command Output:
[Paste relevant output from security analysis commands]

#### Process Isolation Testing
- **Test User Creation:** [Was testuser created successfully?]
- **Process Ownership:** [What did ps -eo output show for user ownership?]
- **Permission Denial Test:** [What happened when you tried to kill another user's process?]
- **Isolation Effectiveness:** [How well does Linux isolate processes between users?]

### 3.2 Process Security Monitoring Results

#### Security-Focused Analysis
- **High Resource Processes:** [Any processes using >50% CPU/Memory?]
- **Process Creation Monitoring:** [What new processes did you observe?]
- **Privilege Separation:** [Describe the difference between regular user and sudo rights]

# Security Monitoring Output:
[Paste relevant output from security monitoring commands]

---

## Analysis and Conclusions

### Key Findings
1. **Process Management:** [Summarize process creation and lifecycle findings]
2. **Scheduling Behavior:** [Summarize scheduling and priority observations]
3. **Multithreading Impact:** [Summarize threading effects on system performance]
4. **Security Features:** [Summarize security-related observations]

### Technical Insights
- **Process Lifecycle Understanding:** [What did you learn about Linux process management?]
- **Scheduling Concepts:** [What did you learn about Linux process scheduling?]
- **Multithreading Benefits:** [What did you learn about Python threading in Linux?]
- **Security Considerations:** [What did you learn about process security in Linux?]

### Challenges and Solutions
- **Challenges Faced:** [List any difficulties encountered]
- **Solutions Applied:** [How did you resolve the challenges?]
- **Linux-Specific Learning:** [What did you learn that's specific to Linux process management?]

### Understanding Questions
- **Process vs Thread:** [Explain the difference between processes and threads based on your observations]
- **Nice Values Impact:** [Explain how nice values affect process scheduling]
- **Security Isolation:** [Explain how Linux isolates processes between different users]

---

**Report Completion Time:** [Total time spent on lab]  
**Confidence Level:** [Rate your understanding 1-10]  
**Questions for Instructor:** [List any remaining questions]
```




---

## 🔗 Additional Resources

### Linux Process Management Documentation
- [Linux Process Management](https://man7.org/linux/man-pages/man2/fork.2.html)
- [ps Command Manual](https://man7.org/linux/man-pages/man1/ps.1.html)
- [htop Documentation](https://htop.dev/)

### Python Threading Resources
- [Python Threading](https://docs.python.org/3/library/threading.html)
- [psutil Documentation](https://psutil.readthedocs.io/)

### Security Resources
- [Linux Security Features](https://www.kernel.org/doc/Documentation/security/)
- [Process Capabilities](https://man7.org/linux/man-pages/man7/capabilities.7.html)

---

## 📤 Submission Instructions

Please refer to the [readme.md](../readme.md) file of the Labs root directory for detailed submission instructions.

### What to Submit
1. **Complete Lab03 folder** with all required files
2. **README.md** with comprehensive documentation using the provided template
3. **Python scripts** (threading_analysis.py, process_monitor.py)

### Submission Process
1. Navigate to your lab folder:
   ```bash
   cd [YOUR_LAB_FOLDER]/SPR100_Labs/
   mkdir -p Lab03
   cd Lab03
   ```

2. Copy your lab report to the `Lab03` folder and then add all files:
   ```bash
   git add .
   ```

3. Commit with descriptive message:
   ```bash
   git commit -am "Complete Lab03 - Process Management & Scheduling Analysis"
   ```

4. Push to GitHub:
   ```bash
   git push
   ```

---