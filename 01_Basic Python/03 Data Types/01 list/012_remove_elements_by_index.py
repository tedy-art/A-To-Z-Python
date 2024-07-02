"""
12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
Sample List: ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output: ['Green', 'White', 'Black']
"""
Sample_List = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
indices_to_remove = [0, 4, 5]

result = [Sample_List[i] for i in range(len(Sample_List)) if i not in indices_to_remove]

print(f"Original List : {Sample_List}")
print(f"altered list : {result}")