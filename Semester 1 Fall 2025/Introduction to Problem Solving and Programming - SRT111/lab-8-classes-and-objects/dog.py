# Add comments before you do anything else.
#--------------------------------
#!/usr/bin/env python3
# Author:
# Date:
# Purpose: class Dog
#--------------------------------

class Dog:
    # __init__ is the constructor. It is automatically called 
    # when an object of this class is created.
    #
    # This constructor defines two instance variables: _name and _breed.
    # These variables are also called attributes.
    #
    # Instance variables belong to each object of the class.
    # Each object gets its own separate copies of these variables.
    
    def __init__(self, dog_name, dog_breed): 
        # 'self' refers to the current object being created.
        # It holds the reference (or address) to that specific object.
        #
        # Using self.variable_name ensures that the variable belongs
        # to this particular object (an instance variable).
        self._name = dog_name   # Assign the value of dog_name to the object's _name attribute
        self._breed = dog_breed # Assign the value of dog_breed to the object's _breed attribute

    def bark(self):
        # each class method can access instance variables.
        return f"{self._name} says woof!"
