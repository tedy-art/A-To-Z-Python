"""
Question 10:
Write a Python script that counts the number of vowels in a given string
using a for loop.
"""


def count_vowels(input_string):
    vowels = "aeiou"
    count = 0
    for char in input_string.lower():
        if char in vowels:
            count += 1
    return count


# Example usage
user_input = input("Enter a string: ")
result = count_vowels(user_input)
print(f"The number of vowels in the given string is: {result}")
