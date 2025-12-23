# Lab 10
In this lab, you will work on a complete example of using Python classes by implementing inheritance. All scripts must be created and executed in GitHub Codespaces.

# Lab Objectives
- To understand the concepts of inheritance, superclass, subclass, and polymorphism.
- To implement inheritance in Python and explore how a child class can use and extend the functionality of a parent class.
- To understand how constructor (__init__()) methods work and to explore their role in inheritance

# Submission Instructions
For each task:
1. **Write the script** in Codespaces.  
2. **Run the script** from the **terminal**.  
3. **Take a screenshot** that clearly shows:  
   - Your **code** in the editor.  
   - The **terminal output**, including your **username** visible in the terminal.  
4. **Insert the screenshot** into a Word document under the heading that matches the task name:  
   - Example: **Lab10a**, **Lab10b**, **Lab10c**, etc.  
5. After completing all tasks, **convert the Word document to PDF**.  Name the PDF file using your **yoursenecausername.pdf**
6. **Submit the PDF file** as your final lab submission on Blackbaord.

## INVESTIGATION 1: INHERITANCE

Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a class to inherit attributes and methods from another class. This promotes code reuse, extending functionality and can make complex systems easier to manage.
A superclass (also known as a parent class or base class) is a class that is inherited by another class. A subclass (also known as a child class or derived class) is a class that inherits from a superclass. Constructors `__init__()`  methods are special methods in Python used to initialize objects when they are created. In inheritance, the child class can call the parent's constructor to initialize attributes from the parent class.

In this example, Animal is the superclass, and Dog is the subclass. In a subclass, you can call the constructor of the superclass to initialize the inherited attributes. This is done using the super() function. The Dog class inherits the name attribute and speak method from Animal but overrides the speak method to provide a specific implementation.


```Python
# Superclass
class Animal:
    def __init__(self, name):
        self._name = name
    def speak(self):
        return f"{self._name} makes a sound."

# Subclass
class Dog(Animal): # To inherit from a parent class, a child class must pass the name of parent class
# as a function argument in class definition.
    def __init__(self, name, breed):
        # Call the superclass constructor
        super().__init__(name)
        self._breed = breed
   def speak(self):
        return f"{self._name} barks."
    
   def display_info(self):
        return f"{self._name} is a {self._breed}."

# Creating an object of the subclass
dog = Dog("Buddy", "Golden Retriever")
print(dog.display_info())  # Output: Buddy is a Golden Retriever.
```

### lab10a: Implementing a Simple Inheritance Structure with Person and Student
**Objective:** Understand how inheritance works in Python by creating a parent class (Person), a child class (Student), and a tester file.<br>
**Instructions:**
- **Create the `Person` class**
  - The file `person.py` is provided.
  - Create a class called `Person` (this is the parent class).
  - Add the following attributes:
    - `name`
    -  `age`
  - Write a constructor `__init__(self, name, age)` to initialize these attibutes with the parameters passed.
  - Create a method `display_info()` to print the name and age of the person.

- **Create the `Student` class**
  - The file `student.py` is provided.
  - Create a class called `Student` (this is the child class) that inherits from `Person`.
  - Add an additional attribute `student_id`.
  - Write the constructor `__init__(self, name, age, student_id)`
    - Use `super().__init__(name, age)` to call the parent constructor.
    - Then initialize the `student_id` attribute.
  - Create a method called `display_student_info(self)` to print the name, age, and student ID of the student.
- **Test your classes**
  - The file `person_student_tester.py` is provided.
  - Write a main function.
     - Inside main create an object `person1` of the `Person` class with the name "Taylor Alison" and age 35.
     - Call `display_info()` for this object.
     - Create an object `student1` of the `Student` class with the name "Moosa", age 20, and student ID "S12345".
     - Call `display_student_info()` for this object.
  - Run the code and make sure output displays correctly.
- **Screenshots to Include**
   - Take a screenshot of `main()`, also capturing the output at this point. Name the screenshot as `lab10a_output.png`. Add this screenshot in the pdf.
   - Screenshot of the entire `Person class`  named as `lab10a_Person.png`
   - Screenshot of the entire `Student class`  named as `lab10a_Student.png`


### lab10b: 
**Objective:** Use the same classes created in lab10a and extend your understanding of inheritance by calling parent methods from a child class and using super().<br>
**Instructions:**
- You will not create any new `.py` files in this task.
- You will only:
   - Add new code inside `main()` in `person_student_tester.py`
   - Make a small modification inside `Student class`.
- **Call display_info() on a Student Object**
   - In the `main()` after creating the `Student` object in lab10a, do the following:
     ``` Python
     student1.display_info()
     ```
    - What you should observe?
       - `display_info()` belongs to `Person`, not `Student`.
       - But Student inherits from Person, so it can still call it.
   - Take a screenshot showing:
      - the updated main() function, and
      - the output produced when calling `display_info()` on the `Student` object.
      - screenshot name: `lab10b_output.png`. Add it to the PDF
- **Modify Student.display_student_info() to Use super()**
   - In `student.py`, modify the `display_student_info()` method so that:
      - It first calls the parent class method `display_info()` using `super()`.
      - Then it prints the student_id
        ```
        def display_student_info(self):
          super().display_info()    # calls Person method
          print(f"Student ID: {self.student_id}")
        ```
     - Why is super() useful? Write a short explanation in a comment inside `student.py`.
- **Screenshots to Include**:
  - the `Person` class named as `lab10b_Person.png`
  - the `Student` class named as `lab10b_Student.png`

## INVESTIGATION 2: METHOD OVERRIDING

Method overriding allows a subclass to replace a method inherited from its superclass by defining a new version with the same name and parameters.
When the overridden method is called on a child-class object, Python uses the child’s version instead of the parent’s.

### lab10c: Overriding a Method in the Student Class
**Objective:** Understand how Python decides which version of a method to call when both parent and child classes define a method with the same name.<br>
**Instructions:**
- In `Student.py` add a new `display_info()` inside the `Student` class.
- This method overrides the version of `display_info()` that is inherited from the `Person` class.
- Inside the new `display_info()` method, Print **only the student ID**.
- In the `main()` inside `person_student_tester.py`, call `display_info()` on your existing Student object like this:
  ```Python
     student1.display_info()
  ```
  - Inside the tester file, write a comment explaining:
     - What changed after overriding?
     - Why the Person version is no longer used?
     - What output is produced now?
- **Screenshots to Include**:
  - Screenshot of the updated Student class (including your overridden display_info() method and explanation comments) named as `lab10c_Student.png`
  - Screenshot of the main() function and the output showing the overridden method being called named as `lab10c_tester_output.png`.


### lab10d: Extending an Overridden Method Using `super()` 
**Objective:**  Learn how to extend the functionality of an inherited method by calling the parent class version of a method using `super()` and then adding child-specific behavior. <br>
**Instructions:**

- In the `Student` class, modify the existing `display_info()` method so that it first prints the `name` and `age` attributes using the parent class method:
  ```python
     super().display_info()
  ```
- This calls the `display_info()` method from the Person class.
- After that, print the student_id so the method now displays:
   - name
   - age
   - student ID
- You can now delete the display_student_info() method from the Student class. This method is no longer needed because the overridden display_info() method now handles all the required output.
- **Screenshots to Include**
   - Screenshot of the updated display_info() method inside the Student class. Filename: lab10d_displayinfo.png
   - Screenshot showing the output in the terminal after calling display_info() on the Student object. Filename: lab10d_tester_output.png

## Lab 10 Sign-Off
- Submit a PDF on Blackboard, named using your Seneca username (e.g., yoursenecausername.pdf).
- The PDF must include screenshots of the following scripts and their terminal output, clearly showing your GitHub username.
    - lab10a
    - lab10b
    - lab10c
    - lab10d
- Ensure the code and output are clearly readable. Screenshots should be high-resolution (minimum 800x600) and not blurry.
- Blurry or unreadable submissions will be returned for redo. Resubmissions will only be graded as Satisfactory with a grade of 0, provided the work is satisfactory.
