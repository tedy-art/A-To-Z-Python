"""
Implement a lambda function to find the minimum of three numbers.
"""
min_three_number = lambda a, b, c: a if a < b and a < c else (b if b < c else c)

result = min_three_number(5, 2, 8)
print(result)
