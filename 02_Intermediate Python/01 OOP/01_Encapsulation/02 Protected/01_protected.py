class BankAccount:
    def __init__(self, account_number, _balance):
        self.account_number = account_number
        self._balance = _balance  # Protected attributes

    def _deduct_fee(self, amount):  # protected method
        fee = 1.50
        self._balance -= (amount + fee)

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._deduct_fee(amount)
            print(f"Withdrawal successful. Remaining balance is: ${self._balance:.2f}.")
        else:
            print("Invalid withdrawal amount or insufficient funds.")


# creating an object
account = BankAccount(account_number="123456", _balance=100.00)

# Not recommendable
print(account._balance)
account._deduct_fee(10.00)

# Depositing and withdrawing using public method
account.deposit(50.00)
account.withdraw(30.00)
