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

Ex.
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
```
Buddy
woof!
```

**4) Encapsulation**
- Wrapping of data and methods together in one class is called Encapsulation.
- you can hide the internal state of an object from outside.

In python, encapsulation is achieved using access modifiers to control the visibility of attributes and methods.
There are three levels of access:
1) Public(default)
2) Protected('_' prefix)
3) Private('__' prefix)

**1) Public access modifiers:**
- Members are accessible from outside the class.

Ex.
```python
class Myclass:
    def __init__(self, attribute):
        self.attribute = attribute
    
    def my_method(self):
        return "This is a public method."


# create a object
obj = Myclass(attribute="example")
print(obj.attribute) # access attribute
print(obj.my_method()) # access method
```

**2) Protected(`_` prefix) :**
- Members should not be accessed directly from outside the class but can be accessed in subclasses.
- by convention, an attribute or method with a single landing underscore(`_`) is considered protected.
- it signals that the attribute or method is intended for internal use within the class or its subclasses.

Ex.
```python
class Myclass:
    def __init__(self, _protected_attribute):
        self._protected_attribute = _protected_attribute

    def _protected_method(self):
        return "This is a protected method"
# Creating an object
obj = Myclass(_protected_attribute="example")
print(obj._protected_attribute)
print(obj._protected_method())
```
**Accessing Protected Members Outside the Class:**
- while it's generally recommended to treat protected members as an internal details, it's still possible to access them from outside the class.
- However, doing so it is discouraged, as it breaks encapsulation and can lead to unintended consequences.
Ex.
```python
class MyClass:
    def __init__(self, _protected_attribute):
        self._protected_attribute = _protected_attribute

    def _protected_method(self):
        return "This is a protected method."
obj = MyClass(_protected_attribute="example")

# (not recommended)
# Accessing the protected attribute from outside the class
print(obj._protected_attribute)

# (not recommended) 
# Calling the protected method from outside the class
print(obj._protected_method())
```

Ex> Protected Bank Account:
```python
class BankAccount:
    def __init__(self, account_number, _balance):
        self.account_number = account_number
        self._balance = _balance  # Protected attributes

    def _deduct_fee(self, amount):  # protected method
        fee = 1.50
        self._balance -= (amount + fee)

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._deduct_fee(amount)
            print(f"Withdrawal successful. Remaining balance is: ${self._balance:.2f}.")
        else:
            print("Invalid withdrawal amount or insufficient funds.")


# creating an object
account = BankAccount(account_number="123456", _balance=100.00)

# Not recommendable
print(account._balance)
account._deduct_fee(10.00)

# Depositing and withdrawing using public method
account.deposit(50.00)
account.withdraw(30.00
```
Output:
```
100.0
Withdrawal successful. Remaining balance is: $107.00.
```

**3) Private('__' prefix):**
- Members are not accessible from outside the class.
- In python, attributes and methods can be marked as private by prefixing their names with double underscore.
  - For ex. `__attributes`, `__methods`
- private attributes are intended and modified only within the class where they are defined.
- they are not intended for direct access from outside the class.
Ex.
```python
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
```
