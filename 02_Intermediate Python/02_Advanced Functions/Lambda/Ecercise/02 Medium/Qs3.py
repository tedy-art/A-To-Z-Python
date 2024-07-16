"""
    Write a lambda function to check if a string is a palindrome.
"""

is_palindrome = lambda s: s == s[::-1]

# Example usage
result1 = is_palindrome("madam")
result2 = is_palindrome("hello")

print(result1)  # Output: True
print(result2)  # Output: False
