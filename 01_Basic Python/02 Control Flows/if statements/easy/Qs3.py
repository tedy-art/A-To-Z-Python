"""
Question 3:
Write a Python script that checks if a given string is empty.
If it is, print "Empty," otherwise print "Not empty."

"""


def check_str_empty(str):
    if len(str) == 0:
        return "empty"
    if len(str) != 0:
        return "not empty"
    


str = input("Enter string : ")
print(check_str_empty(str))
