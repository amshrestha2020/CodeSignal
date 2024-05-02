# Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
# Presented with the integer n, find the 0-based position of the second rightmost zero bit in its binary representation (it is guaranteed that such a bit exists), counting from right to left.

# Return the value of 2position_of_the_found_bit.

# Example

# For n = 37, the output should be
# solution(n) = 8.

# 3710 = 1001012. The second rightmost zero bit is at position 3 (0-based) from the right in the binary representation of n.
# Thus, the answer is 23 = 8.

def solution(n):
    return 2 ** (bin(n)[2:][::-1]).find('0', (bin(n)[2:][::-1]).find('0') + 1)