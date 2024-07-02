"""
Question 5:
Create a program that asks the user for their age.
If the age is less than 18, print "Minor"; otherwise, print "Adult."

"""


def find_category(age):
    if age < 18:
        return f"Minor"
    if age > 18:
        return f"Adult"


age = int(input("Age : "))
print(find_category(age))
