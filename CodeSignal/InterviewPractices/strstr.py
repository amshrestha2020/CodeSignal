# Avoid using built-in functions to solve this challenge. Implement them yourself, since this is what you would be asked to do during a real interview.

# Implement a function that takes two strings, s and x, as arguments and finds the first occurrence of the string x in s. The function should return an integer indicating the index in s of the first occurrence of x. If there are no occurrences of x in s, return -1.

# Example

# For s = "CodefightsIsAwesome" and x = "IA", the output should be
# solution(s, x) = -1;
# For s = "CodefightsIsAwesome" and x = "IsA", the output should be
# solution(s, x) = 10.

def preprocess_pattern(pattern):
    n = len(pattern)
    prefix_suffix_lengths = [0] * n
    length = 0
    i = 1
    
    while i < n:
        if pattern[i] == pattern[length]:
            length += 1
            prefix_suffix_lengths[i] = length
            i += 1
        else:
            if length != 0:
                length = prefix_suffix_lengths[length - 1]
            else:
                prefix_suffix_lengths[i] = 0
                i += 1
                
    return prefix_suffix_lengths

def solution(s, x):
    m = len(x)
    n = len(s)
    
    if m > n:
        return -1
    
    # Preprocess the pattern to get prefix-suffix lengths
    prefix_suffix_lengths = preprocess_pattern(x)
    
    # Initialize variables
    i, j = 0, 0
    
    # Iterate through string s
    while i < n:
        if x[j] == s[i]:
            i += 1
            j += 1
            
            # If the pattern is fully matched, return the starting index
            if j == m:
                return i - j
        else:
            # If there is a mismatch, update the j index using the prefix-suffix lengths
            if j != 0:
                j = prefix_suffix_lengths[j - 1]
            else:
                i += 1
    
    return -1

# Test cases
print(solution("CodefightsIsAwesome", "IA"))  # Output: -1
print(solution("CodefightsIsAwesome", "IsA"))  # Output: 10
