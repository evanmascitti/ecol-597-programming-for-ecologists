# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 09:13:26 2021

@author: evanm
"""
##############################################################################

## Problem 1  - Regular expression practice

import re

# Part (a)  
# some attempts that don't work
str = "Jason Keagy <keagy@psu.edu>"

# Match something that is NOT a <, then NOT a white space, then any number 
# of characters, then an @, then any number of characters,
# then NOT a >
match = re.search(pattern=r"[^<][^\s].*@.*[^>].*",  string=str)
print(match)
# doesn't work because it matches right at the beginning of the string

# Match a word character, then anything that isn't a space,
# then any number of characters, then an @, then any number of characters
match = re.search(pattern=r"\w[^\s].*@.*",  string=str)
print(match)
# doesn't work because it still matches the whole string, i.e. not exclusive 
# enough


# This one works: 
    
# Match 1 or more lowercase letters, 
# then the @, then anything that isn't a > repeated 
# one or more times

match = re.search(pattern=r"[a-z]+@[^>]+", string=str)
print(match)


# It works !! This is pretty fragile though because if 
# a person's e-mail starts with a capital letter or a number it 
# won't work. However this does satisfy the question in this 
# particular case. 


# Part (b)

str= "The date is 02-04-21"

# A couple things I tried that don't work 

# find anything that's not a space repeated two times ?
match = re.search("[^\s]{2}", string = str)
print(match)
# doesn't work becase it matches letters also

# find a sequence between two dashes ?
match = re.search("-\d{2}-", string = str)
print(match)
# this almost works but the dashes are still included 
# maybe could get rid of the dashes with string functions ?

match.replace("-", "")
# nope, the object types don't match 

# There's a function from the re module that will do 
# the substitution. But this won't work either because the match object 
# can't be coerced to a string.

date_without_dashes = re.sub("-", "", match)
print(date_without_dashes)

# Finally, this one is a little clumsy but it works :
# look for something that is not a letter, space, or dash
# repeated two times 

match = re.search("[^a-z-\s]{2}", string = str)
print(match)


# Part (c)

# use a built-in string counting function in Python to count 
# number of instances
str = "We use a state-of-the-art method, magnetic resonance imaging, to get accurate volumetric data for 2 sensory processing regions, the olfactory bulbs and optic tecta. We found a tight correlation between ecology and the size of these brain regions relative to total brain size in 2 lakes with intact species pairs."
n_brain = str.count("brain")
print("The word 'brain' appears", n_brain, "times.")


# Part (d)

# use the square brackets to indicate the string 
# should be split at a literal `.` or a comma
# It will return a list of strings. The `.` does not need to be escaped 
# in this case because it is inside a set.
print(re.split(pattern = "[.,]", string = str))

# Part (e)

# use the re module and indicate the pattern should be exactly
# 5 characters long and contain only lowercase or capital letters
# which are enclosed by a space on both ends. Replace the removed word 
# with a space so the other words are not squished together.

# This works fine except when there are two 5-letter words adjacent to one 
# another, because the spaces overlap. 
less_5_letter_words = re.sub(pattern = "\s([a-z]{5})\s", repl = " ", string = str)
print("Here is the passage with all 5-letter words removed:", less_5_letter_words)

# I can't just search for letters with a space on a single end, because this 
# would allow longer words to match the pattern and they would just be 
# truncated. 

print(re.findall(pattern = "r\s[a-z]{5}\s", string=str))

# By using the \b metacharacter the maybe spaces sandwiching the word can be
# eliminated 
less_5_letter_words = re.sub(pattern = "r\b[A-Za-z]{5}\b", repl = " ", string = str)
print("Here is the passage with all 5-letter words removed:", less_5_letter_words)
#  No this doesn't work either; apparently it is not understanding the \b 


# This one works:
    
# Use "lookarounds" to specify that I want to look for, but not select, the spaces 
# at the beginning and end of each word .

# The syntax for lookaheads is different from that of a lookbehind. Both are positive 
# in this example so they check if the sequence of 5 letters (either lowercase or capital)
#  is preceded by a space or a dash and whether it 
# is followed by either a literal period, a space, or a dash. 
print(re.sub(pattern = "(?<=\s|-)[A-Za-z]{5}(?=\.|\s|-)", string = str, repl = " "))

# Just to make sure it is working correctly, use the same regex with a 
# different function from the re module to print all the 5-letter words that 
# are found in the sequence:

print(re.findall(pattern = "(?<=\s|-)[A-Za-z]{5}(?=\.|\s|-)", string = str))

##############################################################################

## Problem 2, pseudocode 

# pseudocode for gene expression example: 

# input <datafile1>
# def data_compile (file_path)
#     header = clip header from <datafile1>
#     new_vars = <var1, var2, var3, ....> # parse header into new variables
#     data =  # make a data frame from the data in <file_path>
#     data_w_header_info = # tack the <new_vars> onto the end of <data>

# whole_dataset = for i in <data_directory>:
#     data_compile(file_path = i)

# output whole_dataset # write new/combined data frame to a permanent file


# some more English-type reasoning:
    
# First, figure out how to solve this problem for a single file. 
# Once it is working, it can be easily iterated by writing it as a 
# function or a `for` loop.

# Steps to solve the problem for a single file: 

# 1.   figure out what delimiter is used to separate the headers from the data 
#      and how the header itself is structured
# 2.   extract only the header and save it as a new variable 
# 3 a. parse the header into multiple strings and save each individual one 
#      as a new variable in the global environment (using builit-in string 
#      functions or regular expressions) 
# 3 b. convert the data into a "longer" format, where there is a new column 
#      for each variable. Within a given column, every cell should have the 
#      same value because this corresponds to the informatin in the header. 
#      Now every observation is uniquely identified and also contains the 
#      metadata from the header. 


# Once this is working for a single file, use a `for` loop to repeat this 
# action for every .csv file in the directory of interest. 

# Save the results to a new list. All the column names should be identical 
# for each file. 

# Output the list as a .csv file containing the complete  data set. 





##############################################################################

## Problem 3, Debugging 

num = int(input("Please give a number: "))
total = 1
for i in range(num, 1, -1):
    total *= i
    print(num, "! is: ", total, sep = "")


# Hmmmmm.....this code will not run for me.  I tried re-typing 
# it manually instead of copy-paste, but without success. 
# I am getting the `unexpected EOF while parsing` error, 
# with a carat pointing to the end of the `for` loop line.
# Not sure if this is an indentation problem or what but 
# I can't get anything to happen and have to move on to something 
# else. I should have started earlier so I could have asked for help. 
# Sorry!

# However, here is what I assume the table  _should _  look like:
    
 #   | step | i | num | total | note             |
 #   | 6    | 5 |  5  |   25  |  multiply 5*5    |
 #   | 7    | 4 |  5  |   100 |  multiply 25*4   |
 #   | 8    | 3 |  5  |   300 |  multiply 100*3  |
 #   | 9    | 2 |  5  |   600 |  multiply 300*2  |
 #   | 10   | 2 |  5  |   600 |  prints answer   |
  
# I think the loop should stop once i reaches 2 because the end of 
# the range call is exclusive.

