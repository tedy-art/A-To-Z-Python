"""
3. Write a Python program to get the largest number from a list.
"""

# numbers = [10, 21, 100, 14, 27, 36]
# numbers.sort()
# print(numbers[-1])

# Example list of numbers
number_list = [10, 21, 100, 14, 27, 36]

# Initialize largest_number with 0
largest_number = 0  # modified line

# Iterate through the list to find the largest number
for number in number_list:
    # Update largest_number if the current number is greater
    if number > largest_number:
        largest_number = number

# Check if the list is not empty
if largest_number != 0:  # modified line
    print(f"The largest number is: {largest_number}")
else:
    print("The list is empty")
