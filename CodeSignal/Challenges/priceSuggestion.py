# When a customer submits a job request on Thumbtack, this information is sent to Pros in the area who might be interested in it. If it looks like there's a fit, a Pro can respond with a custom quote that includes a personal message and a price estimate.

# Thumbtack tries to help Pros pick a price estimate range using historical contractData, which contains prices for the same job type in the same area. You have been asked to implement the following two-step price suggestion algorithm:

# In the first step, contractData, which is guaranteed to have an even length, is sorted and divided into two groups:
# the first group contains the first half of the elements in contractData.
# the second group contains the other half;
# In the second step, the median values of the first and the second groups are found:
# the median of the first group is rounded down and returned as the lower price bound;
# the median of the second group is rounded up and returned as the upper price bound.
# If the data is insufficient (i.e. contractData contains fewer than 2 elements), a suggestion cannot be made, so nothing should be returned.
# Using the given contractData, find the lower and the upper bounds of the suggested price estimate range.

# Example

# For contractData = [10, 15, 14, 7, 11, 15], the output should be
# solution(contractData) = [10, 15].
# The first step produces groups [7, 10, 11] and [14, 15, 15];
# The second step returns 10 and 15.
# For contractData = [], the output should be
# solution(contractData) = [].
# Input/Output

# [execution time limit] 4 seconds (py3)

# [memory limit] 1 GB

# [input] array.integer contractData

# A list of prices for the same job type in the same area that's guaranteed to have an even length.

# Guaranteed constraints:
# 0 ≤ contractData.length ≤ 8,
# 1 ≤ contractData[i] ≤ 200.

# [output] array.integer

# Array of two elements denoting the suggested price range, or an empty array if the given data is insufficient.

# [Python 3] Syntax Tips

# # Prints help message to the console
# # Returns a string
# def helloWorld(name):
#     print("This prints to the console when you Run Tests")
#     return "Hello, " + name

import math

def solution(contractData):
    # If the data is insufficient
    if len(contractData) < 2:
        return []
    
    # Sort the contractData
    contractData.sort()
    
    # Divide the data into two groups
    mid = len(contractData) // 2
    first_group = contractData[:mid]
    second_group = contractData[mid:]
    
    # Find the median of the first group (lower price bound)
    lower_bound = math.floor((first_group[mid//2 - 1] + first_group[mid//2]) / 2) if mid % 2 == 0 else first_group[mid//2]
    
    # Find the median of the second group (upper price bound)
    upper_bound = math.ceil((second_group[mid//2 - 1] + second_group[mid//2]) / 2) if mid % 2 == 0 else second_group[mid//2]
    
    return [lower_bound, upper_bound]

