"""
Question 6:
Write a Python function that calculates and returns the factorial of a given number
using a for loop.
"""


def factNum(num):
    if num < 0:
        return "-tiv value"
    elif num == 0:
        return "Zero"
    else:
        fact = 1
        for i in range(1, num+1):
            fact = fact * i
        return f"{num} = {fact}"


print(factNum(8))
