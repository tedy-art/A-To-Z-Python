"""
Question 1:
Implement a program that finds and prints the prime numbers between 1 and 30
using a while loop.
"""
i = 2
while i < 100:
    j = 2
    while j < 30:
        if i % j == 0:
            break
        j += 1
    if i == j:
        print(i, end=",")
    i += 1
