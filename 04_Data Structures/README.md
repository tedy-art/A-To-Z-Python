# Data Structure and algorithms
| sr.no | Chapters                          |
|-------|-----------------------------------|
| 1     | Introduction of DS                |
| 2     | In-built data structure in python |
| 3     | Arrays                            |
| 4     | Stack                             |
| 5     | Queue                             |
| 6     | Linked List                       |
| 7     | Binary tree                       |
| 8     | Binary search tree                |
| 9     | Graph                             |
| 10    | Hashing                           |
| 11    | Algorithm Analysis                |
| 12    | Liner and binary search           |
| 13    | Sorting                           |
| 14    | Divide approach to programming    |
| 15    | Greedy approach to programming    |
| 16    | Dynamic programming               |

# Introduction of DS

### What is a Data Structure?
- A data structure is a way of organizing and storing data to perform operations efficiently. 
- It defines the relationship between the data, the operations that can be performed on the data, and the constraints on these operations.
- Data structures can be classified into two main types:

1. **Primitive Data Structures:**
   - These are the basic building blocks and include simple data types like integers, floats, characters, and booleans.

2. **Non-Primitive Data Structures:**
   - These are more complex structures and include arrays, linked lists, stacks, queues, trees, graphs, and hash tables.

### Why Use Data Structures?

- **Efficiency:** 
  - Different data structures are designed for specific types of operations. 
  - Choosing the right data structure can significantly improve the efficiency of algorithms and operations.

- **Organization:** 
  - Data structures help in organizing and managing large amounts of data, making it easier to access, search, and manipulate.

- **Abstraction:** 
  - They provide a level of abstraction, allowing programmers to focus on high-level operations rather than low-level details of data representation.

### Common Data Structures:

1. **Arrays:**
   - A collection of elements, each identified by an index or a key.

2. **Linked Lists:**
   - Elements are stored in nodes, and each node points to the next node in the sequence.

3. **Stacks:**
   - A Last In, First Out (LIFO) structure where elements are added and removed from the same end.

4. **Queues:**
   - A First In, First Out (FIFO) structure where elements are added at the rear and removed from the front.

5. **Trees:**
   - Hierarchical data structures with nodes organized into a tree-like structure.

6. **Graphs:**
   - Collections of nodes and edges that connect pairs of nodes.

7. **Hash Tables:**
   - Data structures that use a hash function to map keys to indexes, allowing for efficient data retrieval.

### Operations on Data Structures:

- **Insertion:** Adding an element to the data structure.
- **Deletion:** Removing an element from the data structure.
- **Traversal:** Visiting all elements in a data structure.
- **Searching:** Finding the location of a specific element.
- **Sorting:** Arranging elements in a specific order.
- **Access:** Retrieving or updating the value of a specific element.

### Conclusion:

Understanding data structures is fundamental to computer science and programming. 
Choosing the right data structure for a specific task can have a significant impact on the efficiency and performance of software applications. 
As you delve deeper into programming, you'll encounter various data structures and learn how to use them effectively to solve different types of problems.

# Must Know:
Before delving into other Data Structures and Algorithms (DSA) topics, having a solid understanding of a few key time
complexities is essential. These time complexities give you a foundation for analyzing the efficiency of algorithms and 
making informed decisions about algorithm selection. 

Here are some key time complexities to focus on before moving to other DSA topics:

1. **O(1) - Constant Time:**
   - Understanding constant time complexity is crucial. 
   - It represents algorithms that have a fixed execution time, regardless of the input size. 
   - Examples include basic arithmetic operations and accessing elements in an array.

2. **O(log n) - Logarithmic Time:**
   - Logarithmic time complexity is common in algorithms that divide the problem space in half with each step. 
   - Binary search is a classic example. Understanding how algorithms with logarithmic time complexity work are foundational.

3. **O(n) - Linear Time:**
   - Linear time complexity is common in algorithms that iterate through the entire input once. 
   - Examples include linear search and simple iteration through an array.

4. **O(n log n) - Linearithmic Time:**
   - Linearithmic time complexity often appears in efficient sorting algorithms like merge sort and heapsort.
   - Understanding this complexity prepares you for more advanced sorting algorithms and divide-and-conquer strategies.

5. **O(n^2) - Quadratic Time:**
   - Quadratic time complexity is found in algorithms with nested loops. 
   - Examples include simple nested loop iterations and certain sorting algorithms like bubble sort and insertion sort.

6. **O(2^n) - Exponential Time:**
   - Exponential time complexity represents algorithms where the running time doubles with each additional element in the input. 
   - Understanding this complexity helps you identify scenarios where more efficient algorithms are needed.

Having a grasp of these time complexities will provide you with a strong foundation. 
As you explore other DSA topics, you'll likely encounter more nuanced time complexities, such as O(n!) for factorial time, 
or complexities specific to certain algorithms and data structures.

Once you are comfortable with the basics, you can gradually introduce and understand complexities associated with more 
advanced topics like dynamic programming, graph algorithms, and advanced data structures. Consistent practice, solving problems,
and applying these concepts in coding exercises will reinforce your understanding as you progress through different DSA topics.

# 2) Array
- An array is a data structure that lets us hold multiple values of the same data type. 
- Think of it as a container that holds a fixed amount of the same kind of object.
- Python makes coding easier for programmers.

### In Python, you primarily have two options for working with array-like structures:
    - the built-in `list` type 
    - the `array` module.

Here's a brief comparison:

### 1. List:
**Example:**
```python
my_list = [10, 20, 30, 40]
```

### 2. `array` Module:

**Example:**
```python
from array import array

array1 = array('i', [10, 20, 30, 40])
```

### Recommendation:

- If you need flexibility, dynamic resizing, and a rich set of methods, use the built-in `list`.

- If you have memory constraints, need to store a large amount of homogeneous data, and can benefit from more memory efficiency, consider the `array` module.

### address calculation for element access
In computer memory, 
   - the address calculation for element access in an array is typically based on the index of the element and the size of each element. 
   - The formula for calculating the memory address of an element in an array is as follows:
```python
Address of element = Base Address + (Index × Size of each element)
```
Here's a breakdown of the components:

- **Base Address:** 
  - The memory address of the first element in the array. 
  - It serves as the starting point for the array.

- **Index:** 
  - The position of the element in the array. 
  - It represents how far the element is from the first element.

- **Size of each element:** 
  - The number of memory units occupied by each element in the array. 
  - This is often expressed in bytes.

Let's illustrate this with a simple Python example:

```python
# Example array
my_array = [10, 20, 30, 40, 50]

# Assume the base address is 1000 (just for illustration purposes)
base_address = 1000

# Size of each element (assuming each element is an integer, which is 4 bytes in most systems)
element_size = 4

# Calculate the address of the third element (index 2)
index = 2
address_of_element = base_address + (index * element_size)

print(f"The address of the element at index {index} is: {address_of_element}")
```

In this example, 
   - we assume a base address of 1000 and an element size of 4 bytes. 
   - The calculation for the address of the third element (index 2) would be:
```python
Address of element=1000+(2×4)=1008
```
This illustrates how the memory address is calculated based on the index and size of each element in the array.
Keep in mind that actual memory management may involve more complexities, but this basic formula captures the essential 
concept.


## Operations in array
### 1. Insertion:

#### a. Append:
```python
my_list = [10, 20, 30, 40]

# Appending an element at the end
my_list.append(50)

print(my_list)  # Output: [10, 20, 30, 40, 50]
```

#### b. Insert at a specific index:
```python
my_list = [10, 20, 30, 40]

# Inserting an element at index 2
my_list.insert(2, 25)

print(my_list)  # Output: [10, 20, 25, 30, 40]
```

### 2. Deletion:

#### a. Remove by value:
```python
my_list = [10, 20, 30, 40]

# Removing the element with value 30
my_list.remove(30)

print(my_list)  # Output: [10, 20, 40]
```

#### b. Pop by index:
```python
my_list = [10, 20, 30, 40]

# Popping (removing and returning) the element at index 2
removed_element = my_list.pop(2)

print(my_list)         # Output: [10, 20, 40]
print(removed_element)  # Output: 30
```

### 3. Updating:

#### a. Update by index:
```python
my_list = [10, 20, 30, 40]

# Updating the element at index 1
my_list[1] = 25

print(my_list)  # Output: [10, 25, 30, 40]
```

### Swapping elements in arrays
- Swapping elements in a list or array in Python is a common operation, and you can achieve it in a few different ways. 
- Here are a couple of methods:

### Method 1: Using a Temporary Variable

```python
my_list = [10, 20, 30, 40]

# Swapping elements at positions 1 and 2
temp = my_list[1]
my_list[1] = my_list[2]
my_list[2] = temp

print(my_list)  # Output: [10, 30, 20, 40]
```

### Method 2: Without Using a Temporary Variable (Using Pythonic Swap)

```python
my_list = [10, 20, 30, 40]

# Swapping elements at positions 1 and 2 without using a temporary variable
my_list[1], my_list[2] = my_list[2], my_list[1]

print(my_list)  # Output: [10, 30, 20, 40]
```

Both methods achieve the same result, swapping the elements at positions 1 and 2 in the list.
The second method is more concise and often considered more Pythonic.

# Multi- dimensional
**2D array :**
A 2D array, also known as a matrix, is a data structure that stores elements in a grid, 
where each element is identified by two indices: a row index and a column index. 
It's essentially an array of arrays, where each inner array represents a row in the matrix.

Let's break down the key concepts of a 2D array:

### 1. **Indexing:**
   - Elements in a 2D array are accessed using two indices: one for the row and one for the column. 
   - The indices start from 0.

### 2. **Declaration and Initialization:**
   - You can declare and initialize a 2D array using nested lists (lists within lists).

   ```python
   # Example of a 2D array (3x3 matrix)
   matrix = [
       [1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]
   ]
   ```

### 3. **Accessing Elements:**
   - Accessing an element involves specifying both the row and column indices.

   ```python
   # Accessing the element in the second row and third column
   element = matrix[1][2]  # Value: 6
   ```

### 4. **Iterating Through Elements:**
   - You can use nested loops to iterate through all elements of the 2D array.

   ```python
   for row in matrix:
       for element in row:
           print(element, end=' ')
       print()
   ```

   This would print:

   ```
   1 2 3
   4 5 6
   7 8 9
   ```

### 5. **Common Operations:**
   - Common operations on 2D arrays include adding, subtracting, and multiplying matrices, as well as transposing the matrix.

   ```python
   # Transposing a matrix
   transposed_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
   ```

### Example of a 2D Array in Memory:

```
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

In memory, it might look like this:

```
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Understanding 2D arrays is essential for working with tasks that involve grids of data, such as image processing,
game development, and certain mathematical operations.

