"""
Question 5: Write a script that converts a string of digits to an integer (e.g., "123" to 123).
"""
get_input = input("Get string : ")
if get_input.isdigit():
    convert = int(get_input)
    print(f"convert into digit {convert} type {type(convert)}")
else:
    print("we can't convert alphabet/special symbols into integer.")
