"""
write a python program to find the sum of all even numbers from 1 to 50.
step 1: 1 to 50 find even numbers.
step 2: store even number in a list.
step 3: addition of even numbers.
step 4: print addition
"""
sum_of_even = 0
number = 1
even_list = []

# 1 to 50 iteration
while number <= 50:
    if number%2 == 0:
        sum_of_even += number
        even_list.append(number)
    number += 1
print(even_list)
print(sum_of_even)
