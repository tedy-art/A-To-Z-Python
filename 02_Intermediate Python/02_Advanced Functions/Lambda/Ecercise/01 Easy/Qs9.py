"""
Implement a lambda function to filter out even numbers from a list.
"""
filter_even_numbers = lambda lst: list(filter(lambda x: x % 2 == 0, lst))
print(filter_even_numbers([54, 65, 8, 4, 45, 88]))
