"""
Question 2:
Write a function that calculates and returns the sum of squares of numbers in
a given list using a while loop.
    sample_numbers = [5, 12, 8, 20, 3, 15, 7, 10, 18, 25]
"""


def cal_squares(num_list):
    i = 0
    square_list = []
    while i < len(num_list):
        sqrt_num = num_list[i] ** 2
        square_list.append(sqrt_num)
        i += 1
    return square_list


def sum_of_sqrt(square_list):
    i = 0
    sum_lst = 0
    while i < len(square_list):
        sum_lst = sum_lst + square_list[i]
        i += 1
    return sum_lst


sample_numbers = [5, 12, 8, 20, 3, 15, 7, 10, 18, 25]
square_list = cal_squares(sample_numbers)
print(square_list)
print(sum_of_sqrt(square_list))