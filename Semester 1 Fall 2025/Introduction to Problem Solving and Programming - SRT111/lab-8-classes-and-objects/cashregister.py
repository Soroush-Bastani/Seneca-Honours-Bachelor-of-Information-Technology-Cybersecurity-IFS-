#!/usr/bin/env python3
# Author: 
# Date: 
# Purpose: Models a cash register used in supermarkets.
# This class allows adding items, tracking total price and item count,
# and provides an undo() feature to remove the most recently added item.

# TO DO 1: Complete the functions below according to given instructions. 

class CashRegister:
    def __init__(self):
        # Constructor that initializes the item count and total price.
        self._itemCount = 0        
        self._totalPrice = 0.0

        # TODO: add an instance variable that you might need to implement undo() method.  


    def addItem(self, price):
        # Adds an item to the cash register.Updates both total price and item count.
        self._itemCount += 1
        self._totalPrice += price

        # TODO: Keep a record of each added item’s price (for undo feature)

    def getTotal(self):
        # Returns the total price of all items added.
        return self._totalPrice

    def getCount(self):
       # Returns the total number of items added.
        return self._itemCount

    def clear(self):
        # Resets the cash register to its initial state. All totals and item records are cleared.
        self._itemCount = 0
        self._totalPrice = 0.0

    def undo(self):
        # Removes the most recently added item and updates totals.
        # If no items have been added, print a message or do nothing.
      
        # TODO: Complete this method.
        pass
