# Determine whether the given string can be obtained by one concatenation of some string to itself.

# Example

# For inputString = "tandemtandem", the output should be
# solution(inputString) = true;
# For inputString = "qqq", the output should be
# solution(inputString) = false;
# For inputString = "2w2ww", the output should be
# solution(inputString) = false.

def solution(inputString):
    return inputString[:len(inputString)//2] == inputString[len(inputString)//2:]
