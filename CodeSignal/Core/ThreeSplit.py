# You have a long strip of paper with integers written on it in a single line from left to right. You wish to cut the paper into exactly three pieces such that each piece contains at least one integer and the sum of the integers in each piece is the same. You cannot cut through a number, i.e. each initial number will unambiguously belong to one of the pieces after cutting. How many ways can you do it?

# It is guaranteed that the sum of all elements in the array is divisible by 3.

# Example

# For a = [0, -1, 0, -1, 0, -1], the output should be
# solution(a) = 4.

# Here are all possible ways:

# [0, -1] [0, -1] [0, -1]
# [0, -1] [0, -1, 0] [-1]
# [0, -1, 0] [-1, 0] [-1]
# [0, -1, 0] [-1] [0, -1]


def solution(a):
    goal = sum(a)/3
    result = currentSum = temp = 0
    
    for i in range(len(a) - 1):
        currentSum += a[i]

        if currentSum == goal:
            temp += 1
        
        if currentSum == 2 * goal:
            result += temp
            if goal == 0:
                result -= 1
    
    return result

