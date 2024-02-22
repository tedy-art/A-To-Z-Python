"""
Question 2:
Implement a class BankAccount with private attributes balance and account_number.
Include methods to deposit and withdraw money.
"""


class BankAccount:
    def __init__(self, account_number):
        self.__balance = 0.0
        self.__account_number = account_number

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited Rs.{amount}. New Balance: Rs.{self.__balance}.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew Rs.{amount}. New Balance: Rs.{self.__balance}.")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def get_balance(self):
        return self.__balance


account_number = "12458451200"
bank_account = BankAccount(account_number)

bank_account.deposit(1000.0)
bank_account.withdraw(500)

balance = bank_account.get_balance()
print(f"current balance :Rs.{balance}")
