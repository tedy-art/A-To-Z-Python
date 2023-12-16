"""
5. Write a Python function to calculate the factorial of a number (a non-negative integer)
The function accepts the number as an argument.
"""


def factorial1(num):
    fact = 1
    if num < 0:
        return "negative number!"
    elif num == 0:
        return "number is 0"
    else:
        for i in range(1, num + 1):
            fact = fact * i
        return fact


num = 5
print(factorial1(num))
