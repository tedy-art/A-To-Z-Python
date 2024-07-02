"""
Question 9:
Create a program that prints the Fibonacci sequence up to the 10th term
using a for loop.
"""


# Function to generate the Fibonacci sequence up to the nth term
def fibonacci(n):
    fib_sequence = [0, 1]
    for _ in range(2, n):
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)
    return fib_sequence


# Print the Fibonacci sequence up to the 10th term
result = fibonacci(10)
print("Fibonacci sequence up to the 10th term:", result)
