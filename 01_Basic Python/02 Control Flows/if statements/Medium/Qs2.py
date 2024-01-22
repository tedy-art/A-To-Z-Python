"""
Question 2:
Create a program that checks if a given year is a leap year,
but only if it is not a century year.
"""
year = int(input("Enter year: "))

if year % 100 != 0:
    if year % 4 == 0:
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
else:
    print(f"{year} is a century year, not checked for leap year.")
