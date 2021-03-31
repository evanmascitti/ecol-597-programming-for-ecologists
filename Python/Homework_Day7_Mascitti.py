# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 10:16:04 2021

@author: evanm
"""

"""
Program: Homework Day 7
Author: Evan C Mascitti
Last Update: 2021-02-12
Description: Answers to homework assignment 7.
"""

# Import the pandas library which I will be using to manipulat the 
# data for this homework. Set the abbreviation as `pd` 

import pandas as pd

## Problem 2: data wrangling for Dr. G

# part a)

# read data file and save as a new object

plant_data = pd.read_csv("plantData.csv")

# print the first 5 rows 

plant_data.head()

# alternatively, use indexing to select only the first 5 rows 
# this prints 5 rows because row indices start at zero and the 
# user-suppluied number is non-inlusive
print(plant_data[:5])

# part b) 

# select and print the shrub length column
# use square brackets to index to the correct column
# this returns a series

lengths = plant_data["length"]
print(lengths)


# part c) 

# print the treatment and site columns in 2 orders 
# use indexing to specify the order 
# the column names are provided with an in-line list

plant_data[["site", "treatment"]]
plant_data[["treatment", "site"]]


# part d)

# create a new column for shrub volume and print it 

plant_data["volume"] = plant_data["length"] * plant_data["width"] * plant_data["height"]

# print the new column 
plant_data['volume']


# part e)

# first import the numpy library which will be used to calculate the 
# log of volume

import numpy as np

# create a new column containing the carbon content of each observed shrub
# by applying the .log() method from numpy to the data frame

plant_data["carbon"] = 1.8+ 2*np.log(plant_data["volume"])

print(plant_data["carbon"])


# part f)

# use indexing and a conditional statement to keep only observations with
# heights greater than 5. Print only the heights column  by indexing into 
# this new data frame (operations here are read left to right)

plant_data[plant_data["height"] > 5]["height"]


# part g)

# compute the mean value of all the dependent variables for each treatment 
# type, averaged across all sites 

treatment_means = plant_data.groupby("treatment").mean()

# print only the mean heights 

treatment_means["height"]


# part h)

# find the maximum width observed at each site by using the `groupby` method 
# and then indexing to select only the width column, which is returned 
# as a series 

plant_data.groupby("site").max()["width"]


