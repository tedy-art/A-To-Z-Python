"""
Question: Implement a function that takes a sentence and returns a dictionary
where keys are words and values are lists of indices where the word appears
"""


def word_indices(sentence):
    words = sentence.split()
    word_index_dict = {}

    for index, word in enumerate(words):
        if word in word_index_dict:
            word_index_dict[word].append(index)
        else:
            word_index_dict[word] = [index]

    return word_index_dict


sentence = "If the item is already in the inventory, it adds the quantity to the existing quantity"
result = word_indices(sentence)
print(result)