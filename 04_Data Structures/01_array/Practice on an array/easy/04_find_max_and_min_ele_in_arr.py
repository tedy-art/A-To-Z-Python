def findmaxelement(arr):
    maximum_element = arr[0]
    for element in arr:
        if maximum_element < element:
            maximum_element = element
    return maximum_element


def findminelement(arr):
    minimum_element = arr[0]
    for element in arr:
        if minimum_element > element:
            minimum_element = element
    return minimum_element


def takearr():
    size = int(input("array size : "))
    arr = []
    for _ in range(size):
        element = int(input(f"Add {_} : "))
        arr.append(element)
    return arr

x = takearr()
maximum_element = findmaxelement(x)
minimum_element = findminelement(x)
print(f"maximum element in array is {maximum_element} and minimum element in array is {minimum_element}.")
