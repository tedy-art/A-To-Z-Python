"""
Write a lambda function to check if a string starts with a specific letter.
"""
starts_with_letter = lambda string, letter: string.startswith(letter)
first = starts_with_letter('tejas', 't')
second = starts_with_letter('hello', 'b')
print(first)
print(second)
