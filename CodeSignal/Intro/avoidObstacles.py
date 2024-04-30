# You are given an array of integers representing coordinates of obstacles situated on a straight line.

# Assume that you are jumping from the point with coordinate 0 to the right. You are allowed only to make jumps of the same length represented by some integer.

# Find the minimal length of the jump enough to avoid all the obstacles.

# Example

# For inputArray = [5, 3, 6, 7, 9], the output should be
# solution(inputArray) = 4.

# Check out the image below for better understanding:


def solution(inputArray):
    max_obstacle = max(inputArray)
    
    for jump_length in range(1, max_obstacle + 2):
        can_jump = all((x % jump_length != 0) for x in inputArray)
        if can_jump:
            return jump_length



