# Given the string, check if it is a palindrome.

def solution(inputString):
    # Compare the string with its reverse
    return inputString == inputString[::-1]

