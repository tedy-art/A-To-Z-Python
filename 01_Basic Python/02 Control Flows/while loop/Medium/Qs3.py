"""
Question 3:
Create a program that iterates through a list of words and prints the length
of each word using a while loop.
    sample_words = ["apple", "banana", "orange", "grape", "kiwi", "melon", "pear", "peach", "plum", "strawberry"]
"""
sample_words = ["apple", "banana", "orange", "grape", "kiwi", "melon", "pear", "peach", "plum", "strawberry"]

# Initialize variables
index = 0
word_count = len(sample_words)

# Iterate through the list and print the length of each word using a while loop
while index < word_count:
    word = sample_words[index]
    word_length = len(word)
    print(f"The length of '{word}' is: {word_length}")
    index += 1

