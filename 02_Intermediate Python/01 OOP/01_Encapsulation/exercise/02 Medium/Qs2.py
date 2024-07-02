"""
Question 2:
Design a VendingMachine class with private attributes
__items (a dictionary of item names and prices)
and
__balance (current balance in the machine).
Implement methods to add money, select an item, and return change.
"""


class VendingMachine:
    def __init__(self, items):
        self.__items = items  # Dictionary of item names and prices
        self.__balance = 0  # Current balance in the machine

    def add_money(self, amount):
        """Add money to the vending machine."""
        if amount > 0:
            self.__balance += amount
            print(f"Added ${amount} to the vending machine. Current balance: ${self.__balance}")
        else:
            print("Invalid amount. Please add a positive amount.")

    def select_item(self, item_name):
        """Select an item from the vending machine."""
        if item_name in self.__items:
            price = self.__items[item_name]
            if self.__balance >= price:
                self.__balance -= price
                print(f"Dispensing {item_name}. Enjoy your {item_name}!")
            else:
                print(f"Insufficient balance. Please add ${price - self.__balance} more.")
        else:
            print(f"Item '{item_name}' not available in the vending machine.")

    def return_change(self):
        """Return change to the user."""
        change = self.__balance
        self.__balance = 0
        return change


# Example usage:
items = {'cola': 1.50, 'chips': 1.00, 'candy': 0.75}
vending_machine = VendingMachine(items)

vending_machine.add_money(2.00)
vending_machine.select_item('cola')
print("Change returned:", vending_machine.return_change())
