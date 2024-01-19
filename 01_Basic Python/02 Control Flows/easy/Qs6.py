"""
Question 6:
Write a function that takes a year as input and prints "Leap year" if it's a leap year,
 otherwise print "Not a leap year."

"""
year = 2000

if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year 1".format(year))
elif (year % 4 == 0) and (year % 100 != 0):
    print("{0} is a leap year 2".format(year))
else:
    print("{0} is not a leap year 3".format(year))