"""
Question: Write a program that counts the frequency of each word in
a given sentence using a dictionary.

"""


def word_frequency(sentence):
    # Split the sentence into a list of words
    words = sentence.split()
    print(words)

    # Initialize an empty dictionary to store word frequencies
    frequency_dict = {}

    # Iterate through each word in the list
    for word in words:
        # Remove common punctuation and convert to lowercase
        word = word.strip('.,!?"\'').lower()

        # Check if the word is already in the dictionary
        if word in frequency_dict:
            # If yes, increment the frequency
            frequency_dict[word] += 1
        else:
            # If not, add the word to the dictionary with a frequency of 1
            frequency_dict[word] = 1

    # Return the final dictionary of word frequencies
    return frequency_dict


# Example usage
sentence = "The quick brown fox jumps over the lazy dog. The dog barks, and the fox runs away."
result = word_frequency(sentence)
print(result)
