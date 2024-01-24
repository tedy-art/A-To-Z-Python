"""
Question 6:
Write a Python function that calculates and returns the factorial of a given
number using a while loop.
"""
n = int(input("Enter number : "))

result = 1
while n > 0:
    result *= n
    n -= 1
print(result)
