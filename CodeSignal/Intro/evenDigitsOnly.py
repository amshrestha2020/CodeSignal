# Check if all digits of the given integer are even.

# Example

# For n = 248622, the output should be
# solution(n) = true;
# For n = 642386, the output should be
# solution(n) = false.

def solution(n):
    # Convert the integer to a string to iterate through its digits
    str_n = str(n)
    
    # Check if all digits are even
    return all(int(digit) % 2 == 0 for digit in str_n)

