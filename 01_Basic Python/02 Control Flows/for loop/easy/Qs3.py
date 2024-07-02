"""
Question 3:
Write a Python script that prints the multiplication table (up to 10)
for a given number using a for loop.
"""


def mul_num(num):
    for i in range(1,11):
        multi = num * i
        print(f"{num} x {i} = {multi}")


mul_num(10)