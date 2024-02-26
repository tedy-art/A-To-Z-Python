"""
Question:
Write a function that takes a dictionary and returns the key with the maximum value.
"""


def key_wih_max_value(dictionary):
    max_key = max(dictionary, key=dictionary.get)
    return f"{max_key}':' {dictionary[max_key]}"


example_dict = {'apple': 5, 'banana': 3, 'orange': 8, 'grape': 2}
x = key_wih_max_value(example_dict)
print(x)
