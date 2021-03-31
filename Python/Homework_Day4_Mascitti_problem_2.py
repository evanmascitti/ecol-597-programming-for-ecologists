# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 21:16:35 2021

@author: evanm
"""

# assign raw data to variables 

observed_group_1_data = [1, 4, 5, 3, 1, 5, 3, 7, 2, 2]
observed_group_2_data = [6, 7, 9, 3, 5, 7, 8, 10, 12]
combined_data = observed_group_1_data + observed_group_2_data


# define a function to compute the difference between the mean of two groups

def mean_diff(group_1, group_2):
    group_1_mean = sum(group_1)/len(group_1)
    group_2_mean = sum(group_2)/len(group_1)
    experiment_diff = abs(group_1_mean - group_2_mean)
    return(experiment_diff)


# apply the function to the observed data set 

observed_difference = abs(mean_diff(group_1 = observed_group_1_data,
                                group_2 = observed_group_2_data))

# import the `random` library
import random


# Run the simulations by taking a random sample of half the observations from 
# the whole data set. Allow the user to choose the number of simulations. 


# Start the iteration number at 1
i = 1 

# create an empty list that will be used to store the results of the simulations
x = []

# as user to supply number of simulations 
n_simulations = int(input("How many random simulations do you want to run?"))

# Use a while loop to repeat the action as long as the iteration number 
# is less than the desired number of simulations. For each iteration, append 
# the list to house the mean difference for that simulation

while i <= n_simulations: 
    group_1 = random.sample(combined_data, len(observed_group_1_data))
    group_2 = list(set(combined_data) - set(group_1))
    departure = abs(mean_diff(group_1, group_2))
    i += 1
    x.append(departure)

# create another empty list which will be used to store whether the difference 
# in the observed data set was larger than the randomly chosen data set
larger_diff_count = []

# loop over the mean of each simulation and append the list with a logical 
# statement about whether it was larger or not.

for i in x: 
    if i >= 1:
      larger_diff_count.append(True)
    else:
        larger_diff_count.append(False)
        
# The `larger_diff_count` list now contains the results of whether the observed 
# difference was larger or smaller than the randomly generated data. Tally the number 
# that exceeded the randomly chosen samples and print the results. 

n_random_exceed = n_simulations - sum(larger_diff_count)        
print("The difference betwen groups was ", round(observed_difference, 2), ".", sep="")
print("A difference at least this large occurred", n_random_exceed, "times out of", n_simulations, "simulations.")
print("p-value:", round(n_random_exceed / n_simulations, 3))
      
      
      
      

