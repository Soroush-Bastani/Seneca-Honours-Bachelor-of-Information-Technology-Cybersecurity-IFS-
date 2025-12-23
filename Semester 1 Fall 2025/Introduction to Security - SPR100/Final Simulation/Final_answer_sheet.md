# SPR100 Final Test Answer Sheet (Template)

Course: SPR100 - Introduction to Computer Systems and Security  


---

## Student Information

**Student Name:** Soroush Bastani
**Student Number:** 119983252
**Student Username:** sbastani1
**Course Section:** NBB
**Date:** 2025-12-05

---

## Answer Sheet

### Task 1

- **Bandwidth:** 6.17 GB/s
- **Explanation of your calculation:** 

#### Step A: Calculate Total Data
*   You have **100** drives.
*   Each is **16 TB**.
*   Total = 100×16=1600 TB

**Crucial Conversion:** The computer doesn't do math in "TB". It does math in "Bytes".
*  1 TB = 1 , 000 , 000 , 000 , 000 Bytes 1 TB=1,000,000,000,000 Bytes ( 1000 × 1000 × 1000 × 1000 1000×1000×1000×1000 ).
*   So, 1600 × (1000^4) = A massive number of bytes

#### Step B: Calculate Total Time
*   You have **3 Days**.
*   Computers count in **Seconds**.
*   Hours: 3 x 24 = 72
*   Minutes: 72 x 60 = 4320.
*   Seconds: 4320 x 60 = 259,200 seconds (in 3 days)

#### Step C: The Division
*   Take the massive number of Bytes from Step A.
*   Divide it by the Seconds from Step B.
*   The result is **Bytes per Second**.

#### Step D: The Final Polish (GB/s)
*   The result from Step C is huge (e.g., 6,000,000,000).
*   To make it readable (GB), we divide by 1,000,000,000 ($1000^3).
*   Result: **6.17 GB/s**.


- **Lines you modified in the python program:** 
```python
# 1. Total Data: (Drives * Size) * (1000^4 conversion to bytes)
    total_bytes = (hard_drives * data_size_tb) * (1000**4)

# 2. Total Time: Days * 24 hours * 60 mins * 60 seconds
    seconds = days * 24 * 60 * 60

# 3. Speed: Bytes / Seconds
    bytes_per_second = total_bytes / seconds
    
# 4. Final: Convert to GB/s (Divide by 1000^3)
    gb_per_second = bytes_per_second / (1000**3)
```

- **Output of your python program:** 
```
=== Alice's Car Bandwidth Calculation ===
Hard drives        : 100
Data size per drive: 16.0 TB
Travel time        : 3.0 days

Bandwidth          : 6.173 GB/s
```

### Task 2

Please run the python program we provide here: `Final_Test/Final_Simulation/final.py` and run `tshark` or `wireshark` to capture the network traffic of the python program.

Please try to find out what did the python program do, by identifying:
- What website does the python program access?
- What protocol(s) are used by the python program?
- What did the python program do in network level during the execution of it?

- **Website URL:**  https://www.google.com
- **Protocols:**  DNS, HTTPS (TLS), TCP
- **Explanation of what the python program does:**  The program resolves the domain www.google.com using DNS. It then establishes a TCP connection and performs a TLS handshake (HTTPS) to securely download the homepage content. Finally, it prints the first 200 bytes of the downloaded HTML to the screen.



