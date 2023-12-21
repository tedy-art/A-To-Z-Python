"""
Take argument which will be number
make a list 0 to N
"""
make_list = lambda x:[i for i in range(0, x + 1)]
list1 = make_list(9)
list2 = make_list(5)

print(f"list1 :{list1}")
print(f"list2 :{list2}")