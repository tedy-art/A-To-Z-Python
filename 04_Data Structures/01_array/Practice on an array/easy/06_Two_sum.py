# class Solution:
#     def twoSum(self, nums, target):
#         seen = {}
#         for i, value in enumerate(nums):
#             remaining = target - nums[i]
#
#             if remaining in seen:
#                 return [i, seen[remaining]]
#
#             seen[value] = i
#
#
# ob = Solution()
# ob.twoSum([2, 7, 11, 15], 6)


def two_sum(nums, target):
    # Create a dictionary to store the indices of elements
    num_indices = {}

    for i, num in enumerate(nums):
        # Calculate the complement needed to reach the target
        complement = target - num

        # Check if the complement is already in the dictionary
        if complement in num_indices:
            # If found, return the indices
            return [num_indices[complement], i]

        # Otherwise, store the current element's index in the dictionary
        num_indices[num] = i

    # If no solution is found, return an empty list or handle it according to the problem requirements
    return []


# Example usage:
nums1 = [2, 7, 11, 15]
target1 = 9
print(two_sum(nums1, target1))  # Output: [0, 1]

nums2 = [3, 2, 4]
target2 = 6
print(two_sum(nums2, target2))  # Output: [1, 2]

nums3 = [3, 3]
target3 = 6
print(two_sum(nums3, target3))  # Output: [0, 1]
