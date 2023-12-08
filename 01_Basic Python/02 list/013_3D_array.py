"""
13. Write a Python program to generate a 3*4*6 3D array whose each element is *
"""
# Create a 3D array using list comprehensions, with 3 rows, 4 columns, and each element initialized as '*'
array = [[['*' for col in range(6)] for col in range(4)] for row in range(3)]

# Print the resulting 3D array
print(array)
