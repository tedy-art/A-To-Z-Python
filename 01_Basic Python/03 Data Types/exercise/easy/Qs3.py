"""
Question 3: Implement a program that checks if a given string is a palindrome.
"""
word = input("Enter you word : ")
if word == word[::-1]:
    print("word is palindrome.")
else:
    print("word is not palindrome.")