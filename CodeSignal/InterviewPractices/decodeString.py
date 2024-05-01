# Given an encoded string, return its corresponding decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is repeated exactly k times. Note: k is guaranteed to be a positive integer.

# Note that your solution should have linear complexity because this is what you will be asked during an interview.

# Example

# For s = "4[ab]", the output should be
# solution(s) = "abababab";

# For s = "2[b3[a]]", the output should be
# solution(s) = "baaabaaa";

# For s = "z1[y]zzz2[abc]", the output should be
# solution(s) = "zyzzzabcabc".


def solution(s):
    stack = []
    current_count = 0
    current_decoded = ''

    for char in s:
        if char.isdigit():
            current_count = current_count * 10 + int(char)
        elif char == '[':
            stack.append((current_count, current_decoded))
            current_count = 0
            current_decoded = ''
        elif char == ']':
            count, prev_decoded = stack.pop()
            current_decoded = prev_decoded + current_decoded * count
        else:
            current_decoded += char

    return current_decoded

# Test cases
print(solution("4[ab]"))  # Output: "abababab"
print(solution("2[b3[a]]"))  # Output: "baaabaaa"
print(solution("z1[y]zzz2[abc]"))  # Output: "zyzzzabcabc"
