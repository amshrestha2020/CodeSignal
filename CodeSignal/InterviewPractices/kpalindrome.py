# A string is a k-palindrome if it can be transformed into a palindrome by removing any amount of characters from 0 to k. Your task is to determine whether the given string s is a k-palindrome.

# Example

# For s = "abrarbra" and k = 1, the output should be
# solution(s, k) = true.

# You can remove one letter, 'r', to obtain the string "abrarba", which is a palindrome.

# For s = "adbcdbacdb" and k = 2, the output should be
# solution(s, k) = false.



def solution(s, k):
    n = len(s)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for gap in range(1, n):
        i = 0
        for j in range(gap, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = min(dp[i][j - 1], dp[i + 1][j]) + 1
            i += 1
    return dp[0][n - 1] <= k
