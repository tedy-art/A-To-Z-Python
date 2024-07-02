"""
Question 2:
Create a program that calculates and prints
the sum of all numbers from 1 to 100 using a for loop.
"""


def cal_sum(start, end):
    sum = 0
    for i in range(start, end+1):
        sum += i
    return sum


start, end = 1, 100
print(cal_sum(start, end))
