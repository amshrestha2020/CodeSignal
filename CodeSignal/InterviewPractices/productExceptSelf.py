# You have an array nums. We determine two functions to perform on nums. In both cases, n is the length of nums:

# fi(nums) = nums[0] · nums[1] · ... · nums[i - 1] · nums[i + 1] · ... · nums[n - 1]. (In other words, fi(nums) is the product of all array elements except the ithf.)
# g(nums) = f0(nums) + f1(nums) + ... + fn-1(nums).
# Using these two functions, calculate all values of f modulo the given m. Take these new values and add them together to get g. You should return the value of g modulo the given m.

# Example

# For nums = [1, 2, 3, 4] and m = 12, the output should be
# solution(nums, m) = 2.

# The array of the values of f is: [24, 12, 8, 6]. If we take all the elements modulo m, we get:
# [0, 0, 8, 6]. The sum of those values is 8 + 6 = 14, making the answer 14 % 12 = 2.


def solution(nums, m):
    n = len(nums)
    
    # Initialize arrays to store the prefix products and suffix products
    prefix_products = [1] * n
    suffix_products = [1] * n
    
    # Calculate prefix products
    for i in range(1, n):
        prefix_products[i] = (prefix_products[i - 1] * nums[i - 1]) % m
    
    # Calculate suffix products
    for i in range(n - 2, -1, -1):
        suffix_products[i] = (suffix_products[i + 1] * nums[i + 1]) % m
    
    # Calculate the sum of products
    g_value = 0
    for i in range(n):
        g_value = (g_value + prefix_products[i] * suffix_products[i]) % m
    
    return g_value

# Test case
print(solution([1, 2, 3, 4], 12))  # Output: 2
