# Given an array strings, determine whether it follows the sequence given in the patterns array. In other words, there should be no i and j for which strings[i] = strings[j] and patterns[i] ≠ patterns[j] or for which strings[i] ≠ strings[j] and patterns[i] = patterns[j].

# Example

# For strings = ["cat", "dog", "dog"] and patterns = ["a", "b", "b"], the output should be
# solution(strings, patterns) = true;
# For strings = ["cat", "dog", "doggy"] and patterns = ["a", "b", "b"], the output should be
# solution(strings, patterns) = false.


def solution(strings, patterns):
    # Create dictionaries to store mappings from string to pattern and pattern to string
    string_to_pattern = {}
    pattern_to_string = {}
    
    # Iterate through each string-pattern pair
    for string, pattern in zip(strings, patterns):
        # Check if the string is already mapped to a different pattern
        if string in string_to_pattern and string_to_pattern[string] != pattern:
            return False
        # Check if the pattern is already mapped to a different string
        if pattern in pattern_to_string and pattern_to_string[pattern] != string:
            return False
        # Update the mappings
        string_to_pattern[string] = pattern
        pattern_to_string[pattern] = string
    
    # If no inconsistencies are found, return True
    return True
