# Lab2
In this lab, you will create **ten simple Python scripts**. All scripts must be written in **GitHub Codespaces**.
This lab focuses on practicing **decision-making** and **iteration** in Python, including:  
- `if` statements  
- `for` loops  
- `while` loops

# Lab Objectives
- Understand and utilize Python's system-level capabilities.
- Develop proficiency in handling user input and validating data
- Apply control flow structures to solve real-world problems
- Master loop constructs for both counter-driven and event-driven tasks
- Implement loop control mechanisms using break and continue
- Recognize and avoid common programming pitfalls
- Document and present code execution results through screenshots and organized submission.
 

# Submission Instructions
For each task:
1. **Write the script** in Codespaces.  
2. **Run the script** from the **terminal**.  
3. **Take a screenshot** that clearly shows:  
   - Your **code** in the editor.  
   - The **terminal output**, including your **username** visible in the terminal.  
4. **Insert the screenshot** into a Word document under the heading that matches the task name:  
   - Example: **Lab2a**, **Lab2b**, **Lab2c**, etc.  
5. After completing all tasks, **convert the Word document to PDF**.  Name the PDF file using your **Seneca username**, for example salim123.pdf
6. **Submit the PDF file** as your final lab submission on Blackbaord.


## INVESTIGATION 1: USING IF-ELSE AND input() FUNCTION
An IF statement is a decision statement that executes or does not execute a section of code based on whether the condition is True or False.
In investigation 1 you will learn how to take input from user, and compare it with other values.

### lab2a.py - Simple if statement
**Objective:** Practice using if statements in Python to make decisions based on user input, including type conversion, relational operators, and Boolean conditions.

**Instructions**
- Open the file lab2a.py and fill in the required fields in the comment section.
- Create a variable named `x` and store a value entered by the user using the `input()` function.  
    - The prompt should clearly ask for a number, for example:  
      ```python
      x = input("Please enter a number: ")
      ```    
    - **Note:** The `input()` function always returns a value of type `str` (string), even if the user types a number.  
- Use the `type()` function to check the type of `x` and print the result. Observe that the type of `x` is `str`.  
- Convert `x` to an integer using the `int()` function and update the variable `x` with this integer value using the statment:
   ```python
    x = int(x)
   ```   
- Write an if-statement to check if `x` is greater than or equal to 6.  
    - If the condition is `True`, print:  
      ```
      x is greater than or equal to 6!
      ```  
- Write another if-statement that uses both relational and Boolean operators to check if `x` is greater than or equal to 4 **and** less than 12.  
    - If this condition is `True`, print an appropriate message informing the user (for example: `"x is between 4 and 11 inclusive"`).  

### lab2b.py - Using if-else statement
**Objective:** Practice decision-making in Python using the `if-else` statement to compare user input with a specific value.
**Instructions: **

- Open the file lab2b.py and fill in the required fields in the comment section.
- Use the input() function and ask the user to enter a 4-digit integer. Save this value in the variable `num`. For example:
  ```python
      num = input("Enter a 4-digit number: ")
  ```
  - Write an `if-else` statement to check if the number is **exactly 1984**:  
  - If `True`, print:  
      ```
      George Orwell
      ```  
  - If `False`, print:  
      ```
      Not quite right!
      ```


### lab2c.py - String comparison
**Objective:** Practice using `if`, `elif`, and `else` statements in Python to compare the length of strings entered by the user.

**Instructions**

- Open the file lab2c.py and fill in the required fields in the comment section.
- Create two variables named `str1` and `str2`.  
- Assign each variable a sentence entered by the user using the `input()` function.  
- Use the `len()` function to determine the length of each string.  
- Use `if`, `elif`, and `else` statements to compare the lengths of `str1` and `str2`:  
  - If `str1` is longer, print:  
    ```python
    str1 is longer than str2!
    ```  
  - If `str2` is longer, print:  
    ```python
    str2 is longer than str1!
    ```  
  - If they are equal in length, print:  
    ```python
    str1 and str2 are of equal length!
    ```

## INVESTIGATION 2: USING COMMAND LINE ARGUMENTS
So far you have been using the `input()` function to get user input. We can also provide input from command line as an argument after your script name on the command line. 
In this section, you will learn how to pass an argument to your Python script, but this time, the argument will be passed when you execute your Python script from the terminal. In fact, your script name is also an argument to Python interpreter. You can provide additional arguments. 

In order to access command line arguments in Python, we will need to use a special Python object called `sys.argv` from the `sys module`. We can use the Python keyword `import` to load the `sys module` so that we can access it in our python script. `sys.argv` is a list object which is used to hold everything given at the command line, including the command itself.

The `sys module` is one of the built-in modules that comes with the Python interpreter. By issuing the import sys statement at the top of a python script, it will load the code written by another person. Each 'library' (or 'module') that gets loaded will give us extra functionality and objects to our python script.

### lab2d.py - Exploring Python's sys Module and Command-Line Arguments
 **Objective:** To explore Python's sys module and understand how command-line arguments are accessed and utilized in scripts.

**Instructions**
- Open the file lab2d.py and fill in the required fields in the comment section.
- Import the sys module.
- Next, add the following lines to your script.
``` Python
print(sys.version) # prints the version of the python currently in use.
print(sys.platform) # prints the name of operating system.
print(sys.argv) # prints the list of all arguments given at the command line when running our python script from terminal.
print(len(sys.argv)) # Displays the number of command-line arguments provided by the user.
```
- Run your script using the command `python ./lab2d.py`
- Observe the output. How many arguments were passed to python this time?  Only one, which is the script name. You will see the path to the script file in the output of  print(sys.argv).
- Add the following lines to your script.
  
```Python
print(sys.argv[0]) # prints the first argument, it is always the name of script.
print(sys.argv[1]) # prints the second argument .
print(sys.argv[2]) # prints the third argument.
print(len(sys.argv)) # tells us the number of command line arguments the user provides from terminal.
```
- Now run the script using the following command: `python ./lab2d.py maija Maija`.
- What do you observe? What did you learn?  This time we provided three arguments. The name of script is the first argument, second argument is maija and third argument is Maija.
- Answer the following questions:
    - What happens if you run the script without any additional arguments?
    - Why is sys.argv[0] always the script name?
    - How could you use command-line arguments in real-world applications?

 
### lab2e.py - Using Command-Line Arguments with Conditional Logic
**Objective:** To practice using command-line arguments in Python and apply conditional logic to process user input.

**Instructions**
- Open lab2e.py and ensure the comment section is completed.
- This script requires exactly two arguments after the script name: a name and an age.
- Create a variable name and assign it sys.argv[1].
- Create a variable age and assign it sys.argv[2].
- Ensure the script checks if exactly two arguments are provided. If not, print an error message and exit.
- The script should use if-else or if-elf or if-elif-else structure and should print the EXACT OUTPUT as shown below.

 **Sample Run 1:**
  ```
   python  ./lab2e.py Maija 20
   output: Hi Maija, you are 20 years old and the script received exactly 2 arguments!
  ```
**Sample Run 2:**
``` 
python ./lab2e.py Maija 20 PRG101
output: Hi Maija, you are 20 years old and the script received 3 arguments.
```  
**Sample Run 3:**
```
python ./lab2e.py Maija 20 PRG101 Seneca
output: Hi Maija, you are 20 years old and the script received 4 arguments.
```  
**Sample Run 4:**
```
python ./lab2e.py
output: The script requires atleast 2 arguments.
```

## INVESTIGATION 3: USING NESTED CONDITIONS
- Using nested conditions are helpfull im multiple situations in python.
- Nested conditions are using statements like if and else multipule times on top of each other.
- These can be used when you have to narrow down specifics or doing more complex conditions.
- In investigation 3 you will learn how to use nested conditions and will practice using them.
- example:
  -  Copy the following code snippet in Jupyter lab and run it to observe its output. You can also copy this code in lab2f.py, run and observe the output and then delete this code form lab2f.py becasue in this file, you will be doing another example.
``` Python
x=3
if x < 6:
    if x >2: # this if is nested in the above if
        print("x is less than 6 and x is greater than 2.")
```

### lab2f.py - Income Tax Calculator with nested conditions
**Objective:** Practice using nested `if`, `elif`, and `else` statements in Python to apply conditional logic based on multiple variables.

![incomeTaxExample](https://github.com/user-attachments/assets/e7325ff1-a90f-445d-b119-06b95cc103c6)

**Instructions:**

- Open lab2f.py and ensure the comment section is completed.
- Create a program that calculates tax based on the table in the image above.
- The script should include a variable `income`. The value of `income` should be entered by the user and should be a number (preferably in the thousands).
- Convert the input to an integer or float so it can be used in numeric comparisons.
- Include a variable `status`, prompt the user to enter either `"single"` or `"married"`.
- Use **nested** `if`, `elif`, and `else` statements to model the logic shown in the tax chart.  
- Use **relational operators** to compare `income` and `status` with the threshold values in the table.  
- Test your program with multiple different combinations of income and marital status to ensure it works correctly.


## INVESTIGATION 4: USING LOOPS
Loops are used in all programming languages to repeat code under certain conditions.  
A loop runs as long as its condition (expression) evaluates to `True`.  
When the condition becomes `False`, the program continues with the next line after the loop.

In Investigation 4, you will learn about the two main types of loops in Python:  
- `while` loop  
- `for` loop  


### Part A: while Loop:
In Python, a `while` loop is used to execute a block of statements repeatedly **while** a given condition is `True`.  
A `while` loop can use the same type of Boolean expressions found in `if` statements.  
While the condition remains `True`, all indented statements in the loop body will run repeatedly.  
When the condition becomes `False`, the loop stops.

**Note:** In Python, all statements indented by the same number of spaces after a control structure are considered part of the same block.

**Syntax:**
```python
while condition:
    statement(s)
```
**Key points:**
- Commonly used when you want to repeat statements until an event occurs (event-controlled loop).
- The loop must have a way to change the condition to avoid running forever.
- An iteration variable is often used in the condition and is updated inside the loop.
  
 ```python
count = 0  # iteration variable
while count != 5:  # condition (evaluates to True or False)
    print(count)   # loop body
    count = count + 1  # update the iteration variable

print('Loop has ended')  # runs after the condition becomes False
```

### lab2g.py - Understanding While Loops in Python
**Objective:** To explore counter-controlled and event-driven while loops in Python and understand common loop-related errors such as the off-by-one error.

**Instructions**
- Fill in the required fields in comment section
- Copy the above code block in lab2g.py.
- Change the value of count to 1 and then run the program to see how many times the loop runs.
- Next change the while condition to `count < 5 ` and then run the program to see how many times the loop runs.
- Next change the condition to `count <= 5` and then run the program to see how many times the loop runs.
- What did you observe in all of the above examples when you change the value of loop variable or the expression. It is important that you are well aware of initial value of loop variable and the condition in the loop expression to know exactly how many times the loop will be executed.
- Search on the internet about "What is off by 1 error in loops"?

Next, we will do a more complex but really useful example.
In Python, we often use while loop to see if the user entered the required value. We keep asking the user for a value until the user enters the correct value. This is a scenario-driven by an event rather than driven by a counter, because you do not know how many times the user will enter the incorrect value before the user enters the correct value. See the example below:

```Python
guess = 5
number = int(input("Guess what number less than 10 I am thinking of?"))
while number != guess:  # loop condition 
  print("incorrect guess, try again...")
  number = int(input("Guess what number less than 10 I am thinking off?")) # keep taking input from user until the user enters the correct guess.
print("You got it right!") # this statement will be executed when loop has terminated which will only happen when the user enters the number 5.

```

### lab2h.py - Validating User Input with a While Loop
**Objective:** To use a while loop to repeatedly prompt the user for a 4-digit PIN until the correct value is entered.

**Instructions:**
- Open lab2h.py and fill in the required fields in the comment section.
- Create a variable called `pin`. Use the `input()` function to ask the user to enter a 4-digit PIN.
- Use a while loop to keep asking for the PIN until the user enters the correct PIN `1234`.
- Add a validation check to ensure the user enters exactly 4 digits and that all characters are numeric.
- Your output should look like this:
```
Please type in your PIN: 0000
Incorrect...try again

Please type in your PIN: 199

Incorrect...enter a 4 digit number

Please type in your PIN: 1234
Correct PIN, You can enter!
```
Keep practicing, attempt this next exercise now!

### lab2i.py - Using break and continue in Loops
**Objective:** To practice using break and continue statements in Python loops to control flow based on user input.

**Instructions:**
- Open lab2i.py and fill in the required fields in the comment section.
- Write a program that repeatedly prompts the user to input a number.
- Based on the input, the program should:
    -  **Negative Number**: Print "Invalid number." and prompt again (use continue).
    -  **Zero**: Print "Exiting ..." and terminate the loop (use break).
    - **Non-Negative Number**: Calculate and print the square root of the number
- **Sample output**: 
``` Python

Please type in a number: 9
3.0

Please type in a number: 1
1.0

Please type in a number: -9
Invalid number.

Please type in a number: 0
Exiting ...
```

### Part B: for Loop:
A for loop is used for iterating over a sequence (that could be either a list, a tuple, a dictionary, a set, or a string).
With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
A very common example of for loop found in all text books is:

``` Python
fruits = ["apple", "banana", "cherry", "date"]

# Use a for loop to iterate over the list
for fruit in fruits:
    print(fruit)
```
for loop is commonly used with range functions. Here's another example using the range function to print numbers from 0  to 5.

``` Python
for i in range(5):
    print(i)
```
The range(5) function generates a sequence of numbers from 0 to 4 (inclusive of 0, exclusive of 5).


### lab2j.py - Summing Even Numbers with a For Loop
**Objective:** To use a for loop and conditional logic to calculate the sum of all even numbers from 1 to 100 (inclusive).

**Instructions**
- Open lab2j.py and fill in the required fields in the comment section.
- Write a Python program that.
   - Uses a for loop to iterate over the numbers from 1 to 100 (inclusive).
   - Checks if each number is even using the modulo operator (%).
   - Adds even numbers to a running total.
   - Prints the final sum after the loop ends.


## Lab 2 Sign-Off
- Submit a PDF named using your Seneca username, **<your-username>.pdf** on *Blackbaord*.
- The document must include screenshots of the following scripts and their terminal output, clearly showing your GitHub username:
    - lab2a.py
    - lab2b.py
    - lab2c.py
    - lab2d.py
    - lab2e.py
    - lab2f.py
    - lab2g.py
    - lab2h.py
    - lab2i.py
    - lab2j.py
- Ensure the code and output are clearly readable. Screenshots should be high-resolution (minimum 800x600) and not blurry.
- Blurry or unreadable submissions will be returned for redo. Resubmissions will only be graded as "**Satisfactory**" with a grade of 0, provided the work is satisfactory. 
