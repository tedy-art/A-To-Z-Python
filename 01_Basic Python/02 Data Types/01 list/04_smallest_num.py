"""
4. Write a Python program to get the smallest number from a list.
"""


def smallest_num_in_list(list):
    min = list[0]
    for a in list:
        # Check if the current element 'a' is smaller than the current minimum 'min'
        if a < min:
            # If 'a' is smaller, update the minimum 'min' to 'a'
            min = a
    return min


print(smallest_num_in_list([10, 21, 100, 14, 27, 36]))
