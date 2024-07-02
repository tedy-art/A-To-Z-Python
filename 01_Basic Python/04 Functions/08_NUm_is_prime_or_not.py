"""
Write a Python function that takes a number as a parameter and checks
whether the number is prime or not.
"""


def check_prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print('Number is not prime.')
                break
        else:
            print('Number is prime.')


number = int(input("Enter your number : "))
check_prime(number)
