"""
Question 10:
Write a Python program that checks if a given string is a palindrome
(reads the same backward as forward).
"""
char =  input("Enter Char : ").lower()

if char == char[::-1]:
    print("palindrome")
else:
    print("Not palindrome")