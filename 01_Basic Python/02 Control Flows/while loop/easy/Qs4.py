"""
Question 4:
Implement a program that prints the even numbers from 2 to 20 using a while loop.
"""
i = 1
even = []
odd = []
while i <= 20:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)
    i += 1

print(f"even numbers : {even}")
print(f"odd numbers : {odd}")

