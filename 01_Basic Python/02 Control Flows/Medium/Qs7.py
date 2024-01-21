"""
Question 7:
Write a function that takes a month as input and prints the number of days in that
month. Assume a non-leap year.
"""


def days_in_month(month):
    # Dictionary mapping month names to their respective days
    days_in_month_dict = {
        'january': 31, 'february': 28, 'march': 31,
        'april': 30, 'may': 31, 'june': 30,
        'july': 31, 'august': 31, 'september': 30,
        'october': 31, 'november': 30, 'december': 31
    }

    # Convert input to lowercase for case-insensitive comparison
    month_lower = month.lower()

    # Check if the input month is valid
    if month_lower in days_in_month_dict:
        return days_in_month_dict[month_lower]
    else:
        return "Invalid month"


# Example usage
input_month = input("Enter a month: ")
result = days_in_month(input_month)

print(result)
