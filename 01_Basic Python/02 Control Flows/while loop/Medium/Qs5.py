"""
Question 5:
Write a Python script that iterates through a dictionary and prints the keys and
values using a while loop.
sample_dict = {
    "name": "John",
    "age": 25,
    "city": "Example City",
    "is_student": False,
    "grades": [90, 85, 92, 78]
}

"""
sample_dict = {
    "name": "John",
    "age": 25,
    "city": "Example City",
    "is_student": False,
    "grades": [90, 85, 92, 78]
}
keys = list(sample_dict.keys())
values = list(sample_dict.values())
length = len(keys)
index = 0

while index < length:
    key = keys[index]
    value = values[index]
    print(f"{key}: {value}")
    index += 1
