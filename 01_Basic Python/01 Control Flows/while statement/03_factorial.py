"""
Write a Python program that asks the user to input a number. The program should
then calculate and print the factorial of that number.

The factorial of a non-negative integer `n` is the product of all positive integers
less than or equal to `n`. It is denoted by n!.

For example:

The factorial of 5(5!) is 5 × 4 × 3 × 2 × 1 = 120

The factorial of 0(0!) is defined to be 1.
"""
num = 5
fact = 1
i = 1

while i < 0:
    fact = fact * i
    i += 1
print(fact)