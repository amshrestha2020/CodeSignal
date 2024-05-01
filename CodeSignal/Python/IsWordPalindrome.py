# Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
# Given a word, check whether it is a palindrome or not. A string is considered to be a palindrome if it reads the same in both directions.

# Example

# For word = "aibohphobia", the output should be
# solution(word) = true;

# For word = "hehehehehe", the output should be
# solution(word) = false.

def solution(word):
    return word == word[::-1]
