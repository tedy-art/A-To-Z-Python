"""
Question: Write a function that takes a list of dictionaries and a key,
and returns a new list of dictionaries sorted by the specified key.

todo:
    1) function
    2) take a list of dictionary
    3) return a new dictionaries sorted by the specified key.
        1) we can sort using age
            sorted_list_of_dicts = [
                {'name': 'Charlie', 'age': 22, 'grade': 95}
                {'name': 'Eva', 'age': 24, 'grade': 92},
                {'name': 'Alice', 'age': 25, 'grade': 90},
                {'name': 'David', 'age': 28, 'grade': 88},
                {'name': 'Bob', 'age': 30, 'grade': 85},
            ]
        2) we can sort using score
            sorted_list_of_dicts = [
                {'name': 'Bob', 'age': 30, 'grade': 85},
                {'name': 'David', 'age': 28, 'grade': 88},
                {'name': 'Alice', 'age': 25, 'grade': 90},
                {'name': 'Eva', 'age': 24, 'grade': 92},
                {'name': 'Charlie', 'age': 22, 'grade': 95}
            ]

"""


def sort_list_of_dicts(list_of_dicts, sort_key):
    n = len(list_of_dicts)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if list_of_dicts[j][sort_key] < list_of_dicts[min_index][sort_key]:
                min_index = j

        # Swap the found minimum element with the first element
        list_of_dicts[i], list_of_dicts[min_index] = list_of_dicts[min_index], list_of_dicts[i]

    return list_of_dicts


students = [
    {'name': 'Alice', 'age': 25, 'grade': 90},
    {'name': 'Bob', 'age': 30, 'grade': 85},
    {'name': 'Charlie', 'age': 22, 'grade': 95},
    {'name': 'David', 'age': 28, 'grade': 88},
    {'name': 'Eva', 'age': 24, 'grade': 92}
]

sorted_students_by_grade = sort_list_of_dicts(students, 'grade')
print(sorted_students_by_grade)
