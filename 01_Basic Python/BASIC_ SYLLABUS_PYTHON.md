### 1. Basic Python

| Topic                                     | Description                                                                                     |
|-------------------------------------------|-------------------------------------------------------------------------------------------------|
| What is Python?                           | Overview of Python and its applications                                                         |
| Variables, Data Types and type conversion | Understanding variables, numbers, strings, and booleans , Implicit and Explicit type conversion |
| Operators                                 | Arithmetic, comparison, logical, membership, identity and assignment operators                  |
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
```python
        a = 10
        b = 1.1
```
#### Rule for naming a variable:<br>
    1) a to z OR A to Z OR 0 to 9 OR _(underscore).<br>
    2) you can't start a variable name with a digit.<br>
    3) use underscore if you want to create a variable name having two or more words.<br>

#### Good name for a variable:<br>
    number, salary, name, first_name, last_name, email, number1 .... more<br>

## Data Types :-
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

### First python program :
```python
print("Hello, World!")
```
#### Output :
```python    
    'Hello, World!'
```
#### Ex.
```python
    name = "Jack"
    age = 22
    print(f"His name is {name} and he is {age} years old.")
```
#### Output
```python
    His name is Jack and he is 22 years old.
```
| <h3> ** Take input from user **</h3> |
|--------------------------------------|
To take input from the user and store it in a variable, use input() function.

Ex.
```python
name = input ("Enter your name : ")
print(f" Hello, { name }!")
```
Output
```python    
    Enter your name : Tejas
    'Hello, Tejas!'
```
## Python Types conversion
_In programming, it's common to convert integer to float, float to string and so more,_
_the process of converting the value of one data type (int, string, float etc.) to another data type is called type conversion._

#### Python has two types of type conversion
- _Implicit Type Conversion_
- _Explicit Type Conversion_

#### 1) Implicit Type Conversion
- In implicit type conversion, python automatically converts one data type to another data type.
Ex.
    
```python
    number_integer = 123
    number_float = 1.23
    
    # addition of int and float
    sum = number_integer + number_float
    print(sum)
```
Output
```python
    124.23
```

| In this context, there are two variables, number_integer and number_float. When these two variables are added, the result is a float to prevent any potential data loss due to the inclusion of decimal values. |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

#### 2) Explicit Type conversion
In Explicit type conversion user converts the data type of object to a required data type.

we use predefined function like int(), float(), str() etc., to perform explicit type conversion.

Ex.
```python
    float_num = 1.734
    
    # manually Converting to integer
    integer_num = int(float_num)

    print(f"float to integer number : {integer_num}.")
    print(f"data type of interger_num { type(integer_num)}.")
```    

Output : 
```python
    float to integer number : 1
    data type of integer_num <class 'int'>
```
conversions of one data type to another 

| conversions | details                                                                                                                                                                  |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| int - float | we can convert integer values to floating values without data loss.                                                                                                      |
| float - int | Converting floating-point values to integers is feasible; however, it comes with a caveat — the risk of data loss.                                                       |
| str - int   | While it is possible to convert string values to integers, errors may occur, especially when the variable contains a combination of alphabetical characters and symbols. |
| int - str   | we can convert int to string                                                                                                                                             |
| float - str | we can convert float to string                                                                                                                                           |

# Operators
Operators are special symbols in python that carry out educational or logical computation.
The value that the operator operates on is called operand.


| sr | Operator Type	 | Description                               | 	Example                         |
|----|----------------|-------------------------------------------|----------------------------------|
| 1) | Arithmetic	    | Perform mathematical operations           | 	+, -, *, /, //, %, **           |
| 2) | Comparison	    | Compare values                            | 	==, !=, <, >, <=, >=            |
| 3) | Logical	       | Perform logical operations                | 	and, or, not                    |
| 4) | Membership	    | Test if a value is a member of a sequence | 	in, not in                      |
| 5) | Identity       | 	Compare object identities                | 	is, is not                      |
| 6) | Assignment     | 	Assign values to variables               | 	=, +=, -=, *=, /=, //=, %=, **= |



### Arithmetic operators:

1. **Addition (`+`):** Adds two operands.
   ```python
   result = 10 + 5  # result is 15
   ```

2. **Subtraction (`-`):** Subtracts the right operand from the left operand.
   ```python
   result = 10 - 5  # result is 5
   ```

3. **Multiplication (`*`):** Multiplies two operands.
   ```python
   result = 10 * 5  # result is 50
   ```

4. **Division (`/`):** Divides the left operand by the right operand (always returns a float).
   ```python
   result = 10 / 5  # result is 2.0
   ```

5. **Floor Division (`//`):** Divides the left operand by the right operand and returns the floor value 
6. (rounded down to the nearest integer).
   ```python
   result = 10 // 3  # result is 3
   ```

6. **Modulus (`%`):** Returns the remainder of the division of the left operand by the right operand.
   ```python
   result = 10 % 3  # result is 1
   ```

7. **Exponentiation (`**`):** Raises the left operand to the power of the right operand.
   ```python
   result = 2 ** 3  # result is 8
   ```

### Comparison operators:

1. **Equal to (`==`):** Checks if two values are equal.
   ```python
   5 == 5  # True
   ```

2. **Not equal to (`!=`):** Checks if two values are not equal.
   ```python
   5 != 10  # True
   ```

3. **Less than (`<`):** Checks if the left value is less than the right value.
   ```python
   5 < 10  # True
   ```

4. **Greater than (`>`):** Checks if the left value is greater than the right value.
   ```python
   10 > 5  # True
   ```

5. **Less than or equal to (`<=`):** Checks if the left value is less than or equal to the right value.
   ```python
   5 <= 5  # True
   ```

6. **Greater than or equal to (`>=`):** Checks if the left value is greater than or equal to the right value.
   ```python
   10 >= 5  # True
   ```

Examples:

```python
x = 10
y = 20

print(x == y)   # False
print(x != y)   # True
print(x < y)    # True
print(x > y)    # False
print(x <= y)   # True
print(x >= y)   # False
```

### Logical operators :
In Python are used to perform logical operations on Boolean values. They help combine multiple conditions and evaluate
the overall truth value. Here are the main logical operators in Python:

| Operator | Description                      | Example                      |
|----------|----------------------------------|------------------------------|
| `and`    | Logical AND                      | `x and y`                    |
| `or`     | Logical OR                       | `x or y`                     |
| `not`    | Logical NOT                      | `not x`                      |

Here's a brief explanation of each logical operator:

- **Logical AND (`and`):** Returns `True` if both operands are true, otherwise `False`.
  ```python
  x = True
  y = False
  result = x and y  # result is False
  ```

- **Logical OR (`or`):** Returns `True` if at least one operand is true, otherwise `False`.
  ```python
  x = True
  y = False
  result = x or y   # result is True
  ```

- **Logical NOT (`not`):** Returns `True` if the operand is false and vice versa.
  ```python
  x = True
  result = not x    # result is False
  ```
  
### Membership operators
In Python are used to test whether a value is a member of a sequence, such as a string, list, tuple, or set. 
There are two membership operators: `in` and `not in`. Here's a brief explanation of each:

1. **`in` Operator:**
   - Returns `True` if a value exists in the sequence.
   - Returns `False` if the value is not found in the sequence.

   Example:
   ```python
   my_list = [1, 2, 3, 4, 5]
   
   print(3 in my_list)  # True
   print(6 in my_list)  # False
   ```

2. **`not in` Operator:**
   - Returns `True` if a value does not exist in the sequence.
   - Returns `False` if the value is found in the sequence.

   Example:
   ```python
   my_tuple = ('apple', 'banana', 'orange')
   
   print('grape' not in my_tuple)  # True
   print('banana' not in my_tuple) # False
   ```
   

### Identity operators:
In Python are used to compare the memory locations of two objects. They determine whether two variables refer to the 
same object in memory. There are two identity operators in Python: `is` and `is not`.

Here's a brief explanation of each identity operator:

| Operator | Description                                           | Example      |
|----------|-------------------------------------------------------|--------------|
| `is`     | True if the operands reference the same object        | `a is b`     |
| `is not` | True if the operands do not reference the same object | `a is not b` |

Examples:

```python
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x is y)        # False, because x and y are different objects
print(x is z)        # True, because x and z reference the same object
print(x is not y)    # True, because x and y are different objects
print(x is not z)    # False, because x and z reference the same object
```

### Assignment operators :
Assignment operators in Python are used to assign values to variables. They allow you to perform an operation and 
assign the result to a variable in a concise way. Here are the common assignment operators in Python.

1. **Assignment (`=`):** Assigns the value of the right operand to the left operand.
   ```python
   x = 5  # Assigns value 5 to the variable x
   ```

2. **Addition Assignment (`+=`):** Adds the right operand to the left operand and assigns the result to the left operand.
   ```python
   y = 10
   y += 5  # Equivalent to y = y + 5
   ```

3. **Subtraction Assignment (`-=`):** Subtracts the right operand from the left operand and assigns the result 
to the left operand.
   ```python
   z = 15
   z -= 3  # Equivalent to z = z - 3
   ```

4. **Multiplication Assignment (`*=`):** Multiplies the left operand by the right operand and assigns the result to 
the left operand.
   ```python
   a = 2
   a *= 4  # Equivalent to a = a * 4
   ```

5. **Division Assignment (`/=`):** Divides the left operand by the right operand and assigns the result to 
the left operand.
   ```python
   b = 10
   b /= 2  # Equivalent to b = b / 2
   ```

6. **Floor Division Assignment (`//=`):** Performs floor division on the left operand by the right operand and 
assigns the result to the left operand.
   ```python
   c = 10
   c //= 3  # Equivalent to c = c // 3
   ```

7. **Modulus Assignment (`%=`):** Calculates the modulus of the left operand divided by the right operand and assigns
the result to the left operand.
   ```python
   d = 7
   d %= 4  # Equivalent to d = d % 4
   ```

8. **Exponentiation Assignment (`**=`):** Raises the left operand to the power of the right operand and assigns the
result to the left operand.
   ```python
   e = 2
   e **= 3  # Equivalent to e = e ** 3
   ```

# Control Flow:
#### 1. if__elif__else statement
#### 2. while loops
#### 3. for loops


| 1. if statement  |
|------------------|
Python supports the usual logical conditions from mathematics : 
- Equal : `a == b`
- Not Equal : `a != b`
- Less than : `a < b`
- Less than and equal to : `a <= b`
- Greater than : `a > b`
- Greater than and equal to : `a >= b`

These conditions can be used in several ways, most commonly in "if statements" and loop.
An "if statement" is written by using the if keyword
Ex
```python
a = 33
b = 200
if b > a:
    print(f"{b} is greater than {a}.")
```
output
```python
'200 is greater than 33'
```
| 1.2 Elif Statement |
|--------------------|
The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".

Example
```python
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
```
Output:
```output
   a and b are equal
```

| 1.3 Else Statement |
|--------------------|
The else keyword catches anything which isn't caught by the preceding conditions.

Example
```python
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
```
Output:
```output
   a is greater than b
```

| 2. while loops |
|----------------|
Python while loop is used to execute a block of statements repeatedly until a given condition is satisfied.

Syntax:
```python
while condition:
    # body of while loop
```
ex.
```python
i = 1
n = 5

while i <= n:
    print(i)
    i = i + 1
```
output:
```output
1
2
3
4
5
```
#### The `break` Statement
with the `break` statement we can stop the loop even if the while condition is true.

Ex. 
```python
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
```
output :
```python
1
2
3
```
#### The `continue` Statement
with the `continue` statement we can stop the current iteration, and continue with the next.

Ex. Continues to the next iteration if i is 3:
```python
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
```
Output:
```python
1
2
4 # 3 is not display
5
6
```
#### The `else` Statement
with the `else` statement we can run a block of code once when the condition no longer is true:
Example:
```python
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")
```

| 3. for loops |
|--------------|
A for loop is used to iterating over a sequence (list, tuple, dictionary, set or string).
Ex. 
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```
Output:
```output
apple
banana
cherry
```
#### Looping Through a String
Even strings are iterable objects, they contain a sequence of characters:

Example

Loop through the letters in the word "banana":
```python
for x in "banana":
  print(x)
```
Output:
```python
b
a
n
a
n
a
```
| Note:<br/> In `for` loop, we can use operations like break, continue statement like we used in `while` loop |
|-------------------------------------------------------------------------------------------------------------|

#### The `range` function : 
To loop through a set of code a specified number of times, we can use the `range()` function,

Example :

Using the `range()` function:

```python
for x in range(6):
  print(x)
```
Output:
```python
0
1
2
3
4
5
```

| Note that range(6) is not the values of 0 to 6, but the values 0 to 5. |
|------------------------------------------------------------------------|


syntax
```python
range(start, stop, step)
```
| sr | operations | description               | Example                                    | output                   |
|----|------------|---------------------------|--------------------------------------------|--------------------------|
| 1) | Start      | start our iteration from  | for i in range(2):</br></t>print(i)        | 0</br>1                  |
| 2) | Stop       | stop our iteration        | for i in range(2, 6):</br></t>print(i)     | 2</br>3</br>4</br>5</br> |
| 3) | Step       | step over specific values | for i in range(2, 10, 3):</br></t>print(i) | 2</br>5</br>8            |

#  Data Structures
1) list
2) Tuple
3) Dict
4) Set

### list
1) list is a comma separated values with in the square brackets "[]".
2) list is used to store multiple items in a single variable.
3) list is ordered, mutable(changeable), duplicates allowed.

ex. Create a list variable
```python
thislist = ['apple', 'banana', 'cherry']
print(thislist)
```
Output:
```output
['apple', 'banana', 'cherry']
```
- we can do indexing with list like arrays and list index start with 0, 1, 2, 3...so on
  - apple = [1]
  - banana = [2]
  - cherry = [3]
  - ...
  - ...

- allow duplicates : 
```python
thislist = ['apple', 'banana', 'cherry', 'apple', 'banana']
print(thislist)
```
Output:
```output
['apple', 'banana', 'cherry', 'apple', 'banana']
```

#### How `len()` work with a list??
len()—how many items in a list

```python
thislist = ['apple', 'banana', 'cherry']
print(len(thislist))
```
Output
```output
3
```

#### A list can contain different data types:
```python
thislist = ['apple', 2, True, 30, 'cherry']
print(type(thislist))
```
Output
```Output
<class 'list'>
```

#### how `list()` works in python??
```python
thislist = list(("apple", "banana", "cherry"))
print(thislist)
```
Output
```output
['apple', 'banana', 'cherry']
```

| Note: as we know, we can access list items with the help of indexing and slicling |
|-----------------------------------------------------------------------------------|

### Access items

- access with indexing
  - The first item has index 0.
```python
thislist = ['apple', 'banana', 'cherry']
print(thislist[1])
```
Output
```python
banana
```
- negative indexing 
  - negative indexing means start with an end.
  - -1 refers to the _last item of the list_, then -2, -3, ... so on.

```python
thistlist = ['apple', 'banana', 'cherry']
print(thistlist[-1])
```
Output:
```python
cherry
```

#### Range of an indexing or slicing list
```python
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) # slicing start with 2 but end with 4 (5 is )
```
output
```python
['cherry','orange','kiwi']
```

```python
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4]) # start from index[0] to index[3]
```
Output
```python
['apple','banana','cherry','orange']
```

```python
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:]) # start from 2 to last item
```
Output:
```python
['cherry','orenge','kiwi','melon','mango']
```

#### Range of negative index or negative slicing
```python
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
```
output
```python
['orange','kiwi','melon']
```

#### Check if Item Exists
```python
thislist = ['apple','banana','cherry']
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list.")
```
Output
```python
Yes, 'apple' is in the fruits list.
```

| Note : List is a mutable(Changeable) and also we can change items in list. |
|----------------------------------------------------------------------------|

### Change Item Values

```python
thislist = ["Apple","Banana","Cherry"]
thislist[1] = "Blackcurrant"
print(thislist)
```
Output
```python
['Apple','Blackcurrant','Cherry']
```
### Change a range of items values
```python
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ['blackcurrant','watermelon']
print(thislist)
```
Output
```python
['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'melon', 'mango']
```
#### Change the second value by replacing it with two new values
```python
thislist = ['apple', 'banana', 'cherry']
# add 2nd index `['blackcurrant', 'watermelon']` and add cherry at 3rd index
thislist[1:2] = ['blackcurrant', 'watermelon']
print(thislist)
```
Output:
```python
['apple', 'blackcurrant', 'watermelon', 'cherry']
```

#### Change the second and third value by replacing it with one value
```python
thislist = ["apple","banana","cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
```
Output
```python
['apple','watermelon']
```

### Insert Items
- To insert a new item, without replacing any of the existing values, we can use the `insert()` method.

```python
thislist = ["apple","banana","cherry"]
thislist.insert(2, "watermelon")
print(thislist)
```
Output
```python
['apple', 'banana', 'watermelon', 'cherry']
```

### Add list items
1) `append()` :
```python
thislist = ["apple","banana","cherry"]
thislist.append("orange")
print(thislist)
```
Output
```python
['apple', 'banana', 'cherry', 'orange']
```

2) `insert()` :
```python
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
```
output
```python
['apple', 'orange', 'banana', 'cherry']
```

3) `extend()` :
```python
thislist = ["apple","banana","cherry"]
tropical = ["mango","pineapple","papaya"]
thislist.extend(tropical) # 'tropical' list added to end of the 'thislist' list
print(thislist)
```
Output
```python
['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']
```

Add any iterable :
```python
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
```
Output
```python
['apple', 'banana', 'cherry', 'kiwi', 'orange']
```

### Remove list items
1) `remove()` :
```python
thislist = ['apple', 'banana', 'cherry']
thislist.remove('banana')
print(thislist)
```
Output
```python
['apple','cherry']
```
| Note : If there are more than one item with the specified value, the remove() method removes the first occurrence |
|-------------------------------------------------------------------------------------------------------------------|

```python
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
```
Output :
```python
['apple', 'cherry', 'banana', 'kiwi']
```

2) `pop()` - remove specified index </br>
Ex.
```python
thislist = ['apple','banana','cherry']
thislist.pop(1)
print(thislist)
```
Output
```python
['apple','cherry']
```
Ex.
```python
thislist = ['apple','banana','cherry']
thislist.pop()
print(thislist)
```
Output
```python
['apple','banana']
```
3) `del` : This `del` keyword also removes the specified index.
```python
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
```
output
```python
['banana','cherry']
```

4) `del` : delete list
```python
thislist = ["apple", "banana", "cherry"]
del thislist
```

5) `clear()` : empty the list
```python
thislist = ["apple","banana","cherry"]
thislist.clear()
print(thislist)
```
Output
```python
[]
```

### for loop in a list
1) loop through a list: 
```python
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)
```
Output: 
```python
apple
banana
cherry
```
2) `range()` with `len()`
```python
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(i)
```
Output
```python
0
1
2
```
### while loop in a list
```python
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
```
output
```python
apple
banana
cherry
```
### list comprehension 
1) list comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
```python
# simple for list with if condition
fruits = ["apple","banana","cherry"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)
```
Output
```python
['apple', 'banana', 'mango']
```

Ex.
```python
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
newlist = [x for x in fruits if "a" in x]
print(newlist)
```
Output
```python
['apple', 'banana', 'mango']
```

| List comprehension syntax : <br/> newlist = [ expression for item in iterable id condition == True ] | 
|------------------------------------------------------------------------------------------------------|

2) Condition
- The condition is like a filter that only accepts the items that valuate to `true`.
```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)
```
Output
```python
['banana', 'cherry', 'kiwi', 'mango']
```
- with no `if` condition
```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]
print(newlist)
```
Output:
```python
['apple', 'banana', 'cherry', 'kiwi', 'mango']
```

3) Iterable
```python
newlist = [x for x in range(10)]
```
Output:
```
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

- Iterable with conditions
```python
newlist = [x for x in range(10) if x > 5]
print(newlist)
```
Output
```
[6, 7, 8, 9]
```

4) Expression
- The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list
```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)
```
Output
```python
['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']
```
Ex 2: You can set the outcome to whatever you like
```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]
print(newlist)
```
Output
```python
['hello', 'hello', 'hello', 'hello', 'hello']
```

Ex. 2: The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome
```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != 'banana' else "orange" for x in fruits]
print(newlist)
```
Output:
```python
['apple', 'orange', 'cherry', 'kiwi', 'mango']
```

### sort Lists
1) Sort list alphanumerically(`sort()`) :
- list objects have a `sort()` method that will sort the list alphanumerically, ascending, by default:
```python
fruits = ["orange" ,"mango", "kivi", "pineapple", "banana"]
fruits.sort()
print(fruits)
```
Output
```python
['banana', 'kivi', 'mango', 'orange', 'pineapple']
```
- With numeric values:
```python
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
```
Output
```python
[23, 50, 65, 82, 100]
```

2) sort Descending(`sort(reverse = True)`) :
```python
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
```
Output
```python
['pineapple', 'orange', 'mango', 'kiwi', 'banana']
```
3) Customize sort function :
- You can also customize your own function by using the keyword argument `key = function`
- The function will return a number that will be used to sort the list (the lowest number first):
Ex.
```python
# Define a function that calculates the absolute difference from 50
def myfunc(n):
    return abs(n - 50)

# Create a list of numbers
thislist = [100, 50, 65, 82, 23]

# Sort the list based on the absolute difference from 50
thislist.sort(key=myfunc)

# Print the sorted list
print(thislist)
```
output
```python
[50, 65, 82, 23, 100]
```
Ex 2 :
```python
# Define a function that calculates the remainder when dividing a number by 3
def remainder_mod3(n):
    return n % 3

# Create a list of numbers
numbers = [10, 21, 14, 27, 36]

# Sort the list based on the remainder when dividing each number by 3
numbers.sort(key=remainder_mod3)

# Print the sorted list
print(numbers)
```
Output:
```python
[21, 27, 36, 10, 14]
```

4) case-insensitive sort : 
- By default, the sort() method is a case sensitive, resulting in all capital letters being sorted before lower case letters
```python
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort() # first capital letter and then lower latter
print(thislist)
```
Output
```python
['Kiwi', 'Orange', 'banana', 'cherry'
```
- `str.lower`
```python
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower) # lower letters first and then capital letters
print(thislist)
```
output
```python
['banana', 'cherry', 'Kiwi', 'Orange']
```

5) Reverse Order `reverse()` :
```python
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse() # reverse order of `thislist`
print(thislist)
```
Output
```python
['cherry', 'Kiwi', 'Orange', 'banana']
```

### Copy List
1) Copy a list
- `copy()` :
```python
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
```
Output
```python
['apple', 'banana', 'cherry']
```

- `list()` :
```python
thislist = ['apple', 'banana', 'cherry']
mylist = list(thislist)
print(mylist)
```
Output
```python
['apple', 'banana', 'cherry']
```

### Join List
1) Join two lists with `+` :
```python
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
```
Output
```python
['a', 'b', 'c', 1, 2, 3]
```
2) join lists with `for` loop :
```python
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)

print(list1)
```
Output
```python
['a', 'b', 'c', 1, 2, 3]
```

3) join lists with `extend()` :
```python
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
```
Output
```python
['a', 'b', 'c', 1, 2, 3]
```
