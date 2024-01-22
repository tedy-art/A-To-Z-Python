"""
Question 8:
Implement a program that checks if a given number is a multiple of both 3 and 5.
If it is, print "FizzBuzz"; otherwise, print the number.
"""

num = int(input("Enter number : "))
if num%3 == 0 and num%5 == 0:
    print("FizzBuzz")
else:
    print(num)