# Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
# Little Billy is not too good with numbers and having trouble even multiplying and adding them. He needs some practice, and you are the one helpful fellow who can give him a list of numbers to practice on. Given a list of numbers, Billy should calculate the following value:

# (((...(a[0] + a[1]) * a[2] + a[3]) * a[4] + ...)
# Unfortunately you yourself are not too good with math, but you know how to code. Implement a function that, given a list of numbers, will return the result of the operation Billy has to perform.

# Example

# For numbers = [1, 2, 3, 4, 5, 6], the output should be
# solution(numbers) = 71.

# Here's how the answer is obtained: ((1 + 2) * 3 + 4) * 5 + 6 = 71.

def solution(numbers):
    return functools.reduce(lambda a, b: a + b[1] if b[0] % 2 else a * b[1], enumerate(numbers), 1)