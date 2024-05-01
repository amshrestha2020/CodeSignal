# Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
# No time to explain! The World Government made contact with intelligent alien life, and needs you to send a message to the outer space. The aliens only receive messages that are stored in a sequence of lists of sizes 0, 1, 1, 2, 3, 5, ..., in other words those whose length increase according to the Fibonacci sequence.

# The Government is too busy composing the message, and needs you to prepare the list in which the message should be sent. Given an integer n, return a list of n lists, where the first element consists is empty (consists of 0 zeros), the second element consists of 1 zero, and so on.

# Example

# For n = 6, the output should be

# solution(n) = [[], 
#                [0], 
#                [0], 
#                [0, 0], 
#                [0, 0, 0], 
#                [0, 0, 0, 0, 0]]


def solution(n):
    return [[0] * x for x in functools.reduce(lambda acc, _: acc + [acc[-1] + acc[-2]], range(2, n), [0, 1])]
