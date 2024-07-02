"""
Question 3:
Write a function that takes three numbers as input and prints the largest of the three.
"""


def largest_num(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return f"{n1} is largest number."
    elif n2 > n1 and n2 > n3:
        return f"{n2} is largest number."
    else:
        return f"{n3} is largest number."


n1 = int(input("Number 1 : "))
n2 = int(input("Number 2 : "))
n3 = int(input("Number 3 : "))
print(largest_num(n1, n2, n3))