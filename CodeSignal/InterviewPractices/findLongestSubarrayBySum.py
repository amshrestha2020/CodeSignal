# You have an unsorted array arr of non-negative integers and a number s. Find a longest contiguous subarray in arr that has a sum equal to s. Return two integers that represent its inclusive bounds. If there are several possible answers, return the one with the smallest left bound. If there are no answers, return [-1].

# Your answer should be 1-based, meaning that the first position of the array is 1 instead of 0.

# Example

# For s = 12 and arr = [1, 2, 3, 7, 5], the output should be
# solution(s, arr) = [2, 4].

# The sum of elements from the 2nd position to the 4th position (1-based) is equal to 12: 2 + 3 + 7.

# For s = 15 and arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], the output should be
# solution(s, arr) = [1, 5].

# The sum of elements from the 1st position to the 5th position (1-based) is equal to 15: 1 + 2 + 3 + 4 + 5.

# For s = 15 and arr = [1, 2, 3, 4, 5, 0, 0, 0, 6, 7, 8, 9, 10], the output should be
# solution(s, arr) = [1, 8].

# The sum of elements from the 1st position to the 8th position (1-based) is equal to 15: 1 + 2 + 3 + 4 + 5 + 0 + 0 + 0.


def solution(s, arr):
    # Initialize the left and right pointers
    left = 0
    right = 0

    # Initialize the current sum and the maximum length
    current_sum = 0
    max_length = -1
    result = [-1]

    # Iterate over the array
    while right < len(arr):
        # Add the current element to the current sum
        current_sum += arr[right]

        # While the current sum is greater than s, move the left pointer to the right
        while current_sum > s:
            current_sum -= arr[left]
            left += 1

        # If the current sum is equal to s and the current length is greater than the maximum length
        if current_sum == s and right - left + 1 > max_length:
            max_length = right - left + 1
            result = [left + 1, right + 1]  # Convert to 1-based index

        # Move the right pointer to the right
        right += 1

    return result
