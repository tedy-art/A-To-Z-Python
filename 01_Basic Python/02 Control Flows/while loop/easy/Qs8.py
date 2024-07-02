"""
Question 8:
Create a program that prints the Fibonacci sequence up to the eighth term using a
while loop.
"""
a, b = 1, 1

print(a)
print(b)

# Initialize a counter
count = 2

# Generate and print the Fibonacci sequence up to the eighth term using a while loop
while count < 8:
    # Calculate the next term
    next_term = a + b
    # Print the next term
    print(next_term)

    # Update values for the next iteration
    a, b = b, next_term

    # Increment the counter
    count += 1
