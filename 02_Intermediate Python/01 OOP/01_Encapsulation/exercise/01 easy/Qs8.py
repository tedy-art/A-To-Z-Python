"""
Question 8:
Implement a class Rectangle with private attributes length and width.
Include methods to calculate the area and perimeter.
"""


class Rectangle:
    def __init__(self):
        self.__length = 0.0
        self.__width = 0.0

    def set(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        if self.__length is not None and self.__width is not None:
            area = self.__length * self.__width
            print(f"Area of rectangle is {area}.")
        else:
            print("Please give values for length and width.")

    def perimeter(self):
        if self.__length is not None and self.__width is not None:
            perimeter = 2 * (self.__length + self.__width)
            print(f"Perimeter of rectangle is {perimeter}.")
        else:
            print("please give values for length and width.")


rectangle_instance = Rectangle()

length =  int(input("Enter length : "))
width = int(input("Enter width : "))
rectangle_instance.set(length, width)

rectangle_instance.area()
rectangle_instance.perimeter()
