"""
Question 7:
Convert the integer 6789 to a Roman numeral string.
"""


def int_to_roman(num):
    roman_mapping = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
        100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
        10: 'X', 9: 'IX', 5: 'V', 4: 'IV',
        1: 'I'
    }

    roman_numeral = ''
    for value, symbol in roman_mapping.items():
        while num >= value:
            roman_numeral += symbol
            num -= value

    return roman_numeral


# Example usage
integer_value = 6789
roman_numeral = int_to_roman(integer_value)
print(roman_numeral)
