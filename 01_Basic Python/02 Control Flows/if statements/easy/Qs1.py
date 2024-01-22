"""
Question 1:
Write a program that checks if a given number is even.
If it is, print "Even," otherwise print "Odd."
"""


def check_even_odd(num):
    if num % 2 == 0:
        return f"{num} is even"
    else:
        return f"{num} is odd"


n = int(input("Enter a number : "))
print(check_even_odd(n))
