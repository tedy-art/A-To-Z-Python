"""
Question 4:
Build a Company class with
private attributes
 __employees (a list of employee names)
and
 __revenue (the company's revenue).
Provide methods to
add an employee,
remove an employee,
 and
calculate the average revenue per employee.
"""


class Company:
    def __init__(self, employees_list, revenue):
        self.__employees = employees_list
        self.__revenue = revenue

    def add_employee(self, employee_name):
        """Add an employee to the company."""
        self.__employees.append(employee_name)
        print(f"Employee '{employee_name}' added.")

    def remove_employee(self, employee_name):
        """Remove an employee from the company."""
        if employee_name in self.__employees:
            self.__employees.remove(employee_name)
            print(f"Employee '{employee_name}' removed.")
        else:
            print(f"Employee '{employee_name}' not found in the company.")

    def calculate_avg_revenue_per_employee(self):
        """Calculate the average revenue per employee."""
        if len(self.__employees) == 0:
            return 0
        else:
            return self.__revenue / len(self.__employees)


# Example usage:
employees = ['John', 'Alice', 'Bob']
company = Company(employees, 1000000)

company.add_employee('Eva')
company.add_employee('Reva')
company.add_employee('Janne')
company.remove_employee('Bob')
print(employees)
avg_revenue_per_employee = company.calculate_avg_revenue_per_employee()
print(f"Average revenue per employee: Rs{avg_revenue_per_employee:.2f}")
