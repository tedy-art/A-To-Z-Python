class Employee:
    def __init__(self, name, __salary):
        self.name = name
        self.__salary = __salary  # private attribute

    def __deduct_tax(self, amount):
        tax_rate = 0.15
        taxed_amount = amount * (1 - tax_rate)
        self.__salary -= taxed_amount

    def recive_salary(self, amount):
        self.__deduct_tax(amount)
        print(f"{self.name} received a salary of ${amount:.2f}. Net salary after tax: ${self.__salary:.2f}.")


# creating an object
employee = Employee(name="Alice", __salary=5000.00)

# Access the private attributes from outside the class(not recommended)
print(employee._Employee.__salary)
