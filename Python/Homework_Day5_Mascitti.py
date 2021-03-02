# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 18:45:28 2021

@author: evanm
"""

#############################################################################

# Problem 1: string encoding and decoding 

# First take the user input and store as a variable 

original_word = input("Input a single word: ")

# randomly select the spacing for the random letters
import random
spacing = random.randrange(1, 4+1, 1)

# randomly select the letter that will be inserted 
import string 
random_letter = random.choice(string.ascii_lowercase)

# now create a list containing the original word divided into a number 
# of pieces
# letters, and the spacing number tacked onto the end 

empty_string = []
for i in range(1, len(original_word)+1, spacing):
  empty_string.append([empty_string + random_letter])    

# print the divided string plus the random letter inserted after each piece 
print(empty_string)

# I'm stumped on this one.....I can't figure out how to paste the split-up
# word and the random letters interspersed between them. 

#############################################################################

# Problem 2 , DNA Sequences 

dna ="ttcacctatgaatggactgtccccaaagaagtaggacccactaatgcagatcctgtgtgtctagctaagatgtattattctgctgtggatcccactaaagatatattcactgggcttattgggccaatgaaaatatgcaagaaaggaagtttacatgcaaatgggagacagaaagatgtagacaaggaattctatttgtttcctacagtatttgatgagaatgagagtttactcctggaagataatattagaatgtttacaactgcacctgatcaggtggataaggaagatgaagactttcaggaatctaataaaatgcactccatgaatggattcatgtatgggaatcagccgggtctcactatgtgcaaaggagattcggtcgtgtggtacttattcagcgccggaaatgaggccgatgtacatggaatatacttttcaggaaacacatatctgtggagaggagaacggagagacacagcaaacctcttccctcaaacaagtcttacgctccacatgtggcctgacacagaggggacttttaatgttgaatgccttacaactgatcattacacaggcggcatgaagcaaaaatatactgtgaaccaatgcaggcggcagtctgaggattccaccttctacctgggagagaggacatactatatcgcagcagtggaggtggaatgggattattccccacaaagggagtgggattaggagctgcatcatttacaagagcagaatgtttcaaatgcatttttagataagggagagttttacataggctcaaagtacaagaaagttgtgtatcggcagtatactgatagcacattccgtgttccagtggagagaaaagctgaagaagaacatctgggaattctaggtccacaacttcatgcagatgttggagacaaagtcaaaattatctttaaaaacatggccacaaggccctactcaatacatgcccatggggtacaaacagagagttctacagttactccaacattaccaggtaaactctcacttacgtatggaaaatcccagaaagatctggagctggaacagaggattctgcttgtattccatgggcttattattcaactgtggatcaagttaaggacctctacagtggattaattggccccctgattgtttgtcgaagaccttacttgaaagtattcaatcccagaaggaagctggaatttgcccttctgtttctagtttttgatgagaatgaatcttggtacttagatgacaacatcaaaacatactctgatcaccccgagaaagtaaacaaagatgatgaggaattcatagaaagcaataaaatgcatgctattaatggaagaatgtttggaaacct"


# Part 1: 
# count instances of 'gagg'
part_1_string = "gagg"
print("There are", dna.count(part_1_string), "occurrences of", part_1_string, ".")
# There are 8 instances 

# Part2: position of first instance of 'atta'
part_2_string = 'atta'
print("The starting position of the first 'atta' is", dna.find(part_2_string), ".")
# The reported start position is 73; since Python starts at 0 the positions of 
# these 4 characters are 72 to 75

# Part 3: sequence length

print("The sequence is", len(dna), "base pairs long.")
# It's 1,363 characters long

# Part 4: total instances of G or C

# make a list of the two numbers corresponding to the g instances and the c 
# instances. Then use the sum function to add them together and divide by the 
# total number of characters
print('The GC content is ', round(100*sum([dna.count("g"), dna.count("c")])/len(dna), 3), "%")


#############################################################################


# Problem 3, pig latin

# take user inputted word 
word = input("What word would you like to translate into pig latin? ")

# assign the first letter to a variable so it can be tacked onto the end of the word 
first_letter = word[0]

# save the word less its first letter to be pasted into the string 

truncated_word = word[1:]

#print concatenated result
print("Your translation is", truncated_word.capitalize(), first_letter.lower(), "ay", sep="")

