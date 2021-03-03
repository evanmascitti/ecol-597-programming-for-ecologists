# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 21:16:35 2021

@author: evanm
"""
# define the raw data 
jason_group_1_data = [1, 4, 5, 3, 1, 5, 3, 7, 2, 2]
jason_group_2_data = [6, 7, 9, 3, 5, 7, 8, 10, 12]

# make a new list containing all the observations
combined_data = jason_group_1_data + jason_group_2_data

def mean_diff(group_1, group_2):
    group_1_mean = sum(group_1)/len(group_1)
    group_2_mean = sum(group_2)/len(group_1)
    experiment_diff = abs(group_1_mean - group_2_mean)
    return(experiment_diff)


observed_difference = abs(mean_diff(group_1 = jason_group_1_data,
                                group_2 = jason_group_2_data))


import random

# use a while loop to repeat the simulation as long as the iteration number 
# is less than 1000

i = 1 
x = []
while i <= 100: 
    group_1 = random.sample(combined_data, 10)
    group_2 = random.sample(combined_data, 10)
    departure = abs(mean_diff(group_1, group_2))
    i += 1
    # print(departure)
    x.append(departure)
print(x)   


ecm_count = []
for i in x: 
    if i >= 1:
      ecm_count.append(True)
   # else:
    #  ecm_count.append(False)
      
sum(ecm_count)

    