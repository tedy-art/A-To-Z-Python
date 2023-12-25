### 2. Intermediate Python

| Topic                             | Description                                                                            |
|-----------------------------------|----------------------------------------------------------------------------------------|
| Object-Oriented Programming (OOP) | Basics of OOP, classes, objects, encapsulation, abstraction, inheritance, polymorphism |
| Functions                         | Advanced function concepts, lambda functions                                           |
| Higher-Order Functions            | Definition,map(), filter(), reduce()                                                   |
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
| NOTE: functions that are defined within a class are typically referred to as "methods,"</br> while functions that exist outside of a class are generally called "functions." |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

```python
from random import randint


class Bank:
    def __init__(self):
        self.account = randint(100000, 999999)
        self.full_name = input("Enter name : ")
        self.phone_number = int(input("Enter phone number : "))
        self.balance = 0

    def show_info(self):
        print(f"Account number : {self.account}")
        print(f"Full name : {self.full_name}")
        print(f"Balance : {self.balance}\n")

    def show_balance(self):
        print(f"Current Balance = {self.balance}")

    def withdraw(self):
        amount = int(input("Enter amount to withdraw : "))
        if amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= amount

    def deposit(self):
        amount = int(input("Enter amount to deposit : "))
        self.balance += amount


banks = []


def check_account_exists(acc_no: int):
    global banks
    for obj in banks:
        if obj.account == acc_no:
            return obj
    return None


while True:
    print("1. create account.")
    print("2. show all details.")
    print("3. deposit.")
    print("4. withdraw")
    print("5. Transfer")
    print("6. Exit")
    choice = int(input("Enter choice : "))
    if choice == 1:
        obj = Bank()
        banks.append(obj)
        print(banks)
    elif choice == 2:
        if len(banks) == 0:
            print("No account has been created yet")
        else:
            for account in banks:
                account.show_info()
    elif choice == 3:
        if len(banks) == 0:
            print("No account has been created yet")
        else:
            acc_no = int(input("Enter account number to deposit :"))
            for obj in banks:
                if obj.account == acc_no:
                    obj.deposit()
                    break
                else:
                    print("Invalid account number.")
    elif choice == 4:
        if len(banks) == 0:
            print("No account has been created yet")
        else:
            acc_no = int(input("Enter account number to withdraw :"))
            for i in banks:
                if i.account == acc_no:
                    i.withdraw()
                    break
                else:
                    print("Invalid account number.")
    elif choice == 5:
        from_acc_no = int(input("Enter account number from which you want to transfer :"))
        to_acc_no = int(input("Enter account number to which you want to transfer :"))
        from_acc_obj = check_account_exists(from_acc_no)
        to_acc_obj = check_account_exists(to_acc_no)
        if from_acc_obj != None and to_acc_obj != None:
            transfer_amount = int(input("Enter transfer amount :"))
            if from_acc_obj.balance < transfer_amount:
                print("Insufficient Balance!")
            else:
                from_acc_obj.balance -= transfer_amount
                to_acc_obj.balance += transfer_amount
        else:
            print("account dose not exists!!")

    elif choice == 6:
        break
    else:
        print("Invalid choice!")
```
Output:
```
1. create account.
2. show all details.
3. deposit.
4. withdraw
5. Transfer
6. Exit
Enter choice : 1
Enter name : Tejas
Enter phone number : 9854875487
[<__main__.Bank object at 0x000001BA270B6010>]

1. create account.
2. show all details.
3. deposit.
4. withdraw
5. Transfer
6. Exit
Enter choice : 1
Enter name : Ak
Enter phone number : 8787878787
[<__main__.Bank object at 0x000001BA270B6010>, <__main__.Bank object at 0x000001BA270C4D10>]

1. create account.
2. show all details.
3. deposit.
4. withdraw
5. Transfer
6. Exit
Enter choice : 2
Account number : 213328
Full name : Tejas
Balance : 0

Account number : 291270
Full name : Ak
Balance : 0

1. create account.
2. show all details.
3. deposit.
4. withdraw
5. Transfer
6. Exit
Enter choice : 3
Enter account number to deposit :291270
Enter amount to deposit : 5000

1. create account.
2. show all details.
3. deposit.
4. withdraw
5. Transfer
6. Exit
Enter choice : 2
Account number : 213328
Full name : Tejas
Balance : 0

Account number : 291270
Full name : Ak
Balance : 5000

1. create account.
2. show all details.
3. deposit.
4. withdraw
5. Transfer
6. Exit
Enter choice : 4
Enter account number to withdraw :291270
Enter amount to withdraw : 500

1. create account.
2. show all details.
3. deposit.
4. withdraw
5. Transfer
6. Exit
Enter choice : 5
Enter account number from which you want to transfer :291270
Enter account number to which you want to transfer :213328
Enter transfer amount :2500

1. create account.
2. show all details.
3. deposit.
4. withdraw
5. Transfer
6. Exit
Enter choice : 2
Account number : 213328
Full name : Tejas
Balance : 2500

Account number : 291270
Full name : Ak
Balance : 2000

1. create account.
2. show all details.
3. deposit.
4. withdraw
5. Transfer
6. Exit
Enter choice : 6

```
4) Pillars of OOPS
   1) encapsulation
   2) abstraction
   3) inheritance
   4) polymorphism
   
## 1) Encapsulation
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
## 2) Abstraction

- Abstraction in python is defined as a process of hiding or reducing complexity by hiding unnecessary details from user.
- abstract classes provide a blueprint for other classes and may contain abstract method that must be implemented by concrete subclass.
- we cannot create an object of abstract class.
- ### __`@abstractmethod`:__
    - If we intend to create an abstract method, it is necessary to import the 'abstract' module.
    - Then, define a function and annotate it with the `@abstractmethod` decorator to designate it as an abstract method.
    - Additionally, the 'abstract' module includes a 'pass' statement within it.
    - Ex
    ```python
     from abc import ABC, abstractmethod
  
    class class_name(ABC):
        @abstactmethod
        def abstract_method_name(self):
            pass
    ```   

ex
```python
from abc import ABC, abstractmethod

# Abstract class representing a Shape
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Concrete class representing a Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# Concrete class representing a Square
class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

# Using abstraction to create objects
circle = Circle(radius=5)
square = Square(side_length=4)

# Accessing the abstract interface without worrying about internal details
print(f"Area of Circle: {circle.area()}")
print(f"Area of Square: {square.area()}")
```
Output:
```python
Area of Circle: 78.5
Area of Square: 16
```

## 3) Inheritance
- Inheritance allows us to define a class that inherits all the methods and properties from another class.

- Parent class:
   - It is the class being inherited from, also called base class.

- Child class:
   - It is the class that inherited from another class also called drived class.

Parent & Child class syntax:
```
    class parent_class_name1:
        parent_class_body

    class Child_class_name(parent_class_name1):
        body_of_child_class
```

e.g.
```python
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def print_name(self):
         print(self.firstname, self.lastname)

class student(Person):
            pass

x = student('Jay','Doe')
x.print_name()    
x = Person('Jay','Doe')
x.print_name()
```

### Types of inheritance: -
1) Sample/single inheritance
2) Multi-level inheritance
3) Multiple inheritance
4) Hierarchical inheritance
5) Hybrid inheritance
6) Cyclic inheritance


### 1) Sample/single inheritance
- single Parent and single Child relation is called Sample/ single inheritance.

e.g.
```python
class P:
    def m1(self):
        print("This is parent m1 method")

class c(P):
    def m2(self):
        print("This is child m2 method")

jay = c()
jay.m2()
jay.m1()
```
Output
```
This is child m2 method
This is parent m1 method
```

### 2) Multi-level inheritance
- Multi-level inheritance is archived when a drived class inherit another  class, there is no limit the number of levels up to which, the Multi-level inheritance is archived in python.
- the relation between GP, P and child is Multi-level inheritance.

e.g.
```python
class GP:
    def m3(self):
        print("This is Grand parent m3 method.")

class P(GP):
    def m1(self):
        print("This is paranet m1 method.")

class c(P):
    def m2(self):
        print("This is child m2 method")


jay = c()
jay.m2()
jay.m1()
jay.m3()
```
output
```
This is child m2 method
This is paranet m1 method.
This is Grand parent m3 method.
```
### 3) Multiple inheritance:
- Python provides us a flexibility to inherit Multiple base class in the child class
- One child and Multiple paranets are Multiple inheritance.

e.g. 
```python
class p1:
    def m1(self):
        print("This is parent1 m1 method.")

class p2:
    def m2(self):
        print("This is parnet2 m2 method.")

class c(p1, p2):
    def m3(self):
        print("This is child m3 method.")

jay = c()
jay.m2()
jay.m1()
jay.m3()
```
Output:
```
This is parnet2 m2 method.
This is parent1 m1 method.
This is child m3 method.
```

### 4) Hirarchical inheritance:
- One Parent and Multiple child is Hirarchical inheritance.

e.g.
```python
class p:
    def m1(self):
        print("This is parent m1 method.")

class c1(p):
    def m2(self):
        print("This is child1 m2 method.")


class c2(p):
    def m3(self):
        print("This is child2 m3 method.")

jay = c1()
jay.m2()
jay.m1()

viru = c2()
viru.m1()
viru.m3()
```
Output:
```
This is child1 m2 method.
This is parent m1 method.
This is parent m1 method.
This is child2 m3 method.
```

### 5) Hybrid inheritance:
- combination of all types of inheritance is Hybrid inheritance.
- inheritance consisting of Multiple types of inheritance is called Hybrid inheritance

e.g.
```python
class school:
    def func1(self):
        print("This function is in school.")

class student1(school):
    def func2(self):
        print("This function is in student1.")

class student2(school):
    def func3(self):
        print("This function is in student2.")

class student3(student1, school):
    def func4(self):
        print("This function is in student3.")

print('*'*10, "student3", '*'*10)
o1 = student3()
o1.func1()
o1.func2()
o1.func4()

print('*'*10, "student2", '*'*10)
o2 = student2()
o2.func1()
o2.func3()

print('*'*10, "student1", '*'*10)
o3 = student1()
o3.func1()
o3.func2()

print('*'*10, "School", '*'*10)
o4 = school()
o4.func1()
```
Output:
```
********** student3 **********
This function is in school.
This function is in student1.
This function is in student3.
********** student2 **********
This function is in school.
This function is in student2.
********** student1 **********
This function is in school.
This function is in student1.
********** School **********
This function is in school.
```

### 4) polymorphism 
- polymorphism refers to having multiple forms.
- polymorphism is a programming term refer to use of the some function name but defferant signiture.
- e.g. `len()` it is used for a strings as well as integers.

Here are key points about polymorphism:
1. **Method Overriding:**
   - Polymorphism often involves method overriding, where a method in a base class is redefined (or overridden) in a derived class. This allows objects of different classes to provide their own implementation of a common method.

    ```python
    class Animal:
        def speak(self):
            return "Animal speaks"

    class Dog(Animal):
        def speak(self):
            return "Dog barks"

    class Cat(Animal):
        def speak(self):
            return "Cat meows"
    ```

2. **Common Interface:**
   - Polymorphism relies on a common interface, typically represented by a base class or an interface (in languages that support interfaces). Objects of different classes that share a common interface can be used interchangeably.

    ```python
    def animal_speech(animal):
        return animal.speak()

    dog = Dog()
    cat = Cat()

    print(animal_speech(dog))  # Output: Dog barks
    print(animal_speech(cat))  # Output: Cat meows
    ```

3. **Duck Typing:**
   - Some languages, including Python, follow the principle of "duck typing," where the suitability of an object for a particular operation is determined by its method and attributes rather than its type.

    ```python
    def print_area(shape):
        print(f"The area is: {shape.calculate_area()}")

    class Circle:
        def calculate_area(self):
            return 3.14 * self.radius ** 2

    class Rectangle:
        def calculate_area(self):
            return self.length * self.width

    # Both Circle and Rectangle can be passed to the print_area function
    print_area(Circle(radius=5))  # Output: The area is: 78.5
    print_area(Rectangle(length=4, width=3))  # Output: The area is: 12
    ```

4. **Operator Overloading:**
   - Polymorphism can extend to operators, allowing objects of different classes to respond to the same operator in a way that makes sense for each class.

    ```python
    class Vector:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __add__(self, other):
            return Vector(self.x + other.x, self.y + other.y)

    vec1 = Vector(x=1, y=2)
    vec2 = Vector(x=3, y=4)

    result = vec1 + vec2
    print(f"Resultant Vector: ({result.x}, {result.y})")  # Output: Resultant Vector: (4, 6)
    ```

- Polymorphism enhances code flexibility, reusability, and extensibility by allowing code to work with objects in a more generic way. 
- It promotes a more natural representation of real-world relationships and behaviors in code.

# Functions

| sr.no | Concept                 | 
|-------|-------------------------|
| 1     | Annotations             | 
| 2     | Lambda Functions        | 
| 3     | Using Lambda with `map` | 
| 4     | Sorting with Lambda     | 
| 5     | Conditional Expressions | 

## 1) Annotations
- Function annotations in Python allow you to attach additional information about the types of function parameters and the return value.
- Annotations are not enforced by the Python interpreter but can be used for documentation or type hinting.

Here's an example:

```python
def add(x: int, y: int) -> int:
    """Add two numbers."""
    return x + y
```

In this example:

- `x: int` and `y: int` are parameter annotations indicating that `x` and `y` should be of type `int`.
- `-> int` is the return type annotation indicating that the function returns an `int`.
- The docstring provides additional documentation.

Function annotations can be accessed using the `__annotations__` attribute:

```python
print(add.__annotations__)
# Output: {'x': <class 'int'>, 'y': <class 'int'>, 'return': <class 'int'>}
```

## 2)Lambda Function
- Lambda functions, also known as anonymous functions, are concise one-line created using the `lambda` keyword.
- They are often used for short, one-time operations where a full function definition is not required.
- Lambda functions can take any number of arguments but can only have one expression.

syntax:
```python
lambda arguments: expression
```

Ex:
```python
square = lambda x:x ** 2
result = square(5)
print(result)
```
output
```python
25
```

Ex.
Take argument which will be number
make a list 0 to N
```python

make_list = lambda x:[i for i in range(0, x + 1)]
list1 = make_list(9)
list2 = make_list(5)

print(f"list1 :{list1}")
print(f"list2 :{list2}")
```
Output:
```python
list1 :[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 :[0, 1, 2, 3, 4, 5]
```

```python
check_even = lambda num : num % 2 == 0

if check_even(16):
    print("even")
else:
    print("odd")
```
Output:
```python
even
```

## Lambda with other functions: (next is about higher order function like map(), filter() and more)
- Lambda functions are often used in conjunction with functions like `map()`, `filter()`, and `sorted()`.
- They are useful when you need a quick, throwaway function without the formality of a full function definition.

## Conditional Expressions:
- Conditional expressions, also known as ternary operators, provide a concise way to express conditional statements in a single line.
- syntax
```python
result_if_true if condition else result_if_false
```
Ex1.
```python
x = 5
y = 10
max_value = x if x > y else y
print(max_value)  # Output: 10
```
Ex2.
```python
value = 15
status = "Even" if value % 2 == 0 else "Odd"
print(status)  # Output: Odd
```

#  Higher-Order Functions
1) Definition
2) some higher-order function in python
   1) map()
   2) filter()
   3) reduce()


4) Definition:
- A higher order function in programming is a function that can take another function as argument or return function as a result.
- In other words, it treats functions as first-class citizens.
- In languages that support higher-order functions:
  - function is not just a block of code but can be passed around, 
  - assigned to variables, 
  - and used as arguments,
  - return values.

## 1) Accepting Functions as Arguments:
   - Higher order function takes one or more functions as parameters.
   - This allows for flexibility in behavior by allowing the caller to customize the function's operations.

Ex.
```python 
def apply_operation(func, x, y):
    return func(x, y)

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

result_add = apply_operation(add, 2, 3)
result_multi = apply_operation(multiply, 2, 3)
print(result_add)
print(result_multi)
```
```
5
6
```

## 2) returning Functions:
- A higher order function can also return a function as its result. 
- THis is useful for creating function on the fly or customizing behavior based on certain conditions.

```python
def create_multipiler(factor):
    def multipiler(x):
        return x * factor
    return multipiler

multiply_by_2 = create_multipiler(2)
result = multiply_by_2(5)
```

## 3) storing function in data structure
- Functions can be stored in data structures like lists, dictionaries, or other collections.
- This allows for dynamic selection and invocation of function.

e.g.
```python
def square(x):
    return x ** 2


def cube(x):
    return x ** 3


operations = [square, cube]

result_square = operations[0](3)  # 0 meaning index 0(square) and x = 3
result_cube = operations[1](3)    # 1 meaning index 1(cube) and x = 3
print(result_square)
print(result_cube)
```
Output
```
9
27
```

# Some most commonly used higher order function
## `map()`:
- The `map()` function executes a specified function for each item in an iterable. 
- The item is sent to the function as a parameter.

Syntax
```
map(function, iterables)
```
#### Parameter Values
| Parameter	 | Description                                                                                                                                                          |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| function	  | Required. The function to execute for each item                                                                                                                      |
| iterable   | Required. A sequence, collection or an iterator object. You can send as many iterables as you like, just make sure the function has one parameter for each iterable. |

Ex.
```python
def myfunc(a, b):
  return a + b

x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))

print(x)

#convert the map into a list, for readability:
print(list(x))
```
Output:
```
<map object at 0x034244F0>
['appleorange', 'bananalemon', 'cherrypineapple']
```
Ex. lambda with `map()`
```python
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]
```

### `filter()`:
- The filter() function returns an iterator where the items are filtered through a function to test if the item is accepted or not.

Syntax
```
filter(function, iterable)
```
#### Parameter Values
| Parameter | 	Description                                        |
|-----------|-----------------------------------------------------|
| function  | 	A Function to be run for each item in the iterable |
| iterable  | 	The iterable to be filtered                        |

Ex.
```python
ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = filter(myFunc, ages)

for x in adults:
  print(x)
```
output:
```
18
24
32
```

Ex. using lambda with `filter()`
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8]
```

## `reduce()`:
- reduce() function takes another function as one of its arguments.

Ex.
```python
from functools import reduce

# Example: Finding the product of elements in a list
numbers = [2, 3, 4, 5]

# Using reduce to find the product
product = reduce(lambda x, y: x * y, numbers)

# Output the result
print(product)  # Output: 120
```
 ##### Other functions are used with lambda:

| Sr No | Name          | Syntax                                      | Description                                     | Example                                                                  |
|-------|---------------|---------------------------------------------|-------------------------------------------------|--------------------------------------------------------------------------|
| 1     | `map()`       | `map(function, iterable)`                   | Applies a function to all items in an iterable. | `list(map(lambda x: x * 2, [1, 2, 3, 4]))`                               |
| 2     | `filter()`    | `filter(function, iterable)`                | Filters elements based on a function's result.  | `list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]))`                    |
| 3     | `reduce()`    | `reduce(function, iterable[, initializer])` | Applies a function cumulatively to the items.   | `from functools import reduce; reduce(lambda x, y: x + y, [1, 2, 3, 4])` |
| 4     | `sorted()`    | `sorted(iterable[, key][, reverse])`        | Returns a sorted list from the elements.        | `sorted([3, 1, 4, 1, 5, 9, 2, 6, 5])`                                    |
| 5     | `any()`       | `any(iterable)`                             | Returns `True` if at least one element is true. | `any([False, True, False])`                                              |
| 6     | `all()`       | `all(iterable)`                             | Returns `True` if all elements are true.        | `all([True, True, True])`                                                |
| 7     | `enumerate()` | `enumerate(iterable[, start])`              | Adds counter to an iterable and returns tuples. | `list(enumerate(['apple', 'banana', 'cherry']))`                         |
| 8     | `zip()`       | `zip(iterable1, iterable2, ...)`            | Combines elements from two or more iterables.   | `list(zip([1, 2, 3], ['a', 'b', 'c']))`                                  |


# File Handling :- 
