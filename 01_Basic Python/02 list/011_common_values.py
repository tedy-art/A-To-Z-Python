"""
11. Write a Python function that takes two lists and returns True if they have at least one common member.
"""


def common_data(list1, list2):
    result = False
    for x in list1:
        for y in list2:
            if x == y:
                # If there's a common element, set 'result' to True and return it
                result = True
                return result
    return result


print(common_data([1, 2, 3, 4, 5], [5, 6, 7, 8, 9]))
print(common_data([1, 2, 3, 4, 5], [6, 7, 8, 9]))
