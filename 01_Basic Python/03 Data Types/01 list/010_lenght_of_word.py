"""
10. Write a Python program to find the list of words that are longer than n from a given list of words.
"""
sample_list = ["the", "quick", "brown", "fox"]
n = 3

for word in sample_list:
    if len(word) > 3:
        print(word)