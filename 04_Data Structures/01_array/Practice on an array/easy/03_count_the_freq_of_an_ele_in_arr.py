def print_element_frequencies(arr):
    n = len(arr)

    # Sort the array to group identical elements together
    arr.sort()

    i = 0
    while i < n:
        # Find the frequency of the current element
        count = 1
        while i < n - 1 and arr[i] == arr[i + 1]:
            count += 1
            i += 1

        # Print the element and its frequency
        print(f"{arr[i]} {count}")

        i += 1


# Example usage
arr1 = [10, 20, 20, 10, 10, 20, 5, 20]
print_element_frequencies(arr1)
print()

arr2 = [10, 20, 20]
print_element_frequencies(arr2)
