"""
8. Write a Python program to check if a list is empty or not.
"""
sample_list = [2, 5, 6, 9, 7]

# for empty condition
# sample_list = []

# ways 1
print("way 1 with `<=, >=`")
if len(sample_list) <= 0:
    print("list is empty")
elif len(sample_list) >= 0:
    print(f"list have some items around {len(sample_list)}")
print()

# way 2
print("way 2 with `==`")
if len(sample_list) == 0:
    print("List is empty")
else:
    print(f"the list has some items around {len(sample_list)}")
print()

# way 3
print("way 3 with logical `not`")
if not sample_list:
    print("list is empty")
else:
    print(f"the list has some items around {len(sample_list)}")