my_array = [3, 8, 2, 10, 5]

max_element = my_array[0]

for element in my_array:
    if element > max_element:
        max_element = element

print(max_element)