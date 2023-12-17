"""
Write a Python function that accepts a string and counts the number of
upper and lower case letters.

"""


def count_char(letter):
    count_upper = 0
    count_lower = 0
    for char in letter:
        if 'A' <= char <= 'Z':
            count_upper += 1
        elif 'a' <= char <= 'z':
            count_lower += 1
        else:
            print("Invalid input please check your input...")

    return f"upper char is {count_upper} and lower char : {count_lower}."


user_str = input("Enter user string : ")
print(count_char(user_str))