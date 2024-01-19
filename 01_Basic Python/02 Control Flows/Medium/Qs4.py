"""
Question 4:
Implement a program that checks if a given word is a palindrome,
considering both uppercase and lowercase characters.
"""

char =  input("Enter Char : ")

if char == char[::-1]:
    print("palindrome")
else:
    print("Not palindrome")