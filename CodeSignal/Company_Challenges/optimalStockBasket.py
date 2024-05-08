# You are picking a series of optimum stocks for your investment portfolio. Thankfully, you have at your disposal a tool called ACME optimizer. For each stock it provides the expected future return in 1 year, as well as the expected risk during the same period. Your goal is to implement a stock picker which will maximize the sum of expected future returns while keeping the total risk within your risk budget (riskBudget).

# Example

# For stocks = [[-1, 2], [10, 15], [11, 13], [9, 10]] and riskBudget = 30, the output should be
# solution(stocks, riskBudget) = 21.

# It's a bad idea to pick the first stock because its expected future return is negative.
# You can pick no more than two stocks from the remaining three because 15 + 13 + 10 > 30 (i.e. the total risk exceeds the risk budget if you pick all three of them). On the other hand, you can pick any pair of stocks because 15 + 13 ≤ 30, 15 + 10 ≤ 30, 13 + 10 ≤ 30.
# To maximize the sum of expected future returns according to ACME optimizer predictions you need to pick the second and third stocks (1-based). The total future return in this case equals 10 + 11 = 21.
# Input/Output

# [execution time limit] 4 seconds (py3)

# [memory limit] 1 GB

# [input] array.array.integer stocks

# stocks[i] consists of two integers: the first one corresponds to the expected future return of the ith stock in dollars, while the second one refers to the expected risk for the same stock.

# Guaranteed constraints:
# 1 ≤ stocks.length ≤ 15,
# -10 ≤ stock[i][0] ≤ 150,
# 0 < stocks[i][1] ≤ 150.

# [input] integer riskBudget

# A positive integer equal to the upper bound for the sum of the expected risks for the stocks which you can add to your portfolio.

# Guaranteed constraints:
# 5 ≤ riskBudget ≤ 100.

# [output] integer

# The maximum possible sum of the expected future returns for the stocks you can add to your portfolio.

def solution(stocks, riskBudget):
    n = len(stocks)
    # Initialize the dp table
    dp = [[0 for _ in range(riskBudget + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(riskBudget + 1):
            # If the risk of the current stock is greater than the current risk budget
            # We can't include this stock, so the answer is the same as not having this stock
            if stocks[i - 1][1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                # Else we can choose to include or not include the current stock
                # We choose the option that gives us the maximum future return
                dp[i][j] = max(dp[i - 1][j], stocks[i - 1][0] + dp[i - 1][j - stocks[i - 1][1]])
    
    # The answer is the maximum future return when we consider all stocks and have a risk budget of riskBudget
    return dp[n][riskBudget]

