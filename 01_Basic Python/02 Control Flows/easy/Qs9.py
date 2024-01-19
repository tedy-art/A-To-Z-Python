"""
Question 9:
Create a program that determines if a given year is a century year.
(A century year is a year that ends with '00'.)
e.g.,
100, 200, __, 1000, 1100 __
"""


def is_century_year(year):
    return year % 100 == 0


year = int(input("Enter year : "))
if is_century_year(year):
    print(f"{year} is century year.")
else:
    print(f"{year} is not century year.")
