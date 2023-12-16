### 2. Intermediate Python

| Topic                             | Description                                                           |
|-----------------------------------|-----------------------------------------------------------------------|
| Object-Oriented Programming (OOP) | Basics of OOP, classes, objects, inheritance, polymorphism            |
| Functions                         | Advanced function concepts, lambda functions                          |
| Higher-Order Functions            | Definition,map(), filter(), reduce(), Functional Programming Concepts |
| File Handling                     | Reading from and writing to files                                     |
| Modules and Packages              | Organizing code into reusable modules and packages                    |
| Decorators                        | Enhancing the functionality of functions                              |
| Generators and Iterators          | Writing memory-efficient code                                         |
| Regular Expressions               | Pattern matching using regular expressions                            |

# Object-Oriented Programming(OOP):
1) Basic of OOP
2) class
3) objects
4) encapsulation
5) abstraction
6) inheritance
7) polymorphism

**1) Basic of OOP:**
- Object-oriented programming is a programming paradigm that uses objects to structure code.
- In python, everything is an object, and the language supports OOP principle.

**2) class :**
- a class is a blueprint for creating objects.
- it defines a data structure(attributes) and methods to manipulate that data.

**3) objects :**
- An object is an instance of a class. 
- it represents a real-world entity and has its own state and behavior.
- objects are created based on the structure defined by the class.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print("woof!")

# creating an object of the Dog class
my_dog = Dog(name="Buddy", age=3)

# Accessing attributes and calling methods
print(my_dog.name)
my_dog.bark()
```
Output
```python
Buddy
woof!
```

**4) Encapsulation**
