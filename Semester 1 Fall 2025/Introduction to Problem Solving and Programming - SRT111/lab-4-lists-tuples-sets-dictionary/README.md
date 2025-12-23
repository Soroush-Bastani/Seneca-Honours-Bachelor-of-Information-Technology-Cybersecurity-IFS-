# Lab4
In this lab, you will create ten simple Python scripts. All scripts must be written in GitHub Codespaces. 
In this lab, you will explore three important Python data structures: **lists**, **sets**, and **dictionaries**. These structures are widely used to organize, store, and manage data efficiently. You will begin by working with lists to understand ordered collections and practice modifying their contents. Next, you will learn how sets store unique, unordered elements and how set operations can be applied in problem-solving. Finally, you will work with dictionaries to see how key–value pairs allow fast and efficient data access. By completing this lab, you will gain practical experience in creating, manipulating, and applying these fundamental data structures in Python programs.
# Lab Objectives
- Create and manipulate Python lists, including adding, removing, and modifying elements.
- Apply built-in functions and list methods to perform common list operations.
- Construct sets and use them to store unique, unordered items.
- Compare lists and sets, highlighting differences in ordering and duplication.
- Perform set operations such as union, intersection, and difference.
- Create dictionaries with key–value pairs for efficient data storage.
- Access and update dictionary values using keys.
- Differentiate between index-based access in lists and key-based access in dictionaries.
# Submission Instructions
For each task:
1. **Write the script** in Codespaces.  
2. **Run the script** from the **terminal**.  
3. **Take a screenshot** that clearly shows:  
   - Your **code** in the editor.  
   - The **terminal output**, including your **username** visible in the terminal.  
4. **Insert the screenshot** into a Word document under the heading that matches the task name:  
   - Example: **Lab4a**, **Lab4b**, **Lab4c**, etc.  
5. After completing all tasks, **convert the Word document to PDF**.  Name the PDF file using your **yoursenecausername.pdf**
6. **Submit the PDF file** as your final lab submission on Blackbaord.

## INVESTIGATION 1: USING LISTS

A list in Python is an ordered collection of items that can be of different types. Lists are mutable, meaning you can change their content after creation.
In this Part you will be creating lists and performing basic operations on lists using list methods and built-in functions.
Lists are used to store data elements. Usually lists contain similar kind of data, but python does not restrict you from adding values of different data types in a list.

### lab4a.py - Creating lists and list concatenation
**Objective:** To practice creating Python lists, storing values in them, concatenating multiple lists using the + operator.

**Instructions:**

Lists are constructed with brackets [] and commas separating every element in the list. For example:
```Python
numbers=[1,2,3,4]
mixed_list=[1, "two", 4.5, True]
```
- Open the file Lab4a.py and fill in the required fields in the comment section.
- Create a variable called `mylist1` that stores the first three odd numbers: 1, 3, 5.
- Create a second list called `mylist2` that stores the first three even numbers: 0, 2, 4.
- Create a third list called `mylist` that combines all elements from mylist1 and mylist2.
   - Hint: You can use + to concatenate lists. For example: [1, 2] + [3, 4] results in [1, 2, 3, 4].
- Print the variable `mylist` and check that it contains all six numbers in order.

---
### lab4b.py- Using list methods to add and remove elements from a list 
**Objective:** To practice using common list methods (append(), insert(), pop(), and index()) for modifying and accessing list elements.

**Instructions:**

- Open the file Lab4b.py and fill in the required fields in the comment section.
- Create a variable `mylist` that contains the first 6 natural numbers: [1, 2, 3, 4, 5, 6].  
- Use the `append()` method to add the number 7 to the end of the list.  
- Use the `insert()` method to insert the number 0 at index 0.  
- Use the `pop()` method to remove the element at index 2.  
- Print the variable `mylist`.  
- Add another statement to find the index of the element `6` and print:  
  - The element 6 is present at the index ---`  *(Hint: use the `index()` method).* 

**Expected Output:**
   ```yaml
   mylist: [0, 1, 3, 4, 5, 6, 7]
   message: "The element 6 is present at the index 5"
   ```

---
### lab4c.py- Modifying a list and using the list in a loop
**Objective:** To practice using common list methods (append(), insert(), pop(), and index()) for modifying and accessing list elements.

**Instructions:**
- Open the file Lab4c.py and fill in the required fields in the comment section.
- Create a list variable called `students` and add the following names: Ama, Eden, Maija, Daniel, Ibrahim.  
- Update the element at index 1 to "Maggy".  *Hint:* Remember that list indices start at 0.  
- Use a `for` loop to iterate over the `students` list and print each name on a separate line.  

## INVESTIGATION 2: WORKING WITH SETS

Sets are used to store multiple items in a single variable. Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
A set has similar characteristics as a list, but there are two major differences:
- Sets are un-ordered.
- Sets cannot contain duplicate values.
Set variables are created with curly brackets.

```Python
myset = {"apples", "oranges", "kiwi"}
print(myset)
# Output : {'kiwi', 'apples', 'oranges'}
```

Since new duplicate entries will be automatically ignored when adding elements to a set, they are very useful for performing tasks such as comparisons: finding similarities or differences in multiple sets. 

```Python
myset = {"apples", "oranges", "kiwi", "oranges"}
print(myset)
Output :
{'kiwi', 'apples', 'oranges'}
```
### lab4d.py - Creating Sets
**Objective:** To practice creating sets in Python, filtering elements based on divisibility by a given number.

**Instructions:**

- In your `lab4c.py` file, complete the given function to create the following sets:
   1. `s3` — contains numbers between 0 and 50 that are divisible by 3.  
   2. `s5` — contains numbers between 0 and 50 that are divisible by 5.  
   3. `s7` — contains numbers between 0 and 50 that are divisible by 7.  
   4. `s11` — contains numbers between 0 and 50 that are divisible by 11.  
- Run the script to verify that the sets are created correctly. Note: Sets are unordered, so the printed output may not be in numerical order.

**Expected Output:**
   ```yaml
s3: {0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48}
s5: {0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50}
s7: {0, 7, 14, 21, 28, 35, 42, 49}
s11: {0, 11, 22, 33, 44}
   ```
 ---
### Useful Sets Functions
Set operations in Python are used to perform mathematical set operations like union, intersection, and difference. Python's set data type supports these operations directly. 
The `union` of two sets is a set containing all the elements of both sets without duplicates.

```Python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Using | operator
union_set = set1 | set2
print(union_set)  # Output: {1, 2, 3, 4, 5}

# Using union() method
union_set_method = set1.union(set2)
print(union_set_method)  # Output: {1, 2, 3, 4, 5}
```

The `intersection` of two sets is a set containing only the elements that are common to both sets.

```Python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Using & operator
intersection_set = set1 & set2
print(intersection_set)  # Output: {3}

# Using intersection() method
intersection_set_method = set1.intersection(set2)
print(intersection_set_method)  # Output: {3}
```

The `difference` of two sets is a set containing elements that are in the first set but not in the second set.

```Python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Using - operator
difference_set = set1 - set2
print(difference_set)  # Output: {1, 2}

# Using difference() method
difference_set_method = set1.difference(set2)
print(difference_set_method)  # Output: {1, 2}
```
### lab4e.py - Set Operations
**Objective:** To practice creating a new set from existing sets using the symmetric difference, and to reinforce passing sets as function arguments.

**Instructions:**

- Copy the code from `lab4d.py` and paste it in the file `lab4e.py`.
- Create a new function called `s3_or_s5(s3, s5)` that returns a set containing all elements that are in `s3` or `s5` but not in both.   
   - *Hint:* Use the symmetric difference operator `^` or the `symmetric_difference()` method.
- Remove extra code from `main()` such as the calls to create `s7` and `s11`.
- Call the function `s3_or_s5()` after creating and printing `s3` and `s5`.
- Run the script to verify that the output shows `s3`, `s5`, and then the new set `s3_or_s5`.

**Expected Output:**
   ```yaml
s3: {0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48}
s5: {0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50}
s3_or_s5: {3, 5, 6, 9, 12, 18, 20, 21, 24, 27, 33, 35, 36, 39, 40, 42, 48, 50}
   ```
---
### lab4f.py - Set Operations
**Objective:** To practice combining multiple sets using intersection and difference, passing multiple sets as function arguments, and creating a new set based on specific conditions.

**Instructions:**

- Copy the code from lab4d.py and paste it in your lab4f.py file.
- Create a new function called `s3_and_s5_not_s7(s3, s5, s7)` that returns a set containing all elements that are in both `s3` and `s5` but not in `s7`.
   - *Hint:* Use set intersection and difference methods, e.g., `s3 & s5 - s7` or `s3.intersection(s5).difference(s7)`.  
- Remove extra code from `main()` and call the function at the appropriate location.
- Run the script to verify that the output shows `s3`, `s5`, `s7`, and the final set.
-- **Expected Output:**
```yaml
s3: {0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48}
s5: {0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50}
s7: {0, 7, 14, 21, 28, 35, 42, 49}
s3_and_s5_not_s7: {3, 6, 9, 12, 15, 18, 24, 27, 30, 33, 36, 39, 45, 48}
```

## INVESTIGATION 3: DICTIONARIES

In Python, a dictionary is a collection of key-value pairs. Dictionaries are unordered collections (like sets), but unlike sets, each element is associated with a key. You can retrieve any value efficiently if you know its key.

Think back to lists: list elements are accessed using numeric indexes (0, 1, 2, ...). If you want to find an element in a list, you either already know its index, or you have to search through the list. In contrast, dictionaries allow you to use descriptive keys instead of numeric indexes. Each key maps directly to a value, and that value can be accessed or changed using the key.
Copy the following code in a new file and run it to see the output.
```Python
this_dictionary = {}
this_dictionary["Switzerland"] = "Alps"
this_dictionary["United States"] = "Alaska Range"
this_dictionary["Armenia"] = "Caucasus"
this_dictionary["Argentina"] = "Andes"
this_dictionary["Pakistan"] = "Karakoram"

print(len(this_dictionary))
print(this_dictionary)
print(this_dictionary["Argentina"])

Output:
5
{'Switzerland': 'Alps', 'United States': 'Alaska Range', 'Armenia': 'Caucasus', 'Argentina': 'Andes', 'Pakistan': 'Karakoram'}
Andes
```
Here:
- {} creates an empty dictionary.
- Five key-value pairs are added: "Switzerland" maps to "Alps", "United States" maps to "Alaska Range", and so on.
- len(this_dictionary) prints the number of key-value pairs.
- Printing the dictionary shows all its contents.
- Finally, accessing this_dictionary["Argentina"] retrieves the value "Andes".

### lab4g.py - Working With Dictionaries
**Objective:** Practice creating and returning dictionaries by generating key-value pairs from a range of numbers.

**Instructions:**

- In your lab4g.py file, create a function named `times_ten(start_index: int, end_index: int)` that creates and returns a new dictionary.
- The keys of the dictionary should be the numbers between `start_index` and `end_index` (inclusive).
- Each value should be the key multiplied by ten.
- The function prints the exact output as:
```Python
my_dictionary = times_ten(2, 6)
print(my_dictionary)

{2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
```
- Run the script from command line to verify the output.
---
### lab4h.py - Traversing a Dictionary
**Objective:** Practice traversing dictionaries using keys, values, and key-value pairs, and formatting the output with the .items() method.

The familiar `for item in collection` loop can also be used with dictionaries. By default, looping through a dictionary goes through its keys one by one. Python provides different ways to traverse dictionaries, depending on whether you want to work with keys, values, or key-value pairs.

**Example 1 – Traversing keys**

```Python
student = {
    "name": "John Doe",
    "age": 21,
    "major": "Computer Science"
}

# Traversing keys
for key in student:
    print(key)

# Output :
name
age
major
```
**Example 2 – Traversing values:**  To iterate through all the values in a dictionary, use the values() method.

```Python
student = {
    "name": "John Doe",
    "age": 21,
    "major": "Computer Science"
}

# Traversing values
for value in student.values():
    print(value)

Output :
John Doe
21
Computer Science
```

**Example 3 – Traversing key-value pairs:** To iterate through key-value pairs, use the items() method, which returns a view of the dictionary’s key-value pairs as tuples.

```Python
student = {
    "name": "John Doe",
    "age": 21,
    "major": "Computer Science"
}

# Traversing key-value pairs
for key, value in student.items():
    print(f"Key: {key}, Value: {value}")

Output :
Key: name, Value: John Doe
Key: age, Value: 21
Key: major, Value: Computer Science
```

**Instructions:**
- A dictionary is provided to you in lab4h.py.
- Use a `for ... in` loop with the `.items()` method to traverse this dictionary.
- Print the dictionary’s contents in the exact format shown below:

```Python
Switzerland : Alps
United States : Alaska Range
Armenia : Caucasus
Argentina : Andes
Pakistan : Karakoram
```
- Run the script from command line to verify the output.
---
### lab4i.py - Using Dictionary for Problem solving
**Objective:** Learn how to use dictionaries to count and summarize data from strings by building a simple text-based histogram.
**Instructions:**

- In your lab4i.py file, create a function named histogram that takes a string as its argument.
- The function should count how many times each letter occurs in the string, using a dictionary.
- Then, print a histogram where each letter is followed by stars (*) representing its frequency.
- For example, the function call `histogram("hello amma")` should print:
```Python
h *
e *
l **
o *
a **
m **
```
- Use a dictionary to store the letter counts.
- Call your histogram() function from a main() function and pass it any string of your choice.
- Run the script from the command line to verify the output.
---
## lab4j.py - Using Dictionary for Structured Data

Dictionaries are very useful for structuring related data. For example, we can represent a student’s record with a dictionary:
```Python
student = {"name": "Eden", "id": "eden2402", "semester": 3, "year": 2}
```
We can then create multiple such dictionaries, each representing one student. A list can be used to group these records together, for example:

```Python
student1 = {"name": "Eden", "id": "eden2402", "semester": 3, "year": 2}
student2 = {"name": "Mustafa", "id": "mstfa12", "semester": 4, "year": 2}
student3 = {"name": "Haiden", "id": "haiden1", "semester": 3, "year": 2}

PRG101 = [student1, student2, student3]
```
This way, the list represents the course, and each dictionary in the list represents a student.

**Instructions:**

- In your lab4i.py file, create a function named add_movie() that adds a new movie to a movie database.
- The movie database is a list, and each movie is represented by a dictionary.
- Each dictionary should have the following keys:
   - "name"
   - "director"
   - "year"
   - "runtime"
- The values for these keys should be passed as arguments to the function.
- Call the function four times with different movies.
- In the main() function, print the database so that each movie dictionary appears on a single line.
- Run the script from the command line to verify the output.
- Note that this is a complex task, you are creating a list of dictionaries. It is a really useful concept and if you are able to write this script, you should be proud of you!

## Lab 4 Sign-Off
- Submit a PDF on Blackboard, named using your Seneca username (e.g., **yoursenecausername.pdf**).
- The PDF must include screenshots of the following scripts and their terminal output, clearly showing your GitHub username.
    - lab4a.py
    - lab4b.py
    - lab4c.py
    - lab4d.py
    - lab4e.py
    - lab4f.py
    - lab4g.py
    - lab4h.py
    - lab4i.py
    - lab4j.py
      
- Ensure the code and output are clearly readable. Screenshots should be high-resolution (minimum 800x600) and not blurry.
- Blurry or unreadable submissions will be returned for redo. Resubmissions will only be graded as **Satisfactory** with a grade of 0, provided the work is satisfactory.

