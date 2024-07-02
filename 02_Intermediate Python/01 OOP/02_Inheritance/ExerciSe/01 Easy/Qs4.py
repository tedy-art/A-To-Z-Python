"""
Implement a class Person with methods eat() and sleep().
Create a subclass Employee inheriting from Person with an additional method work().
"""
class Person:
    def eat(self):
        print("Person can eat.")

    def sleep(self):
        print("Person need to sleep for more efficient work")

class Employee(Person):
    def work(self):
        print("Employee need to work to gain money")


emp = Employee()
emp.eat()
emp.sleep()
emp.work()

