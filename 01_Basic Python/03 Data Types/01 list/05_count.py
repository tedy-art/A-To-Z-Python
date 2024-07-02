"""
5. Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
Sample List: ['abc', 'xyz', 'aba', '1221']
Expected Result: 2
"""


def match_words(words):
    ctr = 0

    # Iterate through each word in the input list 'words'
    for word in words:
        # Check if the word has a length greater than 1 and its first and last characters are the same
        if len(word) > 1 and word[0] == word[-1]:
            # If the condition is met, increment the counter 'ctr'
            ctr += 1

    # Return the final count of matching words
    return ctr


# Call the match_words function with the list ['abc', 'xyz', 'aba', '1221'] as input and print the result
print(match_words(['abc', 'xyz', 'aba', '1221']))
