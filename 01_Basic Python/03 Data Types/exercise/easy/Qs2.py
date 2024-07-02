"""
Question 2: Write a function that takes a list of numbers and returns the
sum of all elements.
"""


# define
def sum_of_list(list1):
    addition = 0
    for ele in range(len(list1)):
        addition += list1[ele]
    return addition


exercise_list = [15, 7, 32, 45, 12, 5, 18, 24, 9, 30]
# call
x = sum_of_list(exercise_list)
print(f"addition of {exercise_list} = {x}.")
