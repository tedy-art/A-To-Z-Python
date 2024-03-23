"""
Design a class Shape with methods area() and perimeter().
Create subclasses Square and Triangle inheriting from Shape.
"""


class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2

    def perimeter(self):
        return self.length * 4


class Triangle(Shape):
    def __init__(self, base, height):
        self.height = height
        self.base = base
        # A = ½ (b × h)

    def area(self):
        return 0.5 * (self.height * self.base)

    def perimeter(self):
        return 3 * self.base


square = Square(5)
print(f"area of Square : {square.area()}")
print(f"perimeter of Square : {square.perimeter()}")

area_of_TR = Triangle(5, 6)
print(f"area of triangle : {area_of_TR.area()}")
print(f"perimeter of triangle : {area_of_TR.perimeter()}")
