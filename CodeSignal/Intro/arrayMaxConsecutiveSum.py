# Given array of integers, find the maximal possible sum of some of its k consecutive elements.

# Example

# For inputArray = [2, 3, 5, 1, 6] and k = 2, the output should be
# solution(inputArray, k) = 8.
# All possible sums of 2 consecutive elements are:

# 2 + 3 = 5;
# 3 + 5 = 8;
# 5 + 1 = 6;
# 1 + 6 = 7.
# Thus, the answer is 8.

def solution(inputArray, k):
    n = len(inputArray)

    # Initialize the initial sum for the first subarray of length k
    current_sum = sum(inputArray[:k])
    max_sum = current_sum

    # Slide the window through the array
    for i in range(k, n):
        # Update the current sum by removing the leftmost element and adding the rightmost element
        current_sum = current_sum - inputArray[i - k] + inputArray[i]
        max_sum = max(max_sum, current_sum)

    return max_sum

