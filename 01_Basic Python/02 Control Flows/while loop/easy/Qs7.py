"""
Question 7:
Write a script that asks the user for a positive integer and prints the numbers
from 1 to that integer using a while loop.
"""
while True:
    num = int(input("Enter positive number : "))
    if num > 0:
        i = 1
        while i <= num:
            print(i)
            i += 1
        break
    else:
        print("number is negative.")
        break