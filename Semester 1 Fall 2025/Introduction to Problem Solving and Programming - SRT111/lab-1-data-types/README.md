# Lab1
In this lab you will create five simple scripts. Write the scripts in codespaces. This lab requires students to create and execute simple python scripts which require creating and initializing variables, dynamic typing, using string methods, print() function, and simple arithmetic operations.

# Lab Objectives
- Create and execute basic Python scripts using GitHub Codespaces.
- Declare and initialize variables with different data types (e.g., strings, integers, floats).
- Use built-in functions such as print(), type(), and input() to interact with the user and inspect data.
- Apply string methods like .upper() and .format() for text manipulation and output formatting.
- Perform arithmetic operations including addition, subtraction, multiplication, division, exponentiation, and modulus.
- Use the math module to access mathematical constants and functions.
- Understand and apply indexing and slicing to extract specific characters or substrings from a string.
- Format numerical output using the % operator for alignment and precision control.
- Observe Python’s dynamic typing behavior by reassigning variables and inspecting their types.
- Document and present code execution results through screenshots and organized submission.


## Lab1a.py - Variables, Dynamic Typing
**Objective**: To understand how Python handles variable assignment and dynamic typing.

**Instructions:**

- Open the file lab1a.py.
-  Add the following comments at the top of your script:
```python 
# Author: [Your Name]
# Script Name: lab1a.py
# Description: Demonstrates basic variable usage, string manipulation, and type checking in Python.
```
- Create a variable called `message` and assign it a string value "Welcome to SRT111". Print the variable.
- Use the builtin `type()` function and print the type of this variable.
- Concatenate the variable `message` with another string and print the result, use the `+` for concatenation.
- Create another variable called `x` and assign it the value 10.
- Check its type using `type()` function.
- In the next statement reassign x to the value "hello" and print its type again.
- What did you observe?  Write your observation in comments.
- Run the script from the terminal.
- Take a screenshot showing:
  - Your code
  - Terminal output. This should show your username in the terminal.
- Add this screenshot in a word document under the heading "**Lab1a**". Later you will convert this word document as a pdf and submit it.


## Lab1b.py - User Input & Arithmetic Operations
**Objective**: Practice using the input() function, type conversion, and basic arithmetic operations in Python.

**Instructions:**
- Open the file lab1b.py. Fill in the required fields in the comment section.
- The script should incorporate a variable called `num1` and take its value from user using input() function.
- The script should have another variable named `num2`. The value of `num2` should also be taken from user.
- Convert the variables to float using the `float()` function.
- Perform all the basic arithmatic operations on these two variables and print the output in the following format.
  ```Python
  num1 + num2 = ....
  num1 - num2 = ....
  num1 * num2 = ....
  num1 ** num2 = ....
  num1 / num2 = ....
  num1 // num2 = ....
  num1 % num2 = ....
  ```
- Run the script from the terminal.
- Take a screenshot showing:
  - Your code
  - Terminal output. This should show your username in the terminal.
- Add this screenshot in a word document under the heading "**Lab1b**". 

  

## Lab1c.py — Using the math Module to Calculate
**Objective:** Learn how to import Python modules, take user input, perform type conversion, and use mathematical constants and formulas.
**Instructions**
- Open the file lab1c.py. Fill in the required fields in the comment section.
- Import `math` module.
- The script should include a variable `r`.
- The value of `r` should be a number inputted from the user.
- Convert `r` to an float with `float()` function.
- Using the constant `pi` from `math` module and compute the area of a circle based on `r` being radius.
- Then print the area to the user with the print function.
- Run the script from the terminal.
- Take a screenshot showing:
  - Your code
  - Terminal output. This should show your username in the terminal.
- Add this screenshot in a word document under the heading "**Lab1c**". 

## Lab1d.py — Strings, Indexing, and Formatting
**Objective:** Practice working with strings, string methods, indexing, and formatted output in Python
**Instructions:** 

- Open the file lab1d.py. Fill in the required fields in the comment section.
-	The script should include a variable called `name`.
-	Create a variable called `name` and assign it your name.
-	Use the string method `.upper()` to convert the name to upper case and print it.
-	Create a variable called `age` and assign it your age:
-	Print a birthday message using the .format() method. The message should be: "How are you yourname? Happy xxth birthday!" USe the following statement.
  ``` python
print("How are you {}? Happy {}th birthday!".format(name, age))
```
-	Next create a variable `words`.	The value of `words` should be "The quick brown fox jumps over the lazy dog".
- Using indexing return the first and 17th characters with print function.
- Use negative indexing to extract and print the words "jumps" and "quick":
- Print all charecturs in between index 2-15
- Print "uick brown fox ju" from `words`.
- Run the script from the terminal.
- Take a screenshot showing:
  - Your code
  - Terminal output. This should show your username in the terminal.
- Add this screenshot in a word document under the heading "**Lab1d**". 


## Lab1e.py - Decimal Numbers & String Formatting
**Objective:** Practice working with decimal numbers and formatting output using the % operator in Python.
**Instructions:** 

- Open the file lab1e.py. Fill in the required fields in the comment section.
- Create a variable called `quantity` and assign it a decimal value of your choice.
- Prompt the user to enter a decimal value for a variable called `stock`.
- Print the product of `quantity` and `stock` with 4 spaces before the answer using the % formatting.
- Print the product of `quantity` and `stock` with 7 spaces before the answer and make sure the answer only goes to hundredths using the module % formatting.
- - Run the script from the terminal.
- Take a screenshot showing:
  - Your code
  - Terminal output. This should show your username in the terminal.
- Add this screenshot in a word document under the heading "**Lab1e**". 





## Lab 1 Sign-Off
- Submit a PDF named using your Seneca username, like: jdoe_lab1.pdf on Blackbaord.
- The document must include screenshots of the following scripts and their terminal output, clearly showing your GitHub username:
  - lab1a.py
  - lab1b.py
  - lab1c.py
  - lab1d.py
  - lab1e.py
- Ensure the code and output are clearly readable. Screenshots should be high-resolution (minimum 800x600) and not blurry.
- Blurry or unreadable submissions will be returned for redo. Resubmissions will be only graded as "Satisfactory" with a grade of 0, provided the work is satisfactory. 
