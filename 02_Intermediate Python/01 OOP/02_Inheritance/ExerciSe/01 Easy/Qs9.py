"""
Write a class Person with methods walk() and talk().
Derive a class Student from Person with an additional method study()
"""


class Person:
    def walk(self):
        return 'walking'

    def talk(self):
        return 'talking'


class student(Person):
    def study(self):
        return 'study'


Nano = student()
print(Nano.walk())
print(Nano.talk())
print(Nano.study())
