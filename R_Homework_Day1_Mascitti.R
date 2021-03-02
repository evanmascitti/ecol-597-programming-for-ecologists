#####
# Program: R Homework Day 1
# Author: Evan C. Mascitti
# Last Update: 2021-02-24
# Description: Answers to R homework assignment 1.
#####



# Problem #2: prime numbers ------------------------------------------------

# generate a sequence of all numbers from 2 to 100 (since 1 is not considered
# prime)

nums <- seq(2, 100, 1)

# for every number in the sequence, check if it can be evenly divided by any one of the
# other numbers. If it can't, print the number. 

cat("Prime numbers between 1 and 100 are:")
for (i in seq_along(nums)) {
  if (i %% nums[1:(i-1)] != 0) {
    cat(i, " ")
  }
}

# Problem #3: distance between 2 points ------------------------------------

# ask user for the coordinates of each point

pt1x <- as.double(readline("Point 1 x-coordinate: "))
pt1y <- as.double(readline("Point 1 y-coordinate: "))

pt2x <- as.double(readline("Point 2 x-coordinate: "))

pt2y <- as.double(readline("Point 2 y-coordinate: "))

# compute distance and print result rounded to 2 decimal places 

distance <- sqrt((pt2x - pt1x)^2 + (pt2y - pt1y)^2)
cat("distance is:",  round(distance, 2))



# #Problem #4: practice with vectors --------------------------------------

# assign 3 vectors:

a <- seq(0, 10, 2)
b <- seq(10, 100, 10)
c <- c(1, 15, 4, 20, 10, 6)

# part a) Find which numbers in vector c are greater than or equal to the max number in vector a.

# Use a vectorized comparison to index into c, selecting only the elements that match the logical condition

cat("Numbers in c that are greater than or equal to the largest number in a are: ", 
    c[c >= max(a)])

# part b) Find which numbers in vector c are in both vector a and vector b 

# similar strategy to part A: use two logicals inside the square selecting brackets 

cat("Members of c which occur in both a and b are: ", c[c %in% a & c %in% b])


# part c: Convert numbers in vector b from deg F to deg C

# take advantage of vectorized mathematical operators to perform calculation on all elements at once 

cat("numbers in b converted from F to C are: ", round((5/9)*(b-32), 2))
