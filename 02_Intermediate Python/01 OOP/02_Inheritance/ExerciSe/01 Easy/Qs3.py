"""
Design a class Shape with a method area().
Create subclasses Rectangle and Circle inheriting from Shape with their own
implementations of area().
"""
import math


class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


# Example usage:
rectangle = Rectangle(5, 4)
print("Area of Rectangle:", rectangle.area())

circle = Circle(3)
print("Area of Circle:", circle.area())
