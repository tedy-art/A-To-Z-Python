original_array = [11, 22, 33, 44, 55, 66, 77]

subarrays_start = 0
subarray_end = 2
subarray = []

for i in range(subarrays_start, subarray_end+1):
    subarray.append(original_array[i])

print("Original array : ", original_array)
print(f"Subarray(first three element): {subarray}")