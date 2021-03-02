# -*- coding: utf-8 -*-
"""

Program: Homework Day 8 (classes and methods)
Author: Evan C. Mascitti
Description: Answers to Homework 8 
Last update: 2021-02-17

"""


# problem 2, fruit shopping cart 

# first define a new class called `fruit`. This will be the "base" for later instances of the varios fruits

class fruit:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.number = int(0)
        
        
# define a method to add another of a given
# fruit to the shopping cart 
        
    def add_fruit(self, quantity):
        self.number += quantity
        self.total_cost = self.number*self.price
    
# define another method to compute the total cost of a 
# given fruit type in the current cart

    def compute_total_cost(self):
        print(self.total_cost)
        
        
# banana = fruit(name = 'banana', price = 1.50)

# banana.add_fruit(3)
# banana.compute_total_cost()
# banana.total_cost
    
# banana.add_fruit(7)
# banana.total_cost

# initiate a new instance of the fruit class for each
# of the 3 fruits. 

apple = fruit("apple", 1.15)
orange = fruit("orange", 1.75)
mango = fruit("mango", 2.35)

############################

##  begin interactive portion of program ##

# set a flag to keep the loop going until the 
# user stops it

keep_shopping = "y"


# set the total price as 0; this will be appended later as items are added 

total_price = 0

# start the loop and continue until user wants to stop
# first ask user for number of each fruits to buy,
# then append each fruit object based on the input
# make sure to coerce the input string to an integer type

print("Welcome to the fruit market!")

while keep_shopping == "y": 
    new_apples = int(input("How many apples would you like to purchase? "))
    new_oranges = int(input("How many oranges? ") )
    new_mangoes = int(input("How many mangoes? "))
    # use the add_fruit method to append the number of each fruit in the cart 
    apple.add_fruit(quantity = new_apples)
    orange.add_fruit(new_oranges)
    mango.add_fruit(new_mangoes)
    print("So far, your cart contains", apple.number, "apples, ", \
          orange.number, 'oranges, and ', mango.number, 'mangoes.')
    total_price = sum([apple.total_cost, orange.total_cost, mango.total_cost])
    keep_shopping = input("Would you like to keep shopping? (y/n) ")

# now that the loop has ended print the total and ask for payment
# [I looked up some documentation to format currency with two decimal places 
# regardless of the float precision]

print("\nYour total comes to ", "${:,.2f}".format(total_price), ".", sep = "")
payment = float(input("What is your payment amount? "))

# calculate change as the difference between the payment and cost
change = "${:,.2f}".format(payment - total_price)

# pay user their change and say bye
print(" --------------------------------------------", 
      "\n --------------------------------------------\n\n",
      "Your change comes to ", change, ".", sep = "")


# add extra code to divide change 

restOfChange = payment - total_price

def numCoins(x, rate): 
    return int(x // rate)

dollars = numCoins(restOfChange, 1)
restOfChange = round(restOfChange - dollars * 1, 2)
quarters = numCoins(restOfChange, 0.25)
restOfChange = round(restOfChange - quarters * 0.25, 2)
dimes = numCoins(restOfChange, 0.10)
restOfChange = round(restOfChange - dimes * 0.10, 2)
nickles = numCoins(restOfChange, 0.05)
pennies = int(round(restOfChange - nickles * 0.05, 2) *
100)

print("\nHere are", dollars, "dollars ", quarters, "quarters, ", dimes,
"dimes, ", nickles, "nickles, and ", pennies, "pennies.", 
"\n\nEnjoy your fruit and have a pleasant day!", 
"\n\n --------------------------------------------\n",
"--------------------------------------------")

