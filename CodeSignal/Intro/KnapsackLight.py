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
    # Initialize a 2D table for dynamic programming
    dp = [[0] * (maxW + 1) for _ in range(3)]

    for i in range(1, 3):
        for j in range(1, maxW + 1):
            # Skip the item if it exceeds the current weight capacity
            if (i == 1 and j < weight1) or (i == 2 and j < weight2):
                dp[i][j] = dp[i-1][j]
            else:
                # Take the maximum value of either skipping the item or taking the item
                dp[i][j] = max(dp[i-1][j], dp[i-1][j - weight1] + value1) if i == 1 else max(dp[i-1][j], dp[i-1][j - weight2] + value2)

    return dp[2][maxW]

