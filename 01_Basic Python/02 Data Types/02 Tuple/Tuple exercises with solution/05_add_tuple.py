"""
5. Write a Python program to add an item to a tuple.
"""
thistuple = ("apple", "banana", "cherry")
thislist = list(thistuple)
thislist.append("kiwi")
thistuple = tuple(thislist)

print(thistuple)

thistuple = ("apple", "banana", "cherry")
thistuple += ("Kiwi", "Mango")
print(thistuple)