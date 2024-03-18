"""
Question:
Create a program that simulates a simple inventory system.
It should have functions to add items, remove items, and display
the current inventory using a dictionary
"""


def add_item(inventory, item, quantity):
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity


def remove_item(inventory, item, quantity):
    if item in inventory:
        inventory[item] -= quantity
        if inventory[item] <= 0:
            del inventory[item]


def display_inventory(inventory):
    print("Current Inventory:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")


# Example Usage
inventory = {}

add_item(inventory, 'apple', 10)
add_item(inventory, 'banana', 5)
add_item(inventory, 'orange', 8)

display_inventory(inventory)

remove_item(inventory, 'banana', 2)

display_inventory(inventory)
