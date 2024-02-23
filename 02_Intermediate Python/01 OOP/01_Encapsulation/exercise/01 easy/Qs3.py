"""
Question 3:
Write a class Circle with a private attribute radius.
Provide methods to set the radius and calculate the area.
"""


class Circle:
    def __init__(self):
        self.__radius = 0.0

    def set_radius(self, radius):
        if radius > 0:
            self.__radius = radius
            print(f"radius set to {radius}.")
        else:
            print("Invalid radius values.")

    def calculate_area(self):
        area = 3.14 * (self.__radius ** 2)
        return area


Circle_instance = Circle()
Circle_instance.set_radius(5.0)
area = Circle_instance.calculate_area()
print(f"area of the circle is {area}.")
