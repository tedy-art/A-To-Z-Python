"""
Question:
Write a program that iterates through a dictionary and prints each key-value pair.
"""
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

# for key, value in sample_dict.items():
#     print(f"{key , value}")

for key in sample_dict:
    print(f"{key} : {sample_dict[key]}")