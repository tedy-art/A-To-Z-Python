class MyClass:
    def __init__(self):
        self.__private_attribute = "I am private"

    def __private_method(self):
        print("I am a private method")

obj = MyClass()

# Accessing private attribute (will raise an AttributeError)
print(obj.__private_attribute)

# Accessing private method (will raise an AttributeError)
obj.__private_method()
