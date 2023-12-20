from random import randint


class Bank:
    def __init__(self):
        self.account = randint(100000, 999999)
        self.full_name = input("Enter name : ")
        self.phone_number = int(input("Enter phone number : "))
        self.balance = 0

    def show_info(self):
        print(f"Account number : {self.account}")
        print(f"Full name : {self.full_name}")
        print(f"Balance : {self.balance}\n")

    def show_balance(self):
        print(f"Current Balance = {self.balance}")

    def withdraw(self):
        amount = int(input("Enter amount to withdraw : "))
        if amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= amount

    def deposit(self):
        amount = int(input("Enter amount to deposit : "))
        self.balance += amount


banks = []


def check_account_exists(acc_no: int):
    global banks
    for obj in banks:
        if obj.account == acc_no:
            return obj
    return None


while True:
    print("1. create account.")
    print("2. show all details.")
    print("3. deposit.")
    print("4. withdraw")
    print("5. Transfer")
    print("6. Exit")
    choice = int(input("Enter choice : "))
    if choice == 1:
        obj = Bank()
        banks.append(obj)
        print(banks)
    elif choice == 2:
        if len(banks) == 0:
            print("No account has been created yet")
        else:
            for account in banks:
                account.show_info()
    elif choice == 3:
        if len(banks) == 0:
            print("No account has been created yet")
        else:
            acc_no = int(input("Enter account number to deposit :"))
            for obj in banks:
                if obj.account == acc_no:
                    obj.deposit()
                    break
                else:
                    print("Invalid account number.")
    elif choice == 4:
        if len(banks) == 0:
            print("No account has been created yet")
        else:
            acc_no = int(input("Enter account number to withdraw :"))
            for i in banks:
                if i.account == acc_no:
                    i.withdraw()
                    break
                else:
                    print("Invalid account number.")
    elif choice == 5:
        from_acc_no = int(input("Enter account number from which you want to transfer :"))
        to_acc_no = int(input("Enter account number to which you want to transfer :"))
        from_acc_obj = check_account_exists(from_acc_no)
        to_acc_obj = check_account_exists(to_acc_no)
        if from_acc_obj != None and to_acc_obj != None:
            transfer_amount = int(input("Enter transfer amount :"))
            if from_acc_obj.balance < transfer_amount:
                print("Insufficient Balance!")
            else:
                from_acc_obj.balance -= transfer_amount
                to_acc_obj.balance += transfer_amount
        else:
            print("account dose not exists!!")

    elif choice == 6:
        break
    else:
        print("Invalid choice!")
