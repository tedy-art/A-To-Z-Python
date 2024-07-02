"""
Question 7:
Create a class Car with private attributes model and year.
Provide methods to set and get the car details.
"""


class Car:
    def __init__(self):
        self.__model = None
        self.__year = None

    def set_details(self, model, year):
        self.__model = model
        self.__year = year

    def get_details(self):
        if self.__model is not None and self.__year is not None:
            print(f"Car model is {self.__model} and year is {self.__year}.")
        else:
            print("Car details are incomplete. Please set both model and year.")


car_instance = Car()
model = input("Enter car model : ")
year = int(input("Enter year : "))
car_instance.set_details(model, year)
car_instance.get_details()
