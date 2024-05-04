# Note: Avoid using regular expressions and implement regex matching yourself in your solution, since this is what you would be asked to do during a real interview.

# Implement regular expression matching with support for '.' and '*', given the following guidelines:
# '.' Matches any single character.
# '*' Matches zero or more of the element that comes before it.

# The matching should cover the entire input string s. If the pattern p matches the input string s, return true, otherwise return false.

# Example

# For s = "bb" and p = "b", the output should be
# solution(s, p) = false;
# For s = "zab" and p = "z.*", the output should be
# solution(s, p) = true;
# For s = "caab" and p = "d*c*x*a*b", the output should be
# solution(s, p) = true.


def solution(s, p):
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    dp[-1][-1] = True
    for i in range(len(s), -1, -1):
        for j in range(len(p) - 1, -1, -1):
            match = i < len(s) and (p[j] == s[i] or p[j] == '.')
            if j + 1 < len(p) and p[j + 1] == '*':
                dp[i][j] = dp[i][j + 2] or (match and dp[i + 1][j])
            else:
                dp[i][j] = match and dp[i + 1][j + 1]
    return dp[0][0]
