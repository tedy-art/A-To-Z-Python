"""
Question 5:
Develop a ShoppingCart class with private attributes
__items (a dictionary of item names and quantities)
and
__total (total cost of items in the cart).
Implement methods to
add items,
remove items,
 and
 calculate the final cost.
"""


class ShoppingCart:
    def __init__(self):
        self.__items = {}
        self.__total = 0

    def add_item(self, item_name, quantity, cost_per_item):
        """Add items to the shopping cart."""
        if item_name in self.__items:
            self.__items[item_name] += quantity
        else:
            self.__items[item_name] = quantity
        self.__total += quantity * cost_per_item

    def remove_item(self, item_name, quantity, cost_per_item):
        """Remove items from the shopping cart."""
        if item_name in self.__items:
            if self.__items[item_name] >= quantity:
                self.__items[item_name] -= quantity
                self.__total -= quantity * cost_per_item
                if self.__items[item_name] == 0:
                    del self.__items[item_name]
            else:
                print(f"Not enough quantity of {item_name} in the cart.")
        else:
            print(f"{item_name} not found in the cart.")

    def calculate_final_cost(self):
        """Calculate the final cost of all items in the cart."""
        return self.__total


# Example usage:
cart = ShoppingCart()
cart.add_item("Apple", 3, 1.50)  # Adding 3 apples at $1.50 each
cart.add_item("Banana", 2, 0.75)  # Adding 2 bananas at $0.75 each
cart.remove_item("Apple", 1, 1.50)  # Removing 1 apple
print("Final cost:", cart.calculate_final_cost())
