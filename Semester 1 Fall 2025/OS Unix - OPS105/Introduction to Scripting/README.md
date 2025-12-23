````md
# Introduction to Scripting

## Objective

The objective of this lab is to introduce scripting.

---

## What to Do

### Step 1: Run a Simple Command

Run the following command:

```bash
echo "OPS105: Hello Bash"
````

Output:

```text
OPS105: Hello Bash
```

---

### Step 2: Create a Script File

Using your favourite editor, create a file called `hello` and add the following content:

```bash
#!/bin/bash

echo "OPS105: Hello Bash"
```

Verify the contents of the file:

```bash
cat hello
```

Output:

```text
#!/bin/bash

echo "OPS105: Hello Bash"
```

---

### Step 3: Check File Permissions

Before making it a script, check the initial file permissions and try to run it:

```bash
ls -l hello
```

Example output:

```text
-rw-r--r-- 1 mfernand_stu mfernand_stu 39 Nov 12 16:27 hello
```

Attempt to run the script:

```bash
./hello
```

Output:

```text
-bash: ./hello: Permission denied
```

---

### Step 4: Make the File Executable

Change the permissions of `hello` to make it executable:

```bash
chmod a+x hello
```

Verify permissions again:

```bash
ls -l hello
```

Output:

```text
-rwxr-xr-x 1 mfernand_stu mfernand_stu 39 Nov 12 16:27 hello
```

Run the script:

```bash
./hello
```

Output:

```text
OPS105: Hello Bash
```

---

### Step 5: Move the Script to Another Directory

Create a directory called `rough-work` and move the script into it:

```bash
mkdir -p rough-work
mv hello rough-work
```

Attempt to run the script from the current directory:

```bash
hello
```

Output:

```text
-bash: ./hello: command not found
```

---

### Step 6: Understanding the Error

The error occurs because the script `hello` is no longer in the **search path** (`$PATH`).

To run the script correctly, you can do one of the following:

#### Option 1: Run Using the Full or Relative Path

```bash
rough-work/hello
```

Output:

```text
OPS105: Hello Bash
```

#### Option 2: Change to the Script’s Directory

Check your current directory:

```bash
pwd
```

Change into the directory containing the script:

```bash
cd rough-work
pwd
```

Example output:

```text
/tmp
/tmp/rough-work
```

Run the script:

```bash
./hello
```

Output:

```text
OPS105: Hello Bash
```

---

```
```
