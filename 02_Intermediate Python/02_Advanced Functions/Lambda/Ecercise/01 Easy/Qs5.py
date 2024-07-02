"""
Create a lambda function to double each element in a list.
"""
double = lambda element_list: [element * 2 for element in element_list]
result = double([54, 65, 21, 54])
print(result)
