````md
# SPR100 Midterm Simulation

**Course:** SPR100 – Introduction to Computer Systems and Security  
**Length:** 80 minutes (simulation practice)  
**Coverage:** Labs 01A, 01B, 02A, 02B, 03  
**Form:** Semi-open-book (see Rules)

---

## Purpose

This simulation lets you practice the exact workflow and expectations for the real midterm.  
If you completed and understood Labs 01–03, this should feel straightforward.

---

## Rules (Semi-Open-Book)

- All work must be done on the **security lab computer**.
- You may **NOT** use your own personal computer.

### You may use:
- Textbooks and manuals  
- Your own lab notes and previous submissions  
- Your VMs on your SSD  

### You may NOT use:
- Internet browsing (except GitHub)  
- Online searches  
- AI assistants  

---

## What You Will Submit

Create a folder named `midterm` at the root of your `SPR100_Labs` repository and place your completed answer sheet inside:

```text
SPR100_Labs/
├── Lab01A/
├── ...
└── midterm/
    └── midterm_answer_sheet.md
````

---

## Template File

Use the provided template file:

```text
Midterm_Test/Midterm_Simulation/midterm_answer_sheet.md
```

Copy it into your `SPR100_Labs/midterm/` folder and fill it in.

---

## How to Submit (REQUIRED Finalization Command)

From your `SPR100_Labs` folder:

### Linux (Ubuntu VM or Matrix)

```bash
git commit --allow-empty -m "Midterm" && git commit --allow-empty -m "Completed" && git push
```

### Windows VM (PowerShell)

```powershell
git commit --allow-empty -m "Midterm" ; git commit --allow-empty -m "Completed" ; git push
```

> **Important:**
> If you do **not** use this exact command to push your midterm answers, your submission **cannot be graded** by the marking scripts and marks will be deducted.

---

## Mock Tasks (Simple Practice)

Perform the following tasks and record outputs/answers in your `midterm_answer_sheet.md`.

---

## Task 1: Run a Python Script on Matrix

* From `Midterm_Test/Midterm_Simulation/`, copy the Python script to Matrix
* Run the script and record the output

**File:**

```text
hello.py
```

---

## Task 2: Run a PowerShell Script in Your Windows VM

* From `Midterm_Test/Midterm_Simulation/`, copy the PowerShell script to your Windows VM
* Run the script and record the output

**File:**

```text
hello.ps1
```

---

## Task 3: Run a Bash Script in Your Ubuntu VM

* From `Midterm_Test/Midterm_Simulation/`, copy the Bash script to your Ubuntu VM
* Run the script and record the output

**File:**

```text
hello._sh
```

**Note:**
Rename `hello._sh` to `hello.sh` after downloading it.

```
```
