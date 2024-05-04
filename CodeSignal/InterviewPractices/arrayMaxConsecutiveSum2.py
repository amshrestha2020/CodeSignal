
# Given an array of integers, find the maximum possible sum you can get from one of its contiguous subarrays. The subarray from which this sum comes must contain at least 1 element.

# Example

# For inputArray = [-2, 2, 5, -11, 6], the output should be
# solution(inputArray) = 7.

# The contiguous subarray that gives the maximum possible sum is [2, 5], with a sum of 7.



def solution(inputArray):
    # Initialize current_sum and max_sum to the first element of the array
    current_sum = max_sum = inputArray[0]

    # Iterate over the rest of the array
    for num in inputArray[1:]:
        # If current_sum is negative, discard it
        current_sum = max(num, current_sum + num)
        
        # Update max_sum if current_sum is greater
        max_sum = max(max_sum, current_sum)

    return max_sum
