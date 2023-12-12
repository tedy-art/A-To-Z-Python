"""
1. Write a Python program to create a tuple.
"""

print("way 1")
tuple1 = ()
print(type(tuple1))
print(f"empty tuple : {tuple1}")

print()
print("way 2")
tuple2 = ("apple", "banana", "cherry")
print(type(tuple2))
print(f"{tuple2}")

print()
print("way 3")
tuple3 = tuple((1, 2, 3, 5, 6, 3))
print(type(tuple3))
print(f"with `tuple()` constructor {tuple3}")
