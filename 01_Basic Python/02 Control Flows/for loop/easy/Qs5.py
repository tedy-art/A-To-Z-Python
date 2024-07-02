"""
Question 5:
Create a program that prints the reverse of a given list using a for loop.
"""


def reverse_list(list1):
    rev_list = []
    for i in list1[::-1]:
        rev_list.append(i)
    return rev_list


sample_list = [2, 7, 14, 5, 23, 10, 18, 3, 15, 8]
print(reverse_list(sample_list))

rev_list = [i for i in sample_list[::-1]]

print(rev_list)
