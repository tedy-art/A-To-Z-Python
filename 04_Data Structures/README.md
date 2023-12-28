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