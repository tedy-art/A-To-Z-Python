"""
3. Write a Python function to multiply all the numbers in a list.
Sample List: (8, 2, 3, -1, 7)
Expected Output: -336
"""


def multi_num(numbers):
    multi = 1
    for number in numbers:
        multi *= number
    return multi


multi_list = [8, 2, 3, -1, 7]
print(multi_num(multi_list))
