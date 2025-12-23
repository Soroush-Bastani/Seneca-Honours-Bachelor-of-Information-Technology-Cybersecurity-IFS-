## Lab 9
In this lab, you will work on two examples to overload math operators and use "Python’s special functions". You will explore the concept of operator overloading in Python through a series of hands-on activities that build on each other. Starting with a simple ComplexNumber class, you will learn how Python’s special methods (such as __add__, __sub__, and __eq__) allow objects to interact using familiar operators like +, -, and ==. You will then extend these ideas in a Fraction class to perform precise arithmetic with fractions instead of decimals. Finally, you will conclude the workshop with a short reflection to summarize your understanding of object oriented programming.

### Lab Objectives

- To be able to implement operator overloading in python.
- To be able to use special methods in python.
- Reflect on your learning of object oriented programming
  
# Submission Instructions
For each task:
1. **Write the script** in Codespaces. For some of the tasks, you will need to capture more than one screenshots to show all the code.
2. **Run the script** from the **terminal**.  
3. **Take a screenshot** that clearly shows:  
   - Your **code** in the editor.  
   - The **terminal output**, including your **username** visible in the terminal.  
4. **Insert the screenshot** into a Word document under the heading that matches the task name:  
   - Example: **Lab9a**, **Lab9b**, etc.  
5. After completing all tasks, **convert the Word document to PDF**.  Name the PDF file using your **yoursenecausername.pdf**
6. **Submit the PDF file** as your final lab submission on Blackbaord.

## INVESTIGATION 1: PYTHON OPERATOR OVERLOADING
Operator overloading allows you to define how operators behave with objects of your custom classes. This is done by defining special methods in your class. Let’s explore some of these methods in detail.
Let's create a class that represents ComplexNumbers in maths, we will overload the +, -, __str__, and __repr__ methods.
Complex numbers are numbers that have both a real part and an imaginary part. They are usually written in the form ( a + bi ), where ( a ) is the real part and ( b ) is the imaginary part, and ( i ) is the imaginary unit with the property that ( i^2 = -1 ).

**Example of a Complex Number**

Let’s take the complex number ( 3 + 4i ):

    The real part is ( 3 ).
    The imaginary part is ( 4i ).

**Addition of Complex Numbers**

To add two complex numbers, you add their real parts and their imaginary parts separately.

Example: (3 + 4i) + (1 + 2i) = (3 + 1) + (4i + 2i) = 4 + 6i 
Let's see how can we implement this functionality in Python. We will use the special method `__add__()` which is called when the + operation is performed on two class objects.
```Python
class ComplexNumber:
    def __init__(self, real, imag):
        self._real = real
        self._imag = imag

    def __add__(self, other):
        new_real = self._real + other._real
        new_imag = self._imag + other._imag
        return ComplexNumber(new_real, new_imag)

# Example usage
c1 = ComplexNumber(1, 2)
c2 = ComplexNumber(3, 4)
c3 = c1 + c2 # __add__() method is called when this statement executes. c1 is passed to `self` reference and c2 is passed to `other` reference
```

**Printing our class objects**

Let's add a new method to print the objects, so that we can print the complex number objects  in the correct format. Python allows us to use a special `__str__()` Method.
The` __str__()` method defines the behavior of the str() function and the print statement for class objects. But first lets add a simple method called `display()` to print our objects.


```Python
class ComplexNumber:
    def __init__(self, real, imag):
        self._real = real
        self._imag = imag

    def __add__(self, other):
        new_real = self._real + other._real
        new_imag = self._imag + other._imag
        return ComplexNumber(new_real, new_imag)

    def display(self):
        print(f"{self._real} + {self._imag}i")


# Example usage
c1 = ComplexNumber(1, 2)
c1.display() # output: 1 + 2i
  
c2 = ComplexNumber(3, 4)
c2.display() # output: 3 + 4i

c3 = c1 + c2
c3.display() #4 + 6i

```
Wouldn't it be interesting if we could simply pass our object to print() function and expect the same output as above? We can do this by using the special method `__str__()`.
Lets replace our display method with `__str__()` and then use it.

```Python
class ComplexNumber:
    def __init__(self, real, imag):
        self._real = real
        self._imag = imag

    def __add__(self, other):
        new_real = self._real + other._real
        new_imag = self._imag + other._imag
        return ComplexNumber(new_real, new_imag)

    def __str__(self):
        return(f"{self._real} + {self._imag}i")


# Example usage
c1 = ComplexNumber(1, 2)
print(c1) # output: 1 + 2i
  
c2 = ComplexNumber(3, 4)
print(c2) # output: 3 + 4i

c3 = c1 + c2
print(c3) #4 + 6i

```
This is phenomenal. We are no more calling the boring `display` method. We can simply call the `print` function. When Python sees that there is a call to`print` function with an argument as class objects, it checks for the implementation of `__str__` method and will execute the `__str__` method instead. This is cool!.

We have used two special methods so far: `__add__()` and  `__str__()`.
Now it is your turn.

### lab9a - Overload the subtraction operator
**Objective:** Learn how to overload the subtraction operator in Python by implementing the __sub__() special method in a custom class.

**Instructions:**
- Create a new Python file called `complexnumber.py`.
- Copy the code from above class `ComplexNumber` in the file.
- Create a new method called `__sub__(self, other)` inside the class. This method should:
  - take two objects of the class and subtract them.
  - return a new ComplexNumber object whose real and imaginary parts are the difference of the two operands.
  - this is the same as the implementation of `__add__()`. Just subtract instead of addition.
- Create a new file called `complexnumber_tester.py`.
- Import the `ComplexNumber` class and write a `main()` function that:
  - Creates two complex number objects.
  - Subtracts them using the `-` operator.
  - Displays the result using your class’s __str__() method.
- Run the script from command line using the command: Python `./complexnumbers_tester.py`.
- Take a clear screenshot showing:
   - The __sub__() method in `complexnumber.py`.
  - The new equality test code in `main()`.
  - The terminal output.
  
### lab9b - Overload the Equality Operator (__eq__)
**Objective:** Learn how to overload the equality operator `(==)` in Python to compare two objects based on their attribute values..

**Instructions:**
- Open your existing complexnumber.py file.
- Add a new method called `__eq__(self, other)` inside the `ComplexNumber` class.
- This method should:
  - Compare the real parts and imaginary parts of both objects
  - return True if both the real and imaginary parts of the two complex numbers are equal, and False otherwise.
- Inside the `main()` function, add code to test the equality operator.
  ```
  def main():
    c1 = ComplexNumber(3, 4)
    c2 = ComplexNumber(3, 4)
    c3 = ComplexNumber(2, 5)

    print("c1 == c2:", c1 == c2)  # Expected: True
    print("c1 == c3:", c1 == c3)  # Expected: False

  ```
- Run your script from the command line:
- Take a screenshot showing:
  - The __eq__() method in `complexnumber.py`.
  - The new equality test code in `main()`.
  - The terminal output.

## INVESTIGATION 2: UNDERSTANDING AND USING THE GIVEN FRACTION CLASS.
In this lab, you are provided with a Fraction class that demonstrates how Python’s special methods can be used to overload basic mathematical operators.
The purpose of this class is to represent and manipulate fractions as exact rational numbers, rather than converting them to decimal values that can lose precision.

Some of the special methods in the Fraction class have already been implemented for you. Your task is to carefully study the completed methods to understand how operator overloading works and then complete the remaining methods according to the given comments.

### lab9c - Complete the methods in fraction class
**Objective:** Strengthen your understanding of operator overloading by completing missing special methods in a Fraction class that supports arithmetic and comparison operations.

**Instructions:**
- Open the provided file `fraction.py.`
- This file contains a partially completed `Fraction` class that uses Python’s special methods to overload basic math and comparison operations (such as addition, subtraction, multiplication, etc.).
- Carefully read the methods that are already implemented. Understand how they work before modifying or adding new ones.
- Complete the remaining methods as directed by the comments in the `fraction.py` file.
   - (Each incomplete method will have a comment explaining what needs to be done.)
- Create a new file called `fraction_tester.py`.
- Import `fraction` class in your tester file.
- Write a  `main()` that:
   - Creates two Fraction objects (e.g., f1 = Fraction(1, 2) and f2 = Fraction(3, 4))
   - Demonstrates the use of all methods from the Fraction class, including those you completed.
- Take clear screenshots showing:
   - The methods you completed in fraction.py
   - The test code in fraction_tester.py
   - The output in the terminal
   - Label and organize your screenshots properly.


## INVESTIGATION 3: REFLECTION
Over the past three weeks, we have covered several key concepts in Python, including classes, objects, encapsulation, instance variables, calling methods, and operator overloading. Reflect on what you have learned so far and explain your understanding of each of these concepts. Additionally, share your thoughts on how you feel about these topics and how they have impacted your interest in Python programming.

### lab9d - Reflection and Summary
**Objective:** Reflect on the key Python concepts you have learned over the past three weeks and explain how they have contributed to your understanding of object-oriented programming.

**Instructions:**
- Write a short reflection (about 150–250 words) in which you:
   - Explain your understanding of each of these concepts in your own words.
   - Describe how they connect to one another (for example, how objects use instance variables or how operator overloading fits into classes).
   - Share your personal thoughts on learning these topics — for instance, which concepts you found most interesting or challenging, and how they have influenced your view of Python programming.
- This reflection must be submitted as part of your Lab 9 work.
- You may write it directly in a text or Word document and include it in your lab report PDF. This should be your own reflection, AI generated responses will be graded as zero.
- 
## Lab 9 Sign-Off
- Submit a PDF on Blackboard, named using your Seneca username (e.g., **yoursenecausername.pdf**).
- The PDF must include screenshots of the following scripts and their terminal output, clearly showing your GitHub username.
    - lab9a.py
    - lab9b.py
    - lab9c.py
    - lab9d.py
     
- Ensure the code and output are clearly readable. Screenshots should be high-resolution (minimum 800x600) and not blurry.
- Blurry or unreadable submissions will be returned for redo. Resubmissions will only be graded as **Satisfactory** with a grade of 0, provided the work is satisfactory.




