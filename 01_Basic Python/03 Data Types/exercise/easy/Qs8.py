"""
Question 8: Write a program that checks if a given number is a prime number.
"""


def primeOrNot(number):
    if number <= 2:
        return "Not prime number"

    for divisor in range(2, int(number**0.5)+1):
        if number % divisor == 0:
            return "not a prime number"

    return "Prime number"


print(primeOrNot(1))