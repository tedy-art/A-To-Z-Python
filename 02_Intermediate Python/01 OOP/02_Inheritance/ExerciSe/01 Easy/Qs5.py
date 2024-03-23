"""
Write a class BankAccount with methods deposit() and withdraw().
Derive a class SavingsAccount from BankAccount with a method calculate_interest().
"""


class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited Rs.{amount}. Current balance is Rs.{self.balance}."
        else:
            return "Deposit amount must be greater than zero."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew Rs.{amount}. Current balance is Rs.{self.balance}."
        else:
            return "Insufficient funds."


class SavingsAccount(BankAccount):
    def calculate_interest(self, interest_rate):
        interest = self.balance * (interest_rate / 100)
        self.balance += interest
        return f"Interest calculated: Rs.{interest}. Current balance is Rs.{self.balance}."


# Example usage:
savings_acc = SavingsAccount()
print(savings_acc.deposit(1000))
print(savings_acc.calculate_interest(5))
print(savings_acc.withdraw(200))
