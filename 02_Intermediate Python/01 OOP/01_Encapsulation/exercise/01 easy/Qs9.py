"""
Question 9:
Write a class Employee with private attributes name and salary.
Include methods to set and get the employee details.
"""


class Employee:
    def __init__(self):
        self.__name = None
        self.__salary = None

    def set_employee(self, name, salary):
        self.__name = name
        self.__salary = salary

    def get_employee(self):
        if self.__name is not None and self.__salary is not None:
            print(f"Name of employee is '{self.__name}' and salary is '{self.__salary}'.")
        else:
            print("please set your details first.")


employee_instance = Employee()
employee_instance.set_employee('Tejas', 95000)
employee_instance.get_employee()
