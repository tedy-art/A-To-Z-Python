"""
1. Positive or Negative:
Write a Python program that takes an integer input from the user
and prints whether it is positive, negative, or zero.
Step 1: get input from user
Step 2: check input value is positive, negative or zero
"""
user_in = int(input("Enter the number : "))
if user_in > 0:
    print("number is positive.")
elif user_in < 0:
    print("number is negative.")
else:
    print("number is Zero.")