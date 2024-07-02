"""
1. Write a Python function to find the maximum of three numbers.
"""
def max_num(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        print("n1 is largest number.")
    elif n2 > n1 and n2 > n3:
        print("n2 is largest number.")
    else:
        print("n3 is largest number.")

max_num(15, 66, 7)