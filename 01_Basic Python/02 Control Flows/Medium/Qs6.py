"""
Question 6:
Create a program that asks the user for two numbers and prints "Equal"
if they are the same, otherwise print "Not equal."
"""
def equal_or_not(num1, num2):
    if num1 == num2:
        return f"{num1} and {num2} are equal."
    else:
        return f"{num1} and {num2} are not equal."

num1 = int(input("Enter : "))
num2 = int(input("Enter : "))
print(equal_or_not(num1, num2))