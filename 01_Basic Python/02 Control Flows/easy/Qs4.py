"""
Question 4:
Implement a program that takes two numbers as input and prints the larger of the two.

"""


def find_larger_num(num1, num2):
    if num1 > num2:
        return f"{num1} is larger number"
    if num1 < num2:
        return f"{num2} is larger number"


num1 = int(input("Number 1 : "))
num2 = int(input("Number 2 : "))
print(find_larger_num(num1, num2))