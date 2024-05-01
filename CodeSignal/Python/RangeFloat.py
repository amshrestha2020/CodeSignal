# Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
# An you may know, the range function in Python allows coders to iterate over elements from start to stop with the given step. Unfortunately it works only for integer values, and additional libraries should be used if a programmer wants to use float values.

# CodeSignal doesn't include third-party libraries, so you have to make do with the standard ones. Given array of arguments args, return array of values the float range generator should return.

# Example

# For args = [5], the output should be
# solution(args) = [0, 1, 2, 3, 4].

# Since args contains only one element, it corresponds to the stop argument. start and step arguments have default parameters, which are 0 and 1, respectively.

# For args = [0.5, 7.5], the output should be
# solution(args) = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5].

# There are only two elements in args, which means that the first value corresponds to start, and the second value corresponds to stop. The step argument thus has a default value, which is 1.

# For args = [-1.1, 2.4, 0.3], the output should be
# solution(args) = [-1.1, -0.8, -0.5, -0.2, 0.1, 0.4, 0.7, 1, 1.3, 1.6, 1.9, 2.2].

# Since args contains all three elements, the values of start, stop and step are -1.1, 2.4 and 0.3, respectively.


class FRange(object):
    def __init__(self, start, stop=None, step=None):
        if stop is None:
            self.i = 0
            self.stop = start
            self.step = 1
        elif step is None:
            self.i = start
            self.stop = stop
            self.step = 1
        else:
            self.i = start
            self.stop = stop
            self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if (self.step > 0 and self.i >= self.stop) \
        or (self.step < 0 and self.i <= self.stop):
            raise StopIteration
        else:
            i = self.i
            self.i += self.step
            return i


def solution(args):
    return list(FRange(*args))
