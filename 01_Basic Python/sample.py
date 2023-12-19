"""
n1 = int(input())
n2 = int(input())

sum = n1 + n2 # add()
# even or odd
if sum%2 == 0: # check()
    print("even number")
else:
    print("Odd number")

write a python function
1) Ask 2 number from user
2) Calculate total of 2 number
3) Print if the sum of addition is even or odd


Create 2 function 1)add(), 2) check
Add() for addition
Check() for check number is even or odd
"""

def add(n1, n2):
    sum = n1 + n2
    print(sum)
    return sum

def check(sum):
    if sum%2 == 0:
        print("even")
    else:
        print("Odd")

n1 = int(input("N1 : "))
n2 = int(input("N2 : "))
x = add(n1, n2)
check(x)