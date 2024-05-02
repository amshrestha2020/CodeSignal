# You found two items in a treasure chest! The first item weighs weight1 and is worth value1, and the second item weighs weight2 and is worth value2. What is the total maximum value of the items you can take with you, assuming that your max weight capacity is maxW and you can't come back for the items later?

# Note that there are only two items and you can't bring more than one item of each type, i.e. you can't take two first items or two second items.

# Example

# For value1 = 10, weight1 = 5, value2 = 6, weight2 = 4, and maxW = 8, the output should be
# solution(value1, weight1, value2, weight2, maxW) = 10.

# You can only carry the first item.

# For value1 = 10, weight1 = 5, value2 = 6, weight2 = 4, and maxW = 9, the output should be
# solution(value1, weight1, value2, weight2, maxW) = 16.

# You're strong enough to take both of the items with you.

# For value1 = 5, weight1 = 3, value2 = 7, weight2 = 4, and maxW = 6, the output should be
# solution(value1, weight1, value2, weight2, maxW) = 7.

# You can't take both items, but you can take any of them.


def solution(value1, weight1, value2, weight2, maxW):
    # Initialize the dp array
    dp = [0] * (maxW + 1)

    # Consider only the first item
    for weight in range(maxW, weight1 - 1, -1):
        dp[weight] = max(dp[weight], dp[weight - weight1] + value1)

    # Consider only the second item
    for weight in range(maxW, weight2 - 1, -1):
        dp[weight] = max(dp[weight], dp[weight - weight2] + value2)

    # Return the maximum value for the given maxW
    return dp[maxW]
