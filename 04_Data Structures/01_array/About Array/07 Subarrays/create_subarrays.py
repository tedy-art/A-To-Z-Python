# Create subarrays from existing arrays:
original_array = [3, 7, 1, 9, 2, 5, 8]

start_index = 1
end_index = 5
subarrays = original_array[start_index: end_index+1]

print("Original Arrays : ", original_array)
print(f"subarray(from index {start_index} to {end_index}) : {subarrays}")