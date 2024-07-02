"""
Create a lambda function to calculate the factorial of a number.
"""
factorial = lambda n: 1 if n == 0 else n * factorial(n-1)
result = factorial(5)
print(result)
