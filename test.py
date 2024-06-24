class parent:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def print_data(self):
        print(f"name is {self.name} and age is {self.age}")
    

class child(parent):
    def print_data(self):
        print(f"child's name is {self.name} and age is {self.age}")

obj1 = parent("ABC", 20)

obj1.print_data()

obj2 = child("xyz", 10)
obj2.print_data()