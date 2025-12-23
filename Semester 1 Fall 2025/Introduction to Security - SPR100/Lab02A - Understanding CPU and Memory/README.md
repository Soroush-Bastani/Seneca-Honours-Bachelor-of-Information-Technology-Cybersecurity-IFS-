# Lab02A - Windows VM CPU and Memory Analysis Report
**Student Name:** Soroush Bastani
**Student ID:** sbastani1
**Course Section:** SPR100NBB.04814.2257
**Completion Date:** 2025-09-23
**Lab Duration:** 2 hours
---
## Part 1: Virtual Machine Setup and Configuration
### 1.1 VM Configuration Summary
- **Hypervisor Name:** VMware® Workstation 17 Pro
- **Hypervisor Version:** 17.6.4 build-24832109
- **CPU Cores:** 1 processor, 2 cores per processor
- **Memory:** 4096 MB (4 GB)
- **Storage:** 60 GB Maximum Capacity (25.1 GB currently used)
- **Network:** NAT (Network Address Translation)

### 1.2 VM Import and Startup Process
- **VM File Source:** `\\mydrive\courses\SPR100\Win10`
- **Import Method:** The virtual machine was imported by opening the `win_nov22.ova` file in VMware Workstation Pro. The OVA (Open Virtualization Appliance) package contains the complete, pre-configured VM.
- **VM Name:** win10-sbastani1
- **Storage Path:** A dedicated folder on an external SSD drive.
- **Startup Time:** Approximately 1 minute and 15 seconds from power-on to the Windows login screen.

### 1.3 Initial System Configuration
- **Password Change Process:** The initial password for the 'Student' account was changed by navigating to Settings > Accounts > Sign-in options > Password, and then following the prompts to enter the old password (`Ch@ng3m3!`) and set a new one (`123`).
- **Git Installation:** Git for Windows was installed by opening PowerShell and running the command `winget install Git.Git`. The installation proceeded by following the on-screen prompts provided by the Windows Package Manager.
---
## Part 2: Windows System Analysis
### 2.1 CPU Analysis Results
#### System Information (msinfo32)
- **Processor Name:** 12th Gen Intel Core i7-12700
- **Number of Cores:** 2
- **Logical Processors:** 2

#### Task Manager CPU Analysis
- **Current CPU Utilization:** 5%
- **Number of Virtual Processors:** 2
- **CPU Base Speed:** 2.11 GHz
- **CPU Current Speed:** 2.11 GHz
- **System Up Time:** 0:00:17:50 (17 minutes, 50 seconds)
- **CPU Utilization Observations:** During the observation period, the CPU utilization remained consistently low, hovering around 5%. This is expected behavior for a system that is mostly idle, with only background processes and the monitoring tools themselves consuming resources.

### 2.2 Memory Analysis Results
#### System Information Memory Details
- **Total Physical Memory:** 4.00 GB
- **Available Physical Memory:** 2.18 GB
- **Total Virtual Memory:** 5.37 GB
- **Available Virtual Memory:** 3.63 GB
- **Virtual Memory Explanation:** Virtual Memory is a memory management technique where the operating system uses a combination of the computer's physical RAM and a dedicated file on the hard disk (the page file) to create a larger address space for applications. When physical RAM is full, the OS moves the least-used data "pages" to the page file, freeing up RAM for active processes. This allows the system to run more applications than it could with RAM alone.

#### PowerShell Memory Commands Output
**Physical Memory Information:**
```powershell
__PATH          : \\DESKTOP-4H9E4CT\root\cimv2:Win32_PhysicalMemory.Tag="Physical Memory 0"
Capacity        : 4294967296
```
- **Document:** The `__PATH` shows the WMI object path for the physical memory module, and the `Capacity` is 4,294,967,296 bytes, which is equivalent to 4 GB.

**Available Memory Information:**
```powershell
Timestamp                 CounterSamples
---------                 --------------
9/19/2025 10:17:56 AM     \\desktop-4h9e4ct\memory\available mbytes : 2092
```
- **Available Memory:** 2092 MB

### 2.3 System Performance Monitoring Results
#### Performance Monitor Data Collector Set
- **Data Collector Set Name:** Lab02A_Performance_Monitoring
- **Sample Interval:** 5 seconds
- **Duration:** 2 minutes
- **Counters Monitored:**
 - Processor: % Processor Time
 - Memory: Available MBytes
 - Physical Disk: % Disk Time
- **Log Location:** `C:\Users\Student\Documents\DESKTOP-4H9E4CT_20250923-000001\DataCollector01.blg`

#### Performance Data Summary
- **CPU Usage Range:** 1% - 5% during the 2-minute monitoring period.
- **Memory Available Range:** 1703 MB - 2150 MB during monitoring.
- **Disk Usage Range:** 0% - 2% during monitoring.
- **Performance Patterns Observed:** The system remained in a stable, idle state. There were no significant spikes in resource usage, indicating that only background services were active. The slight fluctuations in memory were likely due to Windows' own memory management processes.

#### Resource Monitor Observations
- **Peak CPU Usage:** 5% at 100% Maximum Frequency, with `MsMpEng.exe` (Microsoft Defender) being the most active process at 2.70 Average CPU.
- **Peak Memory Usage:** 57% of Physical Memory was in use (2358 MB), with `explorer.exe` having the largest working set at 242,036 KB.
- **Resource Usage During Activities:** During monitoring, disk activity was minimal, peaking at 2% active time. The `System` process and `svchost.exe` generated the most I/O, which is typical for background OS operations.

#### Performance Monitor Data Collector Graph
![Performance Monitor Data Collector Graph](images/performance_chart.gif)

- **How You Extracted:** The `performance_chart.gif` file was moved from the VM to the host computer by configuring a Shared Folder in VMware Workstation settings. This allowed direct access to a folder on the host machine from within the VM's File Explorer, enabling a simple copy-and-paste transfer. I could've uploaded/emailed the file to myself as well.
---
## Analysis and Conclusions
### Key Findings
1. **VM Configuration:** Setting up and configuring the VM was straightforward. Adjusting the allocated RAM from the default 2 GB to 4 GB was a critical step for ensuring smooth performance of the Windows 10 OS.
2. **CPU Performance:** The VM was allocated 2 logical processors. Analysis showed that for light tasks like monitoring and basic navigation, the CPU utilization was very low, indicating the allocation was more than sufficient.
3. **Memory Management:** The system utilized both physical and virtual memory effectively. With 4 GB of RAM, nearly half was available during idle periods, showing that this is a good baseline for this operating system.
4. **Performance Monitoring:** Windows Performance Monitor and Resource Monitor are powerful built-in tools. They provide detailed, real-time, and logged data on key system resources, which is essential for identifying performance bottlenecks and understanding system behavior.

### Technical Insights
- **System Architecture Understanding:** This lab provided a practical understanding of how an operating system views its hardware. It clarified the distinction between physical CPU cores and the logical processors presented to the OS, and how RAM and disk space are combined to form virtual memory.
- **Virtualization Concepts:** The process highlighted how a hypervisor (VMware Workstation) abstracts the host machine's physical hardware to create a self-contained virtual environment. Allocating specific amounts of CPU and RAM directly impacts the VM's performance.
- **Performance Monitoring Tools:** I learned that Performance Monitor is excellent for logging data over time to analyze trends, while Resource Monitor is ideal for a real-time, detailed view of which specific processes are using system resources.
- **PowerShell Commands:** Using PowerShell to retrieve system information (like `Get-WmiObject` and `Get-Counter`) is a fast and scriptable alternative to navigating through GUI-based tools, demonstrating its power for system administration.

### Challenges and Solutions
- **VM Setup Challenges:** The primary challenge was the initial sluggishness of the VM before its memory was reconfigured. The default 2 GB of RAM was insufficient for a smooth Windows 10 experience.
- **Performance Monitoring Issues:** No significant issues were encountered with the performance tools themselves. The process of setting up a Data Collector Set was logical and well-documented in the lab instructions.
- **File Transfer Challenges:** The main challenge was moving the final `performance_chart.gif` from the isolated VM environment to the host PC for submission.
- **Solutions Applied:** The VM's performance issue was resolved by shutting it down and increasing its allocated RAM to 4 GB in the VM settings. The file transfer was accomplished by setting up a VMware Shared Folder, which proved to be an efficient and seamless solution.
- **Lessons Learned:** Always check the recommended system requirements for a guest OS before running it. Allocating adequate resources from the start saves time. Additionally, learning the hypervisor's integration features, like shared folders, is crucial for an efficient workflow.

### Understanding Questions
- **Virtual Memory Concept:** Virtual memory is a feature of an operating system that allows a computer to compensate for shortages of physical memory by temporarily transferring pages of data from RAM to disk storage. This creates the illusion that the computer has more RAM than it actually does, enabling it to run larger applications or more applications simultaneously. It's important because it prevents "out of memory" errors and allows for more efficient multitasking.
- **VM Resource Allocation:** VM resource allocation is the process of assigning a portion of the host computer's physical resources (CPU cores, RAM, disk space) to a virtual machine. This allocation directly defines the VM's performance capabilities. Allocating more resources will generally make the VM faster and more responsive, but it will leave fewer resources available for the host OS and other VMs.
- **Performance Monitoring Value:** Performance monitoring is critically important in system administration because it provides the necessary data to ensure system reliability, efficiency, and availability. It allows administrators to proactively identify performance bottlenecks (e.g., a slow disk or insufficient memory), troubleshoot issues, plan for future capacity needs (capacity planning), and ensure that applications are running optimally.
---
**Report Completion Time:** 2 hours
**Confidence Level:** 10/10