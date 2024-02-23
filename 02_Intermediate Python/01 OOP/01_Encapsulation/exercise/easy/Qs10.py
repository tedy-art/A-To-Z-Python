"""
Question 10:
Create a class Dog with private attributes name and age.
Provide methods to set and get the dog's information.
"""


class Dog:
    def __init__(self):
        self.__name = None
        self.__age = None

    def set_dog(self, name, age):
        self.__name = name
        self.__age = age

    def get_dog(self):
        if self.__name is not None and self.__age is not None:
            print(f"Name of Dog is '{self.__name}' and age is '{self.__age}'.")
        else:
            print("please set your details first.")


dog_instance = Dog()
dog_instance.set_dog('Tommy', 5)
dog_instance.get_dog()
