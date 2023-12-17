class Myclass:
    def __init__(self, attribute):
        self.attribute = attribute

    def my_method(self):
        return "This is a public method."


# create a object
obj = Myclass(attribute="example")
print(obj.attribute)  # access attribute
print(obj.my_method())  # access method