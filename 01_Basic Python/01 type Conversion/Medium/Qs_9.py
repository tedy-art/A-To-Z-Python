"""
Question 9:
Given a string "5.67", convert it to a float and round it to 2 decimal places.
"""
str_in = "5.67"
convert_float = float(str_in)
rounded_float = round(convert_float, 2)
print(f"{rounded_float} and it's type {type(rounded_float)}")