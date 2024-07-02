"""
Question 7:
Implement a program that iterates through a string and prints each character
using a for loop.
"""


def print_char(sample_string):
    for char in range(len(sample_string)):
        print(f"index {char} = {sample_string[char]}")


sample_string = "Hello, World!"
print_char(sample_string)