"""
Develop a function that takes two dictionaries and checks if one is a subset of the
other (contains all the key-value pairs).
"""


def is_subset(dict1, dict2):
    for key, value in dict1.items():
        if key not in dict2 or dict2[key] != value:
            return False
    return True


# Demo dictionaries
dict1 = {'A': 1, 'B': 2, 'C': 3}
dict2 = {'A': 1, 'B': 2, 'C': 3, 'D': 4}  # dict2 is a superset of dict1

dict3 = {'A': 1, 'B': 2, 'C': 3}
dict4 = {'A': 1, 'B': 3, 'C': 3, 'D': 4}  # dict4 has a different value for key 'B'

dict5 = {'A': 1, 'B': 2, 'C': 3}
dict6 = {'A': 1, 'B': 2}  # dict6 does not have the key 'C'

# Test cases
print(is_subset(dict1, dict2))  # True
print(is_subset(dict3, dict4))  # False
print(is_subset(dict5, dict6))  # False
