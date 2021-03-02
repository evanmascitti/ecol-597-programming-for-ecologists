"""
Program: Homework Day 2
Author: Evan Mascitti
Last Update: 2021-01-25
Description: Answers to the homework assignment for Day 2.
"""

# Problem 2: Mad Libs

# ask user for 5 words in succession, then print the result
mad_lib_output = print("Last " + input("Please supply a day of the week") + " I went to " + input("Please supply a place") +
". I was really hoping to " + input("Please supply a verb") + " a " + input("Please supply a noun") +
 ", but all I found was " + input("Please supply a noun") + ".")

#############################################################


"""
 Problem 3: Tip calculator
"""

# ask user for input 
meal_subtotal = float(input("What is the subtotal for your meal?"))

# PA sales tax is a flat rate of 6% across all counties, see https://www.revenue.pa.gov/GeneralTaxInformation/Tax%20Types%20and%20Information/SUT/Pages/default.aspx#:~:text=The%20Pennsylvania%20sales%20tax%20rate,to%20purchases%20made%20in%20Philadelphia.
# therefore the subtotal should be multiplied by 1.06 to yield the total with tax
total_meal_price = 1.06*meal_subtotal

# display message including total price and tip suggestions 
print("With 6% tax, your total comes to ", round(total_meal_price, 2), ". You don't have to tip on tax, but here are some suggested tip amounts: ", 
      "$", round(0.1*meal_subtotal, 2), " (10%), ", "$", round(0.15*meal_subtotal, 2), " (15%), ", "$", round(0.2*meal_subtotal, 2), " (20%).")

#############################################################


"""
 Problem 4: Pig Latin
"""

# ask user for inputs 
first_letter_input = input("What's the first letter of your word?")

word_end_input = input("What's the rest of your word?")

# print the "translation"
print("The pig latin version of your word is '", word_end_input, first_letter_input, "ay'.", sep='')


#############################################################


"""
Problem 5: Tempearture converter
"""

# ask user for input, perform calculation and print result
temp_c = (float(input("Temperature in Fahrenheit:"))-32)*5/9

print(temp_c)




 
 