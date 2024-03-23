"""
Design a class Fruit with a method taste().
Create subclasses Apple and Orange inheriting from Fruit.
"""


class Fruit:
    def taste(self):
        return "tasting"


class Apple(Fruit):
    pass


class Orange(Fruit):
    pass


o1 = Apple()
print(o1.taste())

o2 = Orange()
print(o2.taste())
print('New Changes')
