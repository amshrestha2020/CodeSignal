# You are given an array of integers. On each move you are allowed to increase exactly one of its element by one. Find the minimal number of moves required to obtain a strictly increasing sequence from the input.

# Example

# For inputArray = [1, 1, 1], the output should be
# solution(inputArray) = 3.


def solution(inputArray):
    moves = 0
    prev = inputArray[0]

    for num in inputArray[1:]:
        if num <= prev:
            moves += prev - num + 1
            prev += 1
        else:
            prev = num

    return moves

