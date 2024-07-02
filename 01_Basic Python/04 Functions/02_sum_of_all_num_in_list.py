"""
2. Write a Python function to sum all the numbers in a list.
Sample List: (8, 2, 3, 0, 7)
Expected Output: 20
"""


# way 1: define function
def sum_list1(numbers):
    sum = 0
    for number in numbers:
        sum += number

    return sum


# way 2: define function
def sum_list2(numbers):
    return sum([number for number in numbers])


# Calling functions
num_list = [8, 2, 3, 0, 7]
print(sum_list1(num_list))
print(sum_list2(num_list))
