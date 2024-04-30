# Correct variable names consist only of English letters, digits and underscores and they can't start with a digit.

# Check if the given string is a correct variable name.

# Example

# For name = "var_1__Int", the output should be
# solution(name) = true;
# For name = "qq-q", the output should be
# solution(name) = false;
# For name = "2w2", the output should be
# solution(name) = false.


def solution(name):
    # Check if the string is a valid variable name
    return name.isidentifier()
