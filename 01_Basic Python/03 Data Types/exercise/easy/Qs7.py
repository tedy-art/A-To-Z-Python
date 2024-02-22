"""
Question 7: Create a function that takes a string and removes all vowels,
returning the modified string.(a, e, i, o, u sometime y)
"""


def remove_vowels(str1):
    empty_str = ''
    vowels = ['a', 'e', 'i', 'o', 'u']
    for str in str1:
        if str not in vowels:
            empty_str += str

    return empty_str


string = "don't give up"
x = remove_vowels(string)
print(x)
