# Given some integer, find the maximal number you can obtain by deleting exactly one digit of the given number.

# Example

# For n = 152, the output should be
# solution(n) = 52;
# For n = 1001, the output should be
# solution(n) = 101.

def solution(n):
    n_str = str(n)
    max_number = max(int(n_str[:i] + n_str[i+1:]) for i in range(len(n_str)))
    return max_number

