# Given an array of integers nums and an integer k, determine whether there are two distinct indices i and j in the array where nums[i] = nums[j] and the absolute difference between i and j is less than or equal to k.

# Example

# For nums = [0, 1, 2, 3, 5, 2] and k = 3, the output should be
# solution(nums, k) = true.

# There are two 2s in nums, and the absolute difference between their positions is exactly 3.

# For nums = [0, 1, 2, 3, 5, 2] and k = 2, the output should be
# solution(nums, k) = false.

# The absolute difference between the positions of the two 2s is 3, which is more than k.


def solution(nums, k):
    # Create a dictionary to store the last seen index of each number
    num_index = {}
    
    # Iterate through the array
    for i, num in enumerate(nums):
        # Check if the number exists in the dictionary
        if num in num_index:
            # Calculate the absolute difference between the current index and the last seen index
            diff = i - num_index[num]
            # If the difference is less than or equal to k, return True
            if diff <= k:
                return True
        # Update the last seen index of the number
        num_index[num] = i
    
    # If no such pair is found, return False
    return False
