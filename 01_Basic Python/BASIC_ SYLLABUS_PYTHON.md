### 1. Basic Python

| Topic                                     | Description                                                                                     |
|-------------------------------------------|-------------------------------------------------------------------------------------------------|
| What is Python?                           | Overview of Python and its applications                                                         |
| Variables, Data Types and type conversion | Understanding variables, numbers, strings, and booleans , Implicit and Explicit type conversion |
| Operators                                 | Arithmetic, comparison, logical, and assignment operators                                       |
| Control Flow                              | Conditional statements (if, elif, else), loops (for, while)                                     |
| Data Structures                           | Lists, tuples, dictionaries, sets                                                               |
| Functions                                 | Defining and using functions                                                                    |
| Input and Output                          | Reading input, printing output                                                                  |
| Exception Handling                        | Handling errors with try-except blocks                                                          |


# What is python

1) Python is a programming language created py Guido Van Rossum in 1991.<br>
2) It is a simple, general-purpose, dynamically typed, high-level programming language.<br>
3) It is an interpreted language that supports multiple paradigms i.e., functional approach, practical approach, modular 
approach, object-oriented approach.<br>

It is used in:<br>
1) Creating web applications.<br>
2) data science and machine learning.<br>
3) academic research.<br>
4) automation and many more.<br>

# Variables, Data Types and type conversion
## variables:<br>
A variable in programming is used to store data.

    ex.
        a = 10
        b = 1.1

#### Rule for naming a variable:<br>
    1) a to z OR A to Z OR 0 to 9 OR _(underscore).<br>
    2) you can't start a variable name with a digit.<br>
    3) use underscore if you want to create a variable name having two or more words.<br>

#### Good name for a variable:<br>
    number, salary, name, first_name, last_name, email, number1 .... more<br>

### Data Types :-
###### In python, data types are categorized into two main groups
###### 1) primitive Data Types (Basic data types)
###### 2) Non-primitive Data types (complex data types)
### Primitive Data Types :-
it is a fundamental data types provided by python language.
#### types of primitive data types:-

| sr   | Data Type          | Use/ Description                                                        | Example                     |
|------|--------------------|-------------------------------------------------------------------------|-----------------------------|
| 1)   | Integer Data types | Represents whole number without any decimal point.                      | x = 14                      | 
| 2)   | Float Data types   | Represents real number and is written in decimal point.                 | x = 14.5                    |
| 3)   | Boolean Data types | Represents the truth values 'True' or 'False'.                          | is_true = True              |
| 4)   | String Data types  | Represent sequence of characters enclosed with single or double quotes. | message = "Hello, python!"  |
| 5)   | None type          | Represent null value or absence values                                  | z = None                    |

### Non-primitive Data Types :-
There are more complex data types and are derived from primitiv data types.
#### types of primitive data types:-

| sr | Data Type             | Use/ Description                                                                                                | Example                               |
|----|-----------------------|-----------------------------------------------------------------------------------------------------------------|---------------------------------------|
| 1) | list Data types       | Ordered and mutable collection of elements.                                                                     | my_list = [1, 2, 3, "Python"]         |
| 2) | Tuple Data types      | Ordered and immutable collection of elements.                                                                   | my_tuple = (1, 2, 3, "Python")        |
| 3) | Set Data types        | Unordered collection of unique elements.                                                                        | is_true = True                        |
| 4) | Dictionary Data types | Unordered collection of key-value pairs.                                                                        | my_dict = {'name': 'John', 'age': 25} |
| 5) | String Data type      | Strings, while primitive, can also be considered non-primitive when they are treated as sequences of characters | x = "This is String"                  |

# First python program :

    print("Hello, World!")

#### Output :
    
    'Hello, World!'

#### Ex.

    name = "Jack"
    age = 22
    print(f"His name is {name} and he is {age} years old.")

#### Output

    His name is Jack and he is 22 years old.

| <h3> ** Take input from user **</h3> |
|--------------------------------------|
To take input from the user and store it in a variable, use input() function.

Ex.

    name = input ("Enter your name : ")
    print(f" Hello, { name }!")

Output
    
    Enter your name : Tejas
    'Hello, Tejas!'

## Python Types conversion
_In programming, it's common to convert integer to float, float to string and so more,_
_the process of converting the value of one data type (int, string, float etc.) to another data type is called type conversion._

#### Python has two types of type conversion
- _Implicit Type Conversion_
- _Explicit Type Conversion_

1) Implicit Type Conversion
- In implicit type conversion, python automatically converts one data type to another data type.
Ex.
    
    
    number_integer = 123
    number_float = 1.23
    
    # addition of int and float
    sum = number_integer + number_float
    print(sum)

Output

    124.23

| In this context, there are two variables, number_integer and number_float. When these two variables are added, the result is a float to prevent any potential data loss due to the inclusion of decimal values. |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|