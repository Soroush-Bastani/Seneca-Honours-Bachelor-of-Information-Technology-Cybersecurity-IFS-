# Lab02B - Linux Ubuntu VM CPU and Memory Analysis Report

**Student Name:** Soroush Bastani

**Student ID:** sbastani1  

**Course Section:** SPR100NBB

**Completion Date:** 2025-10-02  

**Lab Duration:** 2 hour 

---

## Part 1: Ubuntu VM Setup and Configuration

### 1.1 VM Configuration Summary
- **Hypervisor:** VMware Workstation Pro
- **Version:** 17.6.3 build-24583834
- **CPU Cores:** 2
- **Memory:** 4 GB
- **Storage:** 30 GB
- **Network:** NAT

### 1.2 VM Installation and Startup Process
- **Ubuntu ISO Source:** Ubuntu 24.04.3 LTS from https://ubuntu.com/download/desktop
- **Installation Method:** Image loaded from the SSD. Full Interactive Installation.
- **Startup Time:** 18 seconds
- **User Account Created:** ubuntu
- **Initial VM State:** No issues deteceted

---

## Part 2: Linux System Analysis

### 2.1 CPU Analysis Results

#### System Information Commands
- **Processor Information:** Vendor ID: GenuineIntel, CPU Family: 6, Model: 141, Cache Size: 24576 KB
- **Architecture:** x86_64
- **Number of Cores:** 2
- **CPU Model Name:** 11th Gen Intel(R) Core(TM) i7-11800H @ 2.30GHz
- **CPU Frequency:** 2303.998 MHz

#### htop CPU Analysis
- **Current CPU Usage:** Very low, with individual cores at 2.0% and 0.7%
- **Number of CPU Cores Visible:** 2
- **CPU Utilization Pattern:** The system is mostly idle. CPU utilization is minimal and slightly unbalanced, with one core handling the htop process itself while the other is nearly inactive.
- **Process CPU Usage:** htop (2.0%), /usr/libexec/gnome-terminal-server (0.7%)

#### Linux Command Outputs
    # Processor Information Command Output:
	Architecture:                    x86_64
	CPU op-mode(s):                  32-bit, 64-bit
	Address sizes:                   45 bits physical, 48 bits virtual
	Byte Order:                      Little Endian
	CPU(s):                          2
	On-line CPU(s) list:             0,1
	Vendor ID:                       GenuineIntel
	Model name:                      11th Gen Intel(R) Core(TM) i7-11800H @ 2.30GHz
	CPU family:                      6
	Model:                           141
	Thread(s) per core:              1
	Core(s) per socket:              1
	Socket(s):                       2
	Stepping:                        1
	BogoMIPS:                        4607.99
	Flags:                           fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ss syscall nx pdpe1gb rdtscp lm constant_tsc arch_perfmon rep_good nopl xtopology tsc_reliable nonstop_tsc cpuid tsc_known_freq pni pclmulqdq ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt aes xsave avx f16c rdrand hypervisor lahf_lm abm 3dnowprefetch pti ssbd ibrs ibpb stibp fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid avx512f avx512dq rdseed adx smap avx512ifma clflushopt clwb avx512cd sha_ni avx512bw avx512vl xsaveopt xsaves avx512vbmi avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnni avx512_bitalg avx512_vpopcntdq rdpid movdiri movdir64b fsrm avx512_vp2intersect md_clear flush_l1d arch_capabilities
	Virtualization features:         
	Hypervisor vendor:               VMware
	Virtualization type:             full
	Caches (sum of all):             
	L1d:                             96 KiB (2 instances)
	L1i:                             64 KiB (2 instances)
	L2:                              2.5 MiB (2 instances)
	L3:                              48 MiB (2 instances)
	NUMA:                            
	NUMA node(s):                    1
	NUMA node0 CPU(s):               0,1
	Vulnerabilities:                 
	Gather data sampling:            Unknown: Dependent on hypervisor status
	Ghostwrite:                      Not affected
	Indirect target selection:       Mitigation; Aligned branch/thunks
	Itlb multihit:                   Not affected
	L1tf:                            Mitigation; PTE Inversion
	Mds:                             Mitigation; clear CPU buffers; SMT Host state unknown
	Meltdown:                        Mitigation; PTI
	Mmio stale data:                 Not affected
	Reg file data sampling:          Not affected
	Retbleed:                        Mitigation; IBRS
	Spec rstack overflow:            Not affected
	Spec store bypass:               Mitigation; Speculative Store Bypass disabled via prctl
	Spectre v1:                      Mitigation; usercopy/swapgs barriers and __user pointer sanitization
	Spectre v2:                      Mitigation; IBRS; IBPB conditional; STIBP disabled; RSB filling; PBRSB-eIBRS Not affected; BHI SW loop, KVM SW loop
	Srbds:                           Not affected
	Tsx async abort:                 Not affected


    # CPU Performance Output:
    Cpu(s):  0.0 us,  0.0 sy,  0.0 ni,100.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st

### 2.2 Memory Analysis Results

#### System Information Memory Details
- **Total Physical Memory:** 3.8Gi (approximately 3960464 kB)
- **Available Physical Memory:** 2.7Gi (approximately 2820696 kB)
- **Memory Usage Pattern:** The htop output shows memory usage is stable and relatively low, at 852M out of 3.78G. A significant portion of the memory is used for buffers and cache (1.2Gi), which is typical for Linux to improve performance by keeping frequently accessed data in RAM. The primary consumer of memory is the graphical user interface (/usr/bin/gnome-shell). Swap memory is completely unused.
- **Buffer and Cache Information:** Buffers: 41040 kB, Cached: 1104036 kB

#### Linux Memory Commands Output
    # Memory Information:
	
               total        used        free      shared    buff/cache   available
	Mem:       3.8Gi       1.1Gi       1.8Gi        34Mi    1.2Gi        2.7Gi
	Swap:      3.8Gi          0B       3.8Gi

    # Memory Performance:
    MemTotal:        3960464 kB
	MemFree:         1854580 kB
	MemAvailable:    2820696 kB

### 2.3 System Performance Monitoring Results

#### Performance Monitoring Script
- **Monitoring Duration:** 2 minutes
- **Sample Interval:** 5 seconds
- **CPU Usage Range:** 0.0% - 59.1%
- **Memory Usage Range:** 53.5% - 54.8%
- **Performance Patterns Observed:** Memory usage remained very stable, consistently staying within the 53-55% range. This indicates a constant memory footprint with no significant memory allocation or deallocation events during the monitoring period. In contrast, CPU usage was highly volatile, showing several sharp spikes (reaching up to 59.1%) followed by periods of being completely idle (0.0%). This pattern is typical of a system running background tasks or services that activate periodically.

#### htop Resource Monitor Observations
- **Peak CPU Usage:** 99.7% on a single core (during the yes command stress test
- **Peak Memory Usage:** 2.14G / 3.78G (approximately 57% during the Firefox/YouTube test)
- **Resource Usage During Activities:** Light Tasks (Text Editor): Minimal impact. CPU usage remained low (<5%) and memory usage was stable around 1.10G.
CPU Stress Test (yes > /dev/null): This command successfully isolated CPU load, pushing one core to its maximum (99.7%) while having a negligible effect on memory consumption.
Memory Stress Test (Firefox with YouTube): This activity created the highest memory load, consuming 2.14G. It also generated a moderate, sustained CPU load (around 24%) to handle web page rendering and video playback.]

---

## Part 3: Security and Virtualization Analysis

### 3.1 Linux Security Features Status
- **AppArmor Status:** Enabled. The AppArmor module is loaded with 152 profiles active. 55 of these profiles are in "enforce" mode, actively restricting program capabilities, while 5 are in "complain" mode for monitoring.
- **UFW Firewall Status:** Inactive
- **UFW Rules Summary:** The firewall is currently disabled, so no rules are being enforced. By default, when UFW is enabled, its policy is to deny all incoming traffic and allow all outgoing traffic.
- **System Updates Status:** There are 65 packages available for upgrade. The system's package list was just synchronized with the repositories.

### 3.2 VM Isolation Test Results

#### File System Isolation
- **Test File Created:** this_is_a_vm_test_file.txt in the VM's home directory
- **Host System Check:** No
- **Isolation Effectiveness:** The isolation is completely effective. The VM's file system is stored within a single virtual disk file (.vmdk) on the host system, acting as a container. The guest OS (Ubuntu) operates entirely within this container and has no direct access to the host's file system. This sandboxing prevents a guest from accessing or modifying host files, which is a fundamental security principle of virtualization.

#### Process Isolation
- **VM Processes Observed:** Key processes included multiple instances of /snap/firefox/6565/usr/lib/firefox/firefox, /usr/bin/gnome-shell, and htop itself.
- **Host Processes Visible:** No
- **Isolation Observations:** The VM's process list is entirely separate from the host's. The hypervisor allocates specific CPU and memory resources to the VM, and the guest OS (Ubuntu) manages its own processes within that self-contained environment. This is a critical security feature, as it ensures that malware or a crash within the VM cannot directly affect the processes running on the host system, maintaining the host's stability and integrity.

### 3.3 Performance Observation Results

#### CPU Performance Comparison
- **VM CPU Usage:** Around 17.4% while actively browsing YouTube.
- **Host CPU Usage:** 3.4% for the VMware Workstation VMX process.
- **Performance Differences:** The VM's htop reports CPU usage relative to the virtual cores it has been assigned (2 cores). The host's Task Manager reports the VM's usage as a percentage of the entire physical CPU. Therefore, a moderate load (17.4%) inside the VM translates to a much smaller load (3.4%) on the more powerful host system. This illustrates the concept of virtualization where the guest's resource perspective is an abstraction of the actual physical hardware being used.

#### Memory Performance Test
- **Applications Opened:** Firefox, Text Editor, Calculator
- **Initial Memory Usage:** 978M / 3.78G (with only a terminal open)
- **Final Memory Usage:** 1.54G / 3.78G (after opening applications)
- **Memory Behavior Observations:** Memory usage increased by approximately 562MB after launching the applications. This demonstrates the direct impact of application processes on RAM consumption. Each program loads its necessary components into memory, with Firefox being the most significant contributor. The system handled this increase easily without needing to use any swap space.

---

## Analysis and Conclusions

### Key Findings
1. **CPU Performance:** The VM is configured with two virtual cores from a host Intel i7-11800H CPU. Under normal idle conditions, CPU usage is very low but experiences frequent, sharp spikes due to background processes. Stress testing showed that a single virtual core can be maxed out, which represents only a small fraction of the host's total CPU power.
2. **Memory Performance:** The VM has 3.8GB of RAM. The Linux OS efficiently uses a significant portion of this (over 1.2GB) for buffer/cache to improve performance. Memory usage scales predictably with the number and type of applications running, increasing from 978MB at idle to over 1.5GB with a few graphical apps open. Swap memory remained unused, indicating sufficient physical RAM for all tested activities.
3. **Virtualization Overhead:** The performance impact of virtualization is visible but minimal for these tasks. A 17.4% CPU load inside the VM only translated to a 3.4% load on the host, demonstrating the efficiency of the VMware hypervisor in managing and translating workloads.
4. **Security Features:** The VM has active security measures like AppArmor, which is enabled and enforcing application profiles. However, the UFW firewall is inactive by default, and there are 65 pending system updates, representing potential security vulnerabilities. Virtualization itself provides strong security through process and file system isolation, effectively sandboxing the guest OS from the host.

### Technical Insights
- **Linux System Understanding:** This analysis provided practical experience with Linux commands for resource monitoring. I learned to interpret outputs from /proc/cpuinfo and /proc/meminfo to understand hardware details, and to use tools like htop, free, and top to observe real-time CPU and memory behavior, including Linux's heavy reliance on caching.
- **Virtualization Concepts:** The isolation tests concretely demonstrated the "sandboxing" nature of VMs. The inability to see host files or processes from within the guest OS is a fundamental security benefit of virtualization, ensuring that guest system issues do not compromise the host.
- **Performance Monitoring:** I learned how to use htop as a dynamic, user-friendly resource monitor and how to create a simple bash script to log performance metrics over time. This shows how command-line tools can be combined to create powerful, custom monitoring solutions.

### Challenges and Solutions
- **Challenges Faced:** The initial top -n 1 | grep "Cpu(s)" command failed to return any output, which temporarily halted progress.
- **Solutions Applied:** After inspecting the top output, I realized the grep pattern needed to be adjusted. Changing the command to top -n 1 | grep "%Cpu(s)" resolved the issue by matching the correct line format.
- **Lessons Learned:** Command-line tools can be very specific about syntax and output formatting. It's important to first look at the full output of a command before trying to pipe and filter it, ensuring the pattern for grep or awk is correct.

---

**Report Completion Time:** 2 hours  
**Confidence Level:** 9
**Questions for Instructor:** For future labs should I write my answeres like this or put them in brackets [like this]?
