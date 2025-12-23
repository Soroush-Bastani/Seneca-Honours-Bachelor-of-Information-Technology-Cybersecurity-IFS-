# Lab 8
In this lab, you will create six Python scripts. All scripts must be written in GitHub Codespaces.<br>

Python is an object-oriented programming language, which means that almost everything you work with — numbers, strings, lists, and even functions — is treated as an object. Objects are created from classes, which serve as blueprints that define the data (attributes) the object stores and the behavior (methods) it can perform.

This lab  is designed to introduce you to the core concepts of object-oriented programming in Python through hands-on activities. You will start by learning how to create simple classes and objects, define attributes and methods, and use the classes by creating class objects.

# Lab Objectives
- Understand what classes and objects are in Python.
- To be able to use a pre-defined class by creating class objects and calling class methods.
- Create and use your own classes.
- Define attributes (variables) and methods (functions) inside a class.
- Understand the instance variables, self parameter, and constructor function.
- Create and manipulate multiple objects from the same class.
  
# Submission Instructions
For each task:
1. **Write the script** in Codespaces.  
2. **Run the script** from the **terminal**.  
3. **Take a screenshot** that clearly shows:  
   - Your **code** in the editor.  
   - The **terminal output**, including your **username** visible in the terminal.  
4. **Insert the screenshot** into a Word document under the heading that matches the task name:  
   - Example: **Lab8a**, **Lab8b**, **Lab8c**, etc.  
5. After completing all tasks, **convert the Word document to PDF**.  Name the PDF file using your **yoursenecausername.pdf**
6. **Submit the PDF file** as your final lab submission on Blackbaord.

  
## INVESTIGATION 1: CREATING A SIMPLE CLASS

In Python, a class is a blueprint for creating objects. It defines a set of attributes (data) and methods (functions) that the objects created from the class will have.
Let’s look at a step-by-step example of how to create a simple class.

**Defining a Class** <br>
A class is defined using the `class` keyword, followed by the class name and a colon:
```Python
class Dog:
    pass
```
The pass statement is a placeholder—it means “do nothing for now,” allowing the class definition to exist without any content yet.

**Adding Attributes**<br>
Attributes are variables that belong to the class.
They are usually defined inside a special method called `__init__()`, which runs automatically when a new object is created.

The self parameter is a reference to the current object being created or used.
- It allows each object to store its own separate data.
- Using self.attribute_name ensures that the attribute belongs to this specific object, not to the class as a whole or to another object.
- Think of self as a way for the object to keep track of its own data.
```Python
class Dog:
    def __init__(self, name, breed):
        self._name = name    # Each dog object has its own name
        self._breed = breed  # Each dog object has its own breed
```
Here self._name and self._breed are instance variables (attributes) belonging to the object.

**Adding Methods**<br>
Methods are functions that belong to a class. They typically perform actions using the object’s data. All class methods have access to the instance variables of the object via self.
```Python
class Dog:
    def __init__(self, name, breed):
        self._name = name
        self._breed = breed

    def bark(self):
        return f"{self._name} says woof!"
```
**Creating and Using an Object**<br>
You can create an object (an instance of the class) by calling the class name like a function, with the required arguments:
```Python
my_dog = Dog("Buddy", "Golden Retriever")
```

You can access an object’s methods or attributes using dot notation:
```Python
print(my_dog.bark())  # Output: Buddy says woof!
```
Let's now do some hands on activities.

### lab8a - Using a class
**Objective:** To create an object from a Python class and call one of its methods.<br>

**Instructions:** 

- Review the code in the file `dog.py`.
  - Understand the Dog class definition and how instance variables are initialized inside the constructor (__init__ method).
- Open the file `dog_tester.py`.
  - Notice that the Dog class has already been imported for you.
- Inside the main() function:
  - Create a new object of the Dog class (for example, my_dog = Dog("Buddy", "Golden Retriever")).
  - Call the bark() method for this object.
- Run the file using the command: `python ./dog_tester.py`.
- Take a clear screenshot of the `main()` from `dog_tester.py` and the output in the terminal.

## lab8b - Implementing a class method and testing the class
**Objective:** To define a method inside a class and test the class from a separate file.<br>

**Instructions:** 

- Open the file `cylinder.py`.
  - A class named Cylinder has already been created for you.
  - Complete the volume() method so that it calculates and returns the volume of the cylinder. (Hint: Volume = π × radius² × height)
- Create a new file called `cylinder_tester.py`
  - Add comments in `cylinder_tester.py` to explain the purpose of this file.
  - Import the Cylinder class using an import statement.
  - Define the `main()` function.
  - Inside `main()`, create an object of the Cylinder class by passing the required arguments (e.g., radius and height).
  - Call the `volume()` method, store the volume in a variable and print it.
- Run the script from command line using the command: `python ./cylinder_tester.py`.
- Take a clear screenshot of `volume()` method, `main()` form `cylinder_tester.py` and the output.


## lab8c - Class CashRegister: Adding instance variable and method in an existing class to extend the functionality
**Objective:** To extend an existing class by adding a new method and modifying instance variables, and to test the class using a separate script.<br>

**Instructions:** 

During our lecture session, we implemented a `CashRegister` that could add items and calculate the total.
Now, suppose the `CashRegister` needs to support an `undo()` method that removes the most recently added item.
This allows a cashier to quickly correct a mistake.

- Open the file `cashregister.py.`
  - Complete the undo function in `cashregister.py`.
    - The `undo()` method should remove the most recently added item and adjust the total accordingly.
    - You need to use an additional instance variable such as a list to store added items.
- Create a new file called `cashregister_tester.py`
  - Add comments in `cashregister_tester.py` to explain the purpose of this file.
- In `cashregister_tester.py`:
  - Import `CashRegister`class.
  - Define the `main()` function.
  - Inside the `main()`:
    - Create an object of the `CashRegister` class.
    - Add a four items using the `addItem()` method.
    - Print the total after adding items.
    - Call the `undo()` method twice to test it.
    - Print the total again to confirm that the last addition(s) were undone.
- Run the script from command line using the command: `python ./cashregister_tester.py`.
- Take a clear screenshot of undo() method, main() from `cashregister_tester.py` and the output.

## lab8d - Managing multiple objects
**Objective:** To work with multiple objects of the same class and perform operations on them.<br>

**Instructions:** 

- Create a new file called `store_tester.py`.
- Import the `CashRegister` class.
- In the `main()`:
  - Create two CashRegister objects, for example register1 and register2.
  - Add a few items to each register using addItem().
  - Print the totals for each register.
- Compare the two totals and print which register collected more money.
- Run the script from command line using the command: `python ./store_tester.py`.
- Take a clear screenshot of main() and the output.

## INVESTIGATION 2 — CLASS VARIABLES AND MODELING A REAL WORLD CLASS

## lab8e - CashRegister: Adding tax functionality
**Objective:** To extend an existing class by adding a class variable and a class method, and calculate total price including tax without modifying the original total.<br>

So far, your `CashRegister` only keeps track of the total price without tax. Now, we want to be able to calculate the total price after applying tax. 
A class variable is shared by all instances of a class, making it perfect for a constant like TAX_RATE. A class method will calculate the total including tax using the class variable.

**Instructions:** 
- Open your previous `cashregister.py` file.
- Add a class variable to the CashRegister class to store the tax rate.
  - Example: TAX_RATE = 0.13 (13% default).
- Remember: this is a class variable, not an instance variable.
- Implement a class method `getTotalWithTax()` that:
  - Accepts self as a parameter.
  - Calculates the total price including tax.
  - Returns the total with tax. Important: Do not update `_totalPrice`. The original total should remain unchanged.
  - Update your tester script (cashregister_tester.py) to:
    - Call the new `getTotalWithTax()` method on your `CashRegister` object.
    - Print both the original total and the total including tax.
- Run the script from command line using the command: `python ./cashregister_tester.py`.
- Take a clear screenshot showing:
  - updated CashRegister class with the new class variable and method.
  - The `main()` function in your tester file.
  - Output displaying total price before and after tax.

## lab8f - CashRegister: Storing items and printing a receipt
**Objective:** To extend the CashRegister class so that it can store item names and individual prices, and print a detailed receipt with totals.<br>

Currently, the `CashRegister` class only keeps a running total of prices and a count of items.
This is not enough to print a proper receipt that shows each item’s name and price.
In this activity, you will re-write the class to store item information individually and modify the methods accordingly.

**Instructions:** 
- Open your previous `cashregister.py` file.
- Update the constructor (__init__) of the CashRegister class.
  - Add instance variable(s) to store item names and their prices.
  - You may choose one of the following approaches:
    - Two parallel lists: one for names, one for prices.
    - A dictionary with item names as keys and prices as values.
    - A list of tuples.
  - Initialize these variable(s) to empty (e.g., empty list or dictionary).
- Update the **addItem()** method:
- Modify it to accept two parameters: itemName and itemPrice.
- Store the item information in the instance variable(s) defined above
- Example for list of tuples:
```Python
self._items.append((itemName, itemPrice))
```
- Update the **getTotal()** and **getCount()** methods (if needed):
  - Ensure that getTotal() calculates the total based on the individual stored prices, rather than relying on a running total.
  - Ensure that getCount() correctly returns the number of items stored.
- Run the script from command line using the command: `python ./cashregister_tester.py`.
- Implement a **printReceipt()** method that prints:
  - Each item’s name and price on a separate line.
  - The total price at the end.
     ``` text
    Apple       2.50
    Bread       3.00
    Milk        4.20
    -----------------
    Total:     9.70
    ```
- Take a clear screenshot showing:
  - Updated CashRegister class with the new instance varaiables and methods.
  - The `main()` function in your tester file.
  - Output displaying the resceipt.
    
## Lab 8 Sign-Off
- Submit a PDF on Blackboard, named using your Seneca username (e.g., yoursenecausername.pdf).
- The PDF must include screenshots of the following scripts and their terminal output, clearly showing your GitHub username.
  - lab8a.py
  - lab8b.py
  - lab8c.py
  - lab8d.py
  - lab8e.py
  - lab8f.py
- Ensure the code and output are clearly readable. Screenshots should be high-resolution (minimum 800x600) and not blurry.
- Blurry or unreadable submissions will be returned for redo. Resubmissions will only be graded as Satisfactory with a grade of 0, provided the work is satisfactory.
