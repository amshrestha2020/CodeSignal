# Define an integer's roundness as the number of trailing zeroes in it.

# Given an integer n, check if it's possible to increase n's roundness by swapping some pair of its digits.

# Example

# For n = 902200100, the output should be
# solution(n) = true.

# One of the possible ways to increase roundness of n is to swap digit 1 with digit 0 preceding it: roundness of 902201000 is 3, and roundness of n is 2.

# For instance, one may swap the leftmost 0 with 1.

# For n = 11000, the output should be
# solution(n) = false.

# Roundness of n is 3, and there is no way to increase it.

def solution(n):
    # Convert integer to string for easier manipulation
    n_str = str(n)
    
    # Find the rightmost non-zero digit
    rightmost_non_zero_index = len(n_str) - 1
    while rightmost_non_zero_index >= 0 and n_str[rightmost_non_zero_index] == '0':
        rightmost_non_zero_index -= 1
    
    # Check if there is at least one zero digit to the left of the rightmost non-zero digit
    for i in range(rightmost_non_zero_index):
        if n_str[i] == '0':
            return True  # Roundness can be increased by swapping
    return False  # Roundness cannot be increased
