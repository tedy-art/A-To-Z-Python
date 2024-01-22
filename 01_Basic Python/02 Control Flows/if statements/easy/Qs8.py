"""
Question 8:
Write a script that asks the user for a number and prints "Positive"
if it's greater than 0, "Negative" if less than 0, and "Zero" if equal to 0.
"""


def pos_neg_zero(num):
    if num > 0:
        return "Positive"
    if num < 0:
        return "Negative"
    if num == 0:
        return "Zero"


num = int(input("Enter : "))
print(pos_neg_zero(num))