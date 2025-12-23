# Lab 5
In this lab, you will create five Python scripts. All scripts must be written in GitHub Codespaces.<br>
So far, you have created Python scripts that take input either through the input() function or from command-line arguments using the `sys.argv` list. However, programs often need to work with external data stored in files. Being able to read data from a file and save processed results back to a file is a crucial programming skill. In this lab, you will learn how to:
- Open a text file.
- Read its contents in different ways.
- Process the data.
- Write results back to a file.

# Lab Objectives
- Understand the importance of file handling in programming and real-world applications.
- Open and close files in Python using the open() and close() functions.
- Read file contents using different methods: read(), readline(), and readlines().
- Write data to a file using different file modes ('w', 'a').
- Explain the differences between reading the entire file, reading line by line, and reading into a list.
- Apply file operations to solve simple tasks, such as processing text data, logging results, or saving program output.
  
# Submission Instructions
For each task:
1. **Write the script** in Codespaces.  
2. **Run the script** from the **terminal**.  
3. **Take a screenshot** that clearly shows:  
   - Your **code** in the editor.  
   - The **terminal output**, including your **username** visible in the terminal.  
4. **Insert the screenshot** into a Word document under the heading that matches the task name:  
   - Example: **Lab5a**, **Lab5b**, **Lab5c**, etc.  
5. After completing all tasks, **convert the Word document to PDF**.  Name the PDF file using your **yoursenecausername.pdf**
6. **Submit the PDF file** as your final lab submission on Blackbaord.

## INVESTIGATION 1: BASIC FILE OPERATIONS
File operations are very common in programming. For example, they are used for logging output or errors, storing configuration data, and handling temporary files. You will now explore some of the most useful file functions in Python.
You can use the following functions while working with files in python :

Here are some commonly used file functions in Python:

- **`open()`** – Opens a file in a specified mode (e.g., read `'r'`, write `'w'`, append `'a'`).  
  Returns a file object.  
  ```python
  f = open("data.txt", "r")
  ```

- **`read()`** – Reads the entire file as a single string.

```Python
content = f.read()
```

- **`readlines()`** – Reads all lines into a list, where each element is one line.

```Python
f.readlines()
```


- **`cloase()`** – Closes the file and releases system resources.

```Python
f.close()
```
**Note:** It is recommended to use the with statement, which automatically closes the file after use:
```Python
with open("data.txt", "r") as f:
    content = f.read()
```

### lab5a.py - Reading data from files
**Objective:** Practice reading data from a text file in Python.  

**Instructions:**
- Create a new file called `data2.txt` in the same directory as your script, and paste the following text into it:  
  ```text
  Hello World, Welcome to File Handling!	
  Line 2
  Line 3
  Line 4
  Line 5
  ```
- Complete the functions in lab5a.py according to the given instructions.
- Run the script from command line.
---

### lab5b.py - Writing Data to Files
**Objective:** Practice reading data from a text file in Python.  
When opening a file for writing, use the `'w'` mode in the `open()` function.  
- Any existing content in the file is deleted immediately when the file is opened.  
- If the file does not exist, it will be created automatically.  
- To write multiple lines, use `\n` to add newlines.


**Instructions:**
- Add the following code to `lab5b.py` to create and write to a file:
```python
f = open('fruits.txt', 'w')
f.write('1. Apples are crunchy.\n2. Oranges are sweet, sour and juicy.\n3. Strawberries are sweet.\n4. Which fruit do you like?')
f.close()
print("File fruits.txt has been created")
```
- Note that we include `\n` in the string to add new lines in the file; otherwise all text appears on one line.
- Run the script from the terminal using the command: `python ./lab5b.py`
- Run the `ls` command to confirm that the file `fruits.txt` has been created.
- Add a print statement to indicate you are reading the file:
```Python
  print("Reading the file fruits.txt ...")
```
- Open the file for reading, read it line by line using a while loop and `readline()` then close the file:
  - Hint: readline() returns an empty string when the end of the file is reached.
- Run the script again to see the output.
- The **output** should look like this:
```yaml 
File fruits.txt has been created
Reading the file fruits.txt ...
1. Apples are crunchy.
2. Oranges are sweet, sour and juicy.
3. Strawberries are sweet.
4. Which fruit do you like?
```
---
### lab5c.py - Reading data from file and process it
**Objective:** Practice reading a file line by line, processing each line, and counting the number of words per line.  

**Instructions:**
- Add the following code to `lab5c.py` to create a text file with a children's rhyme:
```python
with open("rhyme.txt", "w") as dataFile:
    dataFile.write("I made myself a snowball\nAs perfect as could be.\nI thought I'd keep it as a pet\nAnd let it sleep with me.")
```
- Run the script using the command: `python ./lab5c.py`
- Verify with `ls` command that the file `rhyme.txt` now exists with the text content.
- Add code to open `rhyme.txt` in read mode ('r') before processing it.
- Read and process the file line by line:
  - Use a while loop and the `readline()` method.
  - For each line:
    - Remove leading and trailing whitespace using `strip()`.
    - Remove the period at the end of the line using `strip('.')`.
    - Split the line into words using `split()`.
    - Count the number of words using `len()`.
    - Print the line along with the word count in the format: `<line text> --- <number of words> words`
- Close the file after processing all lines to release system resources.
- The **output** should look like this:
```yaml
 I made myself a snowball --- 5 words
 As perfect as could be --- 5 words
 I thought I'd keep it as a pet --- 8 words
 And let it sleep with me --- 6 words
```

## INVESTIGATION 2: ADVANCED FILE OPERATIONS & DATA STRUCTURES

### lab5d.py - Reading data from multiple files and process it
**Objective:** Practice reading and processing lines from two files simultaneously, cleaning the data, and writing formatted output to a new file.  

**Files provided:**  
- `pythonStatements.txt` — contains Python statements with spaces and comments.  
- `machineCode.txt` — contains corresponding 16-digit binary machine code for each Python statement.
The file `pythonStatements.txt` contains four lines and each line contains a line of code form python language. There are some spaces and the comments explaining the line of code.
The file `machineCode.txt` contains four lines of 16 digit binary code. Let's suppose that this binary code is the machine language representation of each python statement in the `pythonStatements.txt` file. The lines in both files correspond to each other, this implies that the Line 1 in `machineCode.txt` is the machine code for line 1 in `pythonStatements.txt`. In the file lab5d.py write script to perform the following tasks.

**Instructions:**
- Ensure that both files (`pythonStatements.txt` and `machineCode.txt`) are in the **same directory** as `lab5d.py`.
- In the file `lab5d.py`, add code to open both files for reading, and create a new file `output.txt` for writing.
- Use a loop to process the lines:
   - Read a line from `pythonStatements.txt` and the corresponding line from `machineCode.txt`.  
   - Remove leading and trailing whitespace from the Python line using `strip()`.  
   - Remove comments from the Python line (anything after `#`).  
   - Write the cleaned Python statement **followed by a tab (`\t`) and the corresponding machine code** to `output.txt`.
- Close all files after processing.
- Run the script from the terminal using the command: `python ./lab5d.py`
- The output in output.txt should look like this:
``` go
print("Hello World")    0000000000010100
x = x + 1    1100110011001100
for i in range(1,n):    1010101010101010
calculateSum(a,b)    1001001001001000
```
---
### lab5e.py – Storing File Data in a Dictionary
**Objective:** Practice reading data from files and storing it in a Python dictionary for easy access and analysis.

**Files Provided**
- `students.txt` — contains student names, one per line.  
- `grades.txt` — contains corresponding grades for each student, one per line (same order as `students.txt`).  

**Instructions**
- Ensure both files are in the **same directory** as `lab5e.py`.
- Open `students.txt` and `grades.txt` for reading.
- Create an **empty dictionary** to store the data:  
   - The **key** will be the student name.  
   - The **value** will be the student’s grade.
- Use a loop to read lines from both files simultaneously:  
   - Remove leading/trailing whitespace from each line using `strip()`.  
   - Add each student and grade to the dictionary.
- After storing all data, **print the dictionary** to verify its contents.
- Perform simple analysis:  
   - Find the **student with the highest grade**.  
   - Calculate the **average grade**.  
   - Print the results.
- Close all files after processing.
- Run the script and verify the output.
- The **output** should look like this:
```Python
# Dictionary after reading files
# Dictionary after reading files
{  'Avery': 88, 'Jordan': 95, 'Riley': 82, 'Taylor': 91, 'Sasha': 77,
   'Amir': 85, 'Priya': 90, 'Kai': 93, 'Lina': 80, 'Diego': 87
}

# analysis
Highest grade: Jordan with 95
Average grade: 86.8
```

## Lab 5 Sign-Off
- Submit a PDF on Blackboard, named using your Seneca username (e.g., **yoursenecausername.pdf**).
- The PDF must include screenshots of the following scripts and their terminal output, clearly showing your GitHub username.
    - lab5a.py
    - lab5b.py
    - lab5c.py
    - lab5d.py
    - lab5e.py
- Ensure the code and output are clearly readable. Screenshots should be high-resolution (minimum 800x600) and not blurry.
- Blurry or unreadable submissions will be returned for redo. Resubmissions will only be graded as **Satisfactory** with a grade of 0, provided the work is satisfactory.

