# Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
# As you may know, the range function in Python allows coders to iterate over elements from start to stop with the given step. Unfortunately it works only for integer values, and additional libraries should be used if a programmer wants to use float values.

# CodeSignal doesn't include third-party libraries, so you have to make do with the standard ones. Given float numbers start, stop and step, your task is to return a list of values from start to stop (including start and not including stop), evenly spaced by the step.

# Values start, stop and step have at most 5 digits after the decimal point each.

# Example

# For start = -0.9, stop = 0.45, and step = 0.2,
# the output should be
# solution(start, stop, step) = [-0.9, -0.7, -0.5, -0.3, -0.1, 0.1, 0.3].



from itertools import takewhile, count

def solution(start, stop, step):
    gen = takewhile(lambda x: x < stop, count(start,step))
    return list(gen)
