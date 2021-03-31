# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 08:00:51 2021

@author: Evan C Mascitti
"""
#############
# Problem 1

# ask user for input values 

starting_number = int(input("Enter a starting value."))
ending_number = int(input("Enter an ending value."))
even_or_odd = input("even or odd output?")

# construct series of logical statements about what the number sequence should be
if starting_number % 2 == 0 and even_or_odd == "even":
    numbers = range(starting_number, ending_number, 2)
elif starting_number % 2 == 0 and even_or_odd == "odd":
    numbers = range(starting_number, ending_number, 2)
elif starting_number %2 != 0 and even_or_odd == "even":
    numbers = range(starting_number + 1, ending_number, 2)
else: numbers = range(starting_number, ending_number, 2 )

# print each element of the constructed number sequence 
for i in numbers :
  print(i)
  
 ###############
 
 # Problem 2
 
 # first assign the percentage to a variable so it can be referenced later
grade = float(input("What is your grade as a percent (no % symbol)?"))

# use nested logical statements to determine the letter grade,
# moving progressibely from highest to lowest
if grade >= 93:
    letter = "A"
elif grade >= 90:
    letter = "A-"
elif grade >= 87:
    letter = "B+"
elif grade >= 83:
    letter = "B"
elif grade >= 80:
    letter = "B-"
elif grade >= 77:
    letter = "C+"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else: letter = "F"

# print the grade entered by the user and the corresponding letter grade 
print("Final grade percentage: ", grade, "%") 
print(letter)

###################

# Problem 3

# define a range of digits to count and also a range of rows
list1 = range(1, 9+1, 1)
list2 = range(1, 9+1, 1)

# check that the first row prints correctly 
for i in list1:
    print(i, end = " ")

# use two for loops to find all possible combinations of the numbers to multiply against one another
# The `end` argument allows the output to be printed horizontally instead of vertically
for x in list2: 
    for i in list1:
      print(i*x, end = " ")
      
for x in list2: 
    for i in list1:
      print(i*x, sep="\t")

      
# the correct digits are printed....however,
# I am stumped on the formatting, i.e. how to break the line
# after 9 numbers being printed. 

# Some other things I tred : 
# for i in list1: print("i")
# for i in list1: print(i+i)
# for i in list1: print(i+2*i)


# update on 2021-01-28  w/ help from Jason
for x in list2: 
    for i in list1:
      print(i*x, end= "\t")
    print()


##############

# Problem 4

# prime numbers must be greater than 1, so begin the range at 2 and end at 100.
# For each value of this range, check whether it can be divided by any other number in the range
# If it can, stop the loop, but if it can't print the number.            
           
for d in range(2, 100+1, 1):
    for i in range(2, d):
        if (d % i) == 0:
            break 
        else: print(d)

# update on 2021-01-28  w/ help from Jason

# this one works! The first step is to check whether the number is divisible by anything smaller than it....
# then if it is, break the loop but if it isn't, AND the number of iterations is still one less than the 
# number to test, print the number to test

for d in range(2, 100+1, 1):
    for i in range(2, d):
        if (d % i) == 0:
            break
        elif i == d-1:
            print(d)
        
# This seems to work, but it is printing a lot of the numbers multiple times. I guess that is beause 
# it prints the number once for every number by which it is not divisible?? Stumped here. 
    



 