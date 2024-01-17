"""
7. Write a Python program to remove duplicates from a list.
"""
sample_list = [1, 2, 3, 3, 4, 8, 9, 8]

# Way 1
# unique_list = list(set(sample_list))

# Way 2
unique_list = []
for item in sample_list:
    if item not in unique_list:
        unique_list.append(item)

print(f"Original List : {sample_list}")
print(f"remove duplicate items : {unique_list}")