"""
Question 4:
Implement a program that prints a pattern of stars in the shape of a right-angled
triangle using a while loop.
*
* *
* * *
* * * *
* * * * *
"""
print("My version : ")
num = 5
i = 0
while i <= num:
    j = 0
    while j < i:
        print("*", end=" ")
        j += 1
    i += 1
    print()

print("ChatGpt versions : ")
num = 5
i = 1
while i <= num:
    print("* " * i)
    i += 1
