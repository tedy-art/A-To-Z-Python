"""
Question 9:
Write a script that takes a user's age as input and determines whether they are a
child (0-12),
teenager (13-19),
adult (20-59),
or senior (60 and above).
"""


def check_age(num):
    if 0 < num <= 12:
        return f"{num} year old person is child stage."
    elif 13 <= num <= 19:
        return f"{num} year old person is teenager stage."
    elif 20 <= num <= 59:
        return f"{num} year old person is adult stage."
    elif 60 <= num <= 100:
        return f"{num} year old person is senior stage."
    else:
        return f"{num} is not valid age."


num = int(input("Enter your age : "))
print(check_age(num))