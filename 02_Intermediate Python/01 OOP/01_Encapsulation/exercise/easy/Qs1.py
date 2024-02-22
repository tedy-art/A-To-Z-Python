"""
Question 1:
Create a simple class Person with a private attribute name.
Provide a method to set the name and another method to get the name.
"""


class Person:
    def __init__(self):
        self.__name = None

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


person_instance = Person()

# set name to person
person_instance.set_name("Tejas")


# get name
name = person_instance.get_name()
print(f"Person's name is {name}.")

