"""
Question 4: Create a function that counts the occurrences of each character in a
            given string and returns a dictionary.
"""


def count_characters(input_string):
    char_count = {}
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


result = count_characters("hello")
print(result)
