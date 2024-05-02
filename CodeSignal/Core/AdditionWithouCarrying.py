# A little child is studying arithmetic. They have just learned how to add two integers, written one below another, column by column. But the child always forgets about the important part - carrying.

# Given two integers, your task is to find the result that the child will get.

# Note: The child had learned from this site, so feel free to check it out too if you are not familiar with column addition.

# Example

# For param1 = 456 and param2 = 1734, the output should be
# solution(param1, param2) = 1180.

#    456
#   1734
# + ____
#   1180
# The child performs the following operations from right to left:

# 6 + 4 = 10 but the child forgets about carrying the 1 and just writes down the 0 in the last column
# 5 + 3 = 8
# 4 + 7 = 11 but the child forgets about the leading 1 and just writes down 1 under 4 and 7.
# There is no digit in the first number corresponding to the leading digit of the second one, so the child imagines that 0 is written before 456. Thus, they get 0 + 1 = 1.

def solution(param1, param2):
    result = ''  # Initialize the result string
    
    # Convert integers to strings to iterate through their digits
    str_param1 = str(param1)
    str_param2 = str(param2)
    
    # Initialize pointers for iterating through the digits
    i = len(str_param1) - 1
    j = len(str_param2) - 1
    
    # Iterate through the digits from right to left
    while i >= 0 or j >= 0:
        # Get the current digits or assume 0 if one integer has fewer digits
        digit1 = int(str_param1[i]) if i >= 0 else 0
        digit2 = int(str_param2[j]) if j >= 0 else 0
        
        # Calculate the sum of the digits without carrying over
        sum_digits = (digit1 + digit2) % 10
        
        # Prepend the sum to the result string
        result = str(sum_digits) + result
        
        # Move the pointers to the next digits
        i -= 1
        j -= 1
    
    return int(result)
