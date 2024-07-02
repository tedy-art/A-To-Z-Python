"""
Question:
Implement a function that removes a key-value pair from a dictionary based on a
given key.

todo:
    1) function: remove_key_values(arguments)
    2) arguments: 1) dictionary
                  2) get input from user as key
    3) function do:
        1) get dictionary and input from user and save it in temporary memory
        2) use for loop to iterate all keys
        3) use if condition : if 'key' is present:
                1) locate a key and delete it's value and also key.
                2) return message and updated dictionary.
        4) use else condition : if key is not present in dictionary.
"""


def remove_key_values(dictionary, keys):
    print(dictionary.keys())
    if keys in dictionary.keys():
        dictionary.pop(keys)
        print(f"{keys} is removed {dictionary.keys()}.")


sample_dict = {
    "name": "John",
    "age": 25,
    "city": "Example City",
    "is_student": False,
    "grades": [90, 85, 92, 78],
    "contact": {
        "email": "john@example.com",
        "phone": "123-456-7890"
    }
}
key = input("Provide key to remove a key: value pair : ")
remove_key_values(sample_dict, key)
