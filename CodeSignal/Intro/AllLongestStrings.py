# Given an array of strings, return another array containing all of its longest strings.

# Example

# For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
# solution(inputArray) = ["aba", "vcd", "aba"].


def solution(inputArray):
    # Find the length of the longest strings
    max_length = max(len(s) for s in inputArray)
    
    # Filter the strings that have the maximum length
    longest_strings = [s for s in inputArray if len(s) == max_length]
    
    return longest_strings

