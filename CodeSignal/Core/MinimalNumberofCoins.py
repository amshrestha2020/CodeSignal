# You find yourself in Bananaland trying to buy a banana. You are super rich so you have an unlimited supply of banana-coins, but you are trying to use as few coins as possible.

# The coin values available in Bananaland are stored in a sorted array coins. coins[0] = 1, and for each i (0 < i < coins.length) coins[i] is divisible by coins[i - 1]. Find the minimal number of banana-coins you'll have to spend to buy a banana given the banana's price.

# Example

# For coins = [1, 2, 10] and price = 28, the output should be
# solution(coins, price) = 6.

# You have to use 10 twice, and 2 four times.


def solution(coins, price):
    nCoins = 0
    
    for coin in coins[::-1]:
        nCoins += price // coin
        price %= coin
    
    return nCoins
