#####
# Program: R Homework Day 2
# Author: Evan C. Mascitti
# Last Update: 2021-03-02
# Description: Answers to R homework assignment 2.
#####

# install/load packages
if(!requireNamespace("AppliedPredictiveModeling", quietly = T)){install.packages("AppliedPredictiveModeling")}
library(tidyverse)
library(AppliedPredictiveModeling)


#  Problem 1: Abalone dataset

# load dataset 

data(abalone)

Abalone <- as_tibble(abalone)


# 1a) Calculate the mean and standard error for number of rings, for
# males and females separately.

# define standard error function

se <- function(x) {
  sd(x) / sqrt(length(x))
}

# apply the mean and standard error functions to the number of rings after grouping by male/female
# name the new columns with glue syntax (pasting together the variable name and the function which was applied)

Abalone %>% 
  group_by(Type) %>% 
  summarise(across(.cols = Rings, 
                   .fns = list(mean = mean, se = se), 
                   .names = "{.col}_{.fn}"))

# I'm no invertebrate biologist so not what type I indicates...either missing data or maybe they are hemaphrodites?? Running ?abalone wasn't much help so I am going to avoid diving down this rabbit hole...


# 1b) Make a new variable “volume”

# I switched the formula for radius to r = diameter / 2 rather than diameter*2

Abalone %>% 
  mutate(volume = pi*Height*(Diameter/2)^2) 

# 1c) Use piping to select all males with shells with more than 10 rings and then count how many males there are. Do the same thing for females.

Abalone %>% 
  filter(Rings > 10, Type == "M") %>% 
  group_by(Type) %>% 
  count(name = "n_shells")

Abalone %>% 
  filter(Rings > 10, Type == "F") %>% 
  group_by(Type) %>% 
  summarise(n_shells = n())

# 1d) Make a new tibble with just the Sex, Height and Diameter.

Abalone %>% 
  select(c(Type, Height, Diameter))



# Problem 2: mammal sleep data set  ---------------------------------------
 

# a) Error checking: How many instances don't add to 24 hours? Which animals are they?

# compute the total time as sum of time spent sleeping and awake, then filter out any rows where the total is exactly 24
# the near() function avoids potential mis-matches between floating point numbers which should evaluate to TRUE

error_check <- msleep %>% 
  mutate(time_correct = sleep_total + awake) %>% 
  filter(!near(time_correct, 24))

# It's easy to see there are only two wrong times because the number of occurences is small, but this wouldn't be true if there were more....so to do this with code, count them use nrow()

n_wrong_times  <- nrow(error_check)

# Print the number and names of the animals:
# use the glue package to run a valid R expression inside a string. Also use the stringr package to insert " and " between the arbitrary number of occurrences matching the condition

glue::glue("There were {n_wrong_times} instances where the time spent sleeping and awake did not sum to 24 hours. The animals were {stringr::str_c(unique(error_check$name), collapse = ' and ')}.")

# b) Make a list of all the domesticated species in the msleep dataset, in alphabetical order.
# Hint: Domesticated species have the entry “domesticated” in the column “conservation”.

# filter to contain only observations having the tag "domesticated" 
domesticated <- msleep %>% 
  filter(conservation == "domesticated") %>% 
  arrange(name) %>% 
  select(name)

# print result 
cat("There are ", length(domesticated$name), "domesticated animals. They include: ", domesticated$name)

# c) Using the function top_n(), identify the top-10 most-awake animals and list
# them from most awake to least awake. Hint: Before calling top_n(), use the
# function select() to extract the two columns name and sleep_total, in that
# order.

sleepiest <- msleep %>% 
  select(name, sleep_total) %>% 
  top_n( n = 10) %>% 
  arrange(desc(sleep_total))

cat("The 10th and 11th sleepiest animals are tied at", round(min(sleepiest$sleep_total), 2), "hr, so the list contains 11 animals. They are: ", sleepiest$name, ".")

# d) What is the max and min for sleep time for each order?

# need to add new columns with summarize after grouping by order. Like 1a, we could do this
# one function at a time, but more concise to use `across` to apply multiple
# functions to the same column of data. Rename them based on the original column
# names and the functions that were applied to them

msleep %>% 
  group_by(order) %>% 
  summarise(across(.cols = sleep_total, 
                   .fns = list(min = min, max = max), 
                   .names = "{.fn}_{.col}"))
  
#   e) Filter the rows for mammals that sleep a total of more than 16 hours and have a body
# weight of greater than 1 kilogram.

msleep %>% 
  filter(sleep_total > 16, bodywt > 1)


# f) Remember that the mutate() function will add new columns to the tibble. Create a
# new column called “rem_proportion” which is the ratio of rem sleep to total amount of
# sleep.

# create the column and then select only the name and the new column
# animals that have missing values have NA automatically inserted for the ratio

msleep %>% 
  mutate(rem_proportion = sleep_rem / sleep_total) %>% 
  select(name, rem_proportion)


