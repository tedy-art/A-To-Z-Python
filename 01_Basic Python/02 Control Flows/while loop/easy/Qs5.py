"""
Question 5:
Create a program that prints the reverse of a given list using a while loop.
"""
print("ways 1 :")
sample_numbers = [5, 12, 8, 20, 3, 15, 7, 10, 18, 25]
length_of_ls = len(sample_numbers)
i = 1
while i <= length_of_ls:
    print(sample_numbers[-i])
    i += 1

print()
print("ways 2 :")

sample_numbers = [5, 12, 8, 20, 3, 15, 7, 10, 18, 25]
while sample_numbers:
    print(sample_numbers.pop())
