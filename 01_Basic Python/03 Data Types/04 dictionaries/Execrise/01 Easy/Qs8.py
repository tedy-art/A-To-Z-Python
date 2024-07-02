"""
Question: Create a function that takes a list of dictionaries and
returns a new dictionary with the union of all key-value pairs.

todo:
    1) function : merge_dictionaries(arguments)
    2) arguments : 1) list of dictionaries
                list_of_dicts = [
                    {'apple': 3, 'banana': 2, 'orange': 5},
                    {'banana': 1, 'grape': 4, 'kiwi': 2},
                    {'orange': 3, 'kiwi': 1, 'melon': 6}
                ]
    3) return a new dictionary
            dictionary = {
                    'apple': 3, 'banana': 2, 'orange': 5,
                    'banana': 1, 'grape': 4, 'kiwi': 2,
                    'orange': 3, 'kiwi': 1, 'melon': 6
            }
    4) function do :
        1) create a empty dictionary
        2) use for to iterate all dictionaries in list
        3) update dictionary : add iterated dictionary in empty dictionary
"""
def merge_dictionaries(list_of_dicts):
    new_dictionary = {}
    for dictionary in list_of_dicts:
        new_dictionary.update(dictionary)
    return new_dictionary


list_of_dicts = [
    {'apple': 3, 'banana': 2, 'orange': 5},
    {'banana': 1, 'grape': 4, 'kiwi': 2},
    {'orange': 3, 'kiwi': 1, 'melon': 6}
]

x = merge_dictionaries(list_of_dicts)
print(x)
