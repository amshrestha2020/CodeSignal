# Given an integer product, find the smallest positive (i.e. greater than 0) integer the product of whose digits is equal to product. If there is no such integer, return -1 instead.

# Example

# For product = 12, the output should be
# solution(product) = 26;
# For product = 19, the output should be
# solution(product) = -1.

def solution(product):
   # If product is 0, return 10 (smallest positive integer with product 0)
    if product == 0:
        return 10
    
    # If product is 1, return 1 (smallest positive integer with product 1)
    if product == 1:
        return 1
    
    # Initialize an empty list to store the digits
    digits = []
    
    # Find the digits that multiply to the product
    for i in range(9, 1, -1):
        while product % i == 0:
            digits.append(i)
            product //= i
    
    # If product is not 1, no valid integer can be formed
    if product != 1:
        return -1
    
    # Construct the smallest number using the digits
    result = 0
    while digits:
        result = result * 10 + digits.pop()
    
    return result