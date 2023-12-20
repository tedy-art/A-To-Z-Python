### 2. Intermediate Python

| Topic                             | Description                                                                            |
|-----------------------------------|----------------------------------------------------------------------------------------|
| Object-Oriented Programming (OOP) | Basics of OOP, classes, objects, encapsulation, abstraction, inheritance, polymorphism |
| Functions                         | Advanced function concepts, lambda functions                                           |
| Higher-Order Functions            | Definition,map(), filter(), reduce(), Functional Programming Concepts                  |
| File Handling                     | Reading from and writing to files                                                      |
| Modules and Packages              | Organizing code into reusable modules and packages                                     |
| Decorators                        | Enhancing the functionality of functions                                               |
| Generators and Iterators          | Writing memory-efficient code                                                          |
| Regular Expressions               | Pattern matching using regular expressions                                             |

# Object-Oriented Programming(OOP):
1) Basic of OOP
2) class
3) objects
4) Pillars of OOPS
   1) encapsulation
   2) abstraction
   3) inheritance
   4) polymorphism

## 1) Basic of OOP:
- Object-oriented programming is a programming paradigm that uses objects to structure code.
- In python, everything is an object, and the language supports OOP principle.

__1.1 What is OOPS??__
- Object-Oriented Programming (OOP) is a programming paradigm that organizes code into objects, each of which represents an instance of a class. The fundamental idea behind OOP is to model real-world entities and problems by creating and manipulating objects, which are instances of classes.
- Object-Oriented Programming (OOP) is a programming paradigm designed to model real-world entities and solve complex problems by organizing code into objects, which represent instances of classes.
-  OOP promotes the DRY principle by encouraging code reuse through concepts like inheritance and encapsulation. With inheritance, you can create a new class by inheriting attributes and methods from an existing class, reducing code duplication.

###  1.2 `_ _init_ _()`:
- `__init__()` is a special method in Python classes, also known as the constructor.
- It is automatically called when an object is created from a class, and it initializes the object's attributes. 
- The name `__init__` stands for "initialize."

### 1.3 self:
- self is a convention used to represent the instance of a class.
- It is the first parameter in the definition of instance methods, including special methods like `__init__`.
- The name self is not a keyword in the language; rather, it's a widely adopted convention.

## 2) class :
- a class is a blueprint for creating objects.
- it defines a data structure(attributes) and methods to manipulate that data.

## 3) objects :
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

## 4) Encapsulation
- Wrapping of data and methods together in one class is called Encapsulation.
- you can hide the internal state of an object from outside.

In python, encapsulation is achieved using access modifiers to control the visibility of attributes and methods.
There are three levels of access:
1) Public(default)
2) Protected('_' prefix) [single underscore]
3) Private('_ _' prefix) [Double underscore]

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
Ex> private 
```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary  # Private attribute with name mangling

    def __deduct_tax(self, amount):
        tax_rate = 0.15
        taxed_amount = amount * (1 - tax_rate)
        self.__salary -= taxed_amount  # Private method

    def receive_salary(self, amount):
        self.__deduct_tax(amount)
        print(f"{self.name} received a salary of ${amount:.2f}. Net salary after tax: ${self.__salary:.2f}")

# Creating an object of the Employee class
employee = Employee(name="Alice", salary=50000.00)

# Accessing the private attribute from outside the class (name mangling is applied)
# This is not recommended and should be avoided.
# Note: Do not use the mangled name directly, use the attribute as intended.
print(employee._Employee__salary)

# Receiving a salary using the public method
employee.receive_salary(5000.00)
```
## 5) Abstraction

