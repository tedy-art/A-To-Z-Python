my_array = [3, 8, 2, 10, 5]

min_element = my_array[0]

for element in my_array:
    if element < min_element:
        min_element = element

print(min_element)