# Sort the letters in the string s by the order they occur in the string t.

# Example

# For s = "weather" and t = "therapyw", the output should be
# solution(s, t) = "theeraw";

# For s = "good" and t = "odg", the output should be
# solution(s, t) = "oodg".

def solution(s, t):
    # Create a dictionary to store the count of each character in s
    count = {}
    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    # Create the result string
    result = ''
    for char in t:
        if char in count:
            result += char * count[char]
            del count[char]

    return result
