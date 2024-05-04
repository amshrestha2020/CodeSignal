# Note: Come up with a linear solution, since that is what you would be asked to do in an interview.

# You have a sorted array of integers. Write a function that returns a sorted array containing the squares of those integers.

# Example

# For array = [-6, -4, 1, 2, 3, 5], the output should be
# solution(array) = [1, 4, 9, 16, 25, 36].

# The array of squared integers from array is: [36, 16, 1, 4, 9, 25]. When sorted, it becomes: [1, 4, 9, 16, 25, 36].

def solution(array):
    n = len(array)
    result = [0] * n
    left = 0
    right = n - 1
    for i in range(n - 1, -1, -1):
        if abs(array[left]) > abs(array[right]):
            result[i] = array[left] * array[left]
            left += 1
        else:
            result[i] = array[right] * array[right]
            right -= 1
    return result
