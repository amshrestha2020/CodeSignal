# Given an array of strings, sort them in the order of increasing lengths. If two strings have the same length, their relative order must be the same as in the initial array.

# Example

# For

# inputArray = ["abc",
#               "",
#               "aaa",
#               "a",
#               "zz"]
# the output should be

# solution(inputArray) = ["",
#                         "a",
#                         "zz",
#                         "abc",
#                         "aaa"]


def solution(inputArray):
    length = []
    values = {}

    for string in inputArray:
        if len(string) not in values:
            values[len(string)] = []
            length.append(len(string))
        values[len(string)].append(string)

    length.sort()

    res = []
    for cur_length in length:
        res.extend(values[cur_length])

    return res
