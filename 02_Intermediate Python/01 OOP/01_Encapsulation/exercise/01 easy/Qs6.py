"""
Question 6:
Write a class TemperatureConverter with private attributes Celsius and Fahrenheit.
Include methods to convert between Celsius and Fahrenheit.
"""


class TemperatureConverter:
    def __init__(self):
        self.__celsius = 0.0
        self.__fahrenheit = 0.0

    def set_celsius(self, celsius):
        self.__celsius = celsius

    def set_fahrenheit(self, fahrenheit):
        self.__fahrenheit = fahrenheit

    def convert_c_to_f(self):
        if self.__celsius is not None:
            self.__fahrenheit = (self.__celsius * 9/5) + 32
            print(f"{self.__celsius} degrees Celsius is {self.__fahrenheit} degrees Fahrenheit.")
        else:
            print("Please set the temperature in the celsius first.")

    def convert_f_to_c(self):
        if self.__fahrenheit is not None:
            self.__celsius = (self.__fahrenheit - 32) * 5/9
            print(f"{self.__fahrenheit} degrees fahrenheit is {self.__celsius} degrees celsius.")


temperatureconverter_instance = TemperatureConverter()

temperatureconverter_instance.set_celsius(25)
temperatureconverter_instance.convert_c_to_f()

temperatureconverter_instance.set_fahrenheit(77)
temperatureconverter_instance.convert_f_to_c()
