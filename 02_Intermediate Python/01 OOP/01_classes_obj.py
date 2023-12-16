class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("woof!")


# create an object
my_dog = Dog(name="Buddy", age=3)

# access attributes
print(my_dog.name)
my_dog.bark()
