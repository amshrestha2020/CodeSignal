# Let's define digit degree of some positive integer as the number of times we need to replace this number with the sum of its digits until we get to a one digit number.

# Given an integer, find its digit degree.

# Example

# For n = 5, the output should be
# solution(n) = 0;
# For n = 100, the output should be
# solution(n) = 1.
# 1 + 0 + 0 = 1.
# For n = 91, the output should be
# solution(n) = 2.
# 9 + 1 = 10 -> 1 + 0 = 1.

def solution(n):
    def sum_of_digits(num):
        return sum(int(digit) for digit in str(num))

    digit_degree = 0

    while n >= 10:
        n = sum_of_digits(n)
        digit_degree += 1

    return digit_degree

