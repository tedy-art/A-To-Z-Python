"""
Create a class Animal with a method speak().
Derive a class Dog from Animal with its own implementation of speak().
"""


class Animal:
    def speak(self):
        print("An animal speaks.")


class Dog(Animal):
    def speak(self):
        print("Woof!")


# Creating an instance of Dog
dog = Dog()

# Calling the speak() method of Dog
dog.speak()
