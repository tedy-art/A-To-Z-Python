"""
Question 2:
Create a program that determines if a user-inputted integer is positive, negative,
or zero.
"""


def check_Pos_Neg_zero(num):
    if num > 0:
        return "Positive"
    if num < 0:
        return "Negative"
    if num == 0:
        return "Zero"


n = int(input("Enter number : "))
print(check_Pos_Neg_zero(n))
