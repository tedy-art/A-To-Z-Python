"""
Implement a class Animal with a method move().
Create a subclass Bird inheriting from Animal with its own method fly().
"""


class Animal:
    def move(self):
        return 'moving'


class Bird(Animal):
    def fly(self):
        return 'flying'


parrot = Bird()
print(parrot.move())
print(parrot.fly())
