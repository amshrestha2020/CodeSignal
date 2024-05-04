# Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
# Given K sorted arrays, return their sorted concatenation.

# Example

# For arrays = [[1, 3, 5], [2, 3], [2, 3, 5, 8]], the output should be
# solution(arrays) = [1, 2, 2, 3, 3, 3, 5, 5, 8].


def solution(arrays):
    firstUnused = []
    result = []
    n = 0
    for i in range(len(arrays)):
        firstUnused.append(0)
        n += len(arrays[i])
    for i in range(n):
        minIndex = -1
        minValue = 0
        for j in range(len(arrays)):
            if firstUnused[j] < len(arrays[j]):
                if minIndex == -1 or arrays[j][firstUnused[j]] < minValue:
                    minIndex = j
                    minValue = arrays[j][firstUnused[j]]
        result.append(minValue)
        firstUnused[minIndex] += 1
    return result
