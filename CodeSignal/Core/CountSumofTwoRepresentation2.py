# Given integers n, l and r, find the number of ways to represent n as a sum of two integers A and B such that l ≤ A ≤ B ≤ r.

# Example

# For n = 6, l = 2, and r = 4, the output should be
# solution(n, l, r) = 2.

# There are just two ways to write 6 as A + B, where 2 ≤ A ≤ B ≤ 4: 6 = 2 + 4 and 6 = 3 + 3.

def solution(n, l, r):
    if 2 * r < n or 2 * l > n:
        return 0
    min_val = max(l, n - r)
    max_val = min(r, n - l)
    mid_val = (max_val + min_val) // 2
    return mid_val - min_val + 1

# Example usage
n = 6
l = 2
r = 4
result = solution(n, l, r)
print(f"The number of valid ways to represent {n} is: {result}")
