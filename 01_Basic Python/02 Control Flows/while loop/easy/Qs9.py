"""
Question 9:
Write a Python script that asks the user to guess a secret number between 1 and 10.
Keep prompting until they guess correctly.
"""
import random
random_num = random.randint(1, 10)

while True:
    num = int(input("Guess : "))
    if num == random_num:
        print("You guess right.")
        break
    else:
        print("please try again")
