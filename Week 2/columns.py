#!/usr/local/bin/python3
# NAME: Nestor Alvarez
# FILE: columns.py
# DATE: Week 2
# DESC: Prints list of numbers in columns

# Create list of 100 numbers from 1 to 100
nums = list(range(1,101))
count = 0

for i in range(0, 10):
    for j in range(0, 10):
        print("{0:>5}".format(nums[count]), end= ' ')
        count = count + 1
    print()
