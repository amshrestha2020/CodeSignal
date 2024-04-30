# Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.

# Example

# For inputArray = [2, 4, 1, 0], the output should be
# solution(inputArray) = 3.

def solution(inputArray):
    max_difference = 0
    
    for i in range(len(inputArray) - 1):
        difference = abs(inputArray[i] - inputArray[i + 1])
        max_difference = max(max_difference, difference)
    
    return max_difference

