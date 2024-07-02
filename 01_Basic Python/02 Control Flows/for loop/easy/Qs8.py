"""
Question 8:
Write a script that prints the square of each number in a given list
using a for loop.
"""


def square_list(list1):
    root_list = []
    for i in list1:
        rt = i ** 2
        root_list.append(rt)

    return root_list


sample_list = [2, 7, 14, 5, 23, 10, 18, 3, 15, 8]
print(square_list(sample_list))

# list comprehension
sqr_list = [i ** 2 for i in sample_list]
print(sqr_list)