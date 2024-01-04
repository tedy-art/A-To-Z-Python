def largestElement(arr: [], n: int) -> int:
    # Write your code from here.

    for element in range(n):
        element = int(input("add : "))
        arr.append(element)
    print(f"Array : {arr}")

    largest_element = arr[0]

    for element in range(len(arr)):
        if largest_element < arr[element]:
            largest_element = arr[element]

    return largest_element


n = int(input("size of array : "))
arr = []
x = largestElement(arr, n)
print(f"largest element in current array : {x}")

