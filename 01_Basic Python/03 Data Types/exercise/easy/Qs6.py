"""
Question 6: Implement a program that extracts the unique elements from a list and returns a new list.
"""


def element_count(random_list):
    sorted_list = []
    for ele in random_list:
        if ele not in sorted_list:
            sorted_list.append(ele)
    return sorted_list


random_list = [1, 2, 2, 3, 4, 4, 5]
x = element_count(random_list)
print(x)
