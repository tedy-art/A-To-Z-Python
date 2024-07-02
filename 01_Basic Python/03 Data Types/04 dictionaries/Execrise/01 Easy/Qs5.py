"""
Question:
Create a function that takes a dictionary and
returns a list containing all the keys sorted in alphabetical order

todo:{
    function : "sort_keys",
    output : {
        return_key : "all_keys",
        sort : "alphabetical_order"
    }
}
sort_keys = attributes -> 1) dictionary
return_keys = return all keys in dictionary in a list
sort = sort those key in a alpha order
print
"""


def sort_keys(dictionary):
    keys = []
    for key in dictionary:
        keys.append(key)

    sort = sorted(keys)
    return sort


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
x = sort_keys(sample_dict)
print(x)

print("__________________________________________________________________")


def sort_keys_alphabetically(my_dict):
    key_list = list(my_dict.keys())
    for i in range(len(key_list)):
        for j in range(i + 1, len(key_list)):
            if key_list[i] > key_list[j]:
                key_list[i], key_list[j] = key_list[j], key_list[i]
        return key_list


my_dict = {
    "name": "Tejas",
    "age": 12,
    "city": "Ahmednagar",
    "is_student": True,
    "grades": [90, 85, 92, 78],
    "contact": {
        "email": "tejas@example.com",
        "phone": "321-654-7890"
    }
}

x = sort_keys_alphabetically(my_dict)
print(x)
