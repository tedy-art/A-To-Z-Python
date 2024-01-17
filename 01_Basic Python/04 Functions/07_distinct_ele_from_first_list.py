"""
Write a Python function that takes a list and returns a new list with distinct
elements from the first list.
Sample List: [10,20,20,20,10,10,50]
Unique List: [10,20,50]
"""


def distinct_item(l1):
    unique_list = []
    for item in l1:
        if item not in unique_list:
            unique_list.append(item)

    return unique_list


List1 = [10, 20, 20, 20, 10, 10, 50]
x = distinct_item(List1)
print(x)
