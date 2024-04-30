# Given a string, your task is to replace each of its characters by the next one in the English alphabet; i.e. replace a with b, replace b with c, etc (z would be replaced by a).

# Example

# For inputString = "crazy", the output should be solution(inputString) = "dsbaz".

def solution(inputString):
    result = ""
    for char in inputString:
        if char.isalpha():
            # Handle uppercase letters
            if char.isupper():
                result += chr((ord(char) - ord('A') + 1) % 26 + ord('A'))
            # Handle lowercase letters
            else:
                result += chr((ord(char) - ord('a') + 1) % 26 + ord('a'))
        else:
            result += char
    return result

