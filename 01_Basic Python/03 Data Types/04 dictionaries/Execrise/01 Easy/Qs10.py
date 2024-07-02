"""
Question:
Implement a function that takes a dictionary and returns a new dictionary
with only the key-value pairs where the value is an integer.
"""


def value_integer(dictionary):
    new_dict = {}
    for key, value in dictionary.items():
        if type(value) == int:
            new_dict[key] = value

    return new_dict


input_dict = {'apple': 3, 'banana': 'two', 'orange': 5, 'grape': 2, 'kiwi': 'three'}
x = value_integer(input_dict)
print(x)
