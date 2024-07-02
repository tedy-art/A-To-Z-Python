print("Using temp variable : ")


my_list = [10, 20, 30, 40]
print(f"Original list : {my_list}")

# Swapping elements at positions 1 and 2
temp = my_list[1]
my_list[1] = my_list[2]
my_list[2] = temp

print(f"Swapping list : {my_list}")  # Output: [10, 30, 20, 40]
