"""
Question: Implement a function that checks if a given key is present in a dictionary.
"""


def check_keys(dictionary, keys):
    if keys in dictionary:
        print(f"{keys}  in a dictionary.")
    else:
        print(f"There is no key named {keys} in dictionary")


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
key = input("Please enter a key : ")
check_keys(sample_dict, key)
