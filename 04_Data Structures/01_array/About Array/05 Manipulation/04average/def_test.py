def addition(arr):
    add = 0
    for element in arr:
        add += element
    return add


def average_of_array(sum_of_array, my_array):
    average = sum_of_array / len(my_array)
    return average


my_array = [3, 8, 2, 10, 5]
sum = addition(my_array)
average = average_of_array(sum, my_array)
print(f"sum of an array is : {sum},\naverage of an array is {average}")