"""
Question: Create a function that takes a dictionary as an argument and returns
the number of key-value pairs in the dictionary.
"""


def dictionary(dict1):
    return len(dict1)


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

s1 = dictionary(sample_dict)
print(s1)