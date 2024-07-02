"""
Question 4:
Implement a program that prints the even numbers from 2 to 20 using a for loop.
"""


def step_even_num(start, stop, step):
    print("way1 : step value :")
    for i in range(start, stop + 1, step):
        print(i)


def if_even_num(start, stop):
    print("way 2: if statement : ")
    for i in range(start, stop+1):
        if i % 2 == 0:
            print(i)


start = 2
stop = 20
step = 2
step_even_num(start, stop, step)
if_even_num(start, stop)
