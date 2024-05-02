# Check whether the given string is a subsequence of the plaintext alphabet.

# Example

# For s = "effg", the output should be
# solution(s) = false;
# For s = "cdce", the output should be
# solution(s) = false;
# For s = "ace", the output should be
# solution(s) = true;
# For s = "bxz", the output should be
# solution(s) = true.

def solution(s):
    return s == ''.join(sorted(set(s)))
