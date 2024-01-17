"""
9. Write a Python program to clone or copy a list.
"""
sample_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# way 1
print()
print("way 1 with `list()`")
new_list = list(sample_list)
print(new_list)

print()
print("way 2 with `assign old list to new list`")
new_list = sample_list
print(new_list)

print()
print("way 3 with `for loop & append`")
new2list = []
for i in sample_list:
    new2list.append(i)

print(new2list)