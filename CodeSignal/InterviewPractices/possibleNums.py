# You have a collection of coins, and you know the values of the coins and the quantity of each type of coin in it. You want to know how many distinct sums you can make from non-empty groupings of these coins.

# Example

# For coins = [10, 50, 100] and quantity = [1, 2, 1], the output should be
# solution(coins, quantity) = 9.

# Here are all the possible sums:

# 50 = 50;
# 10 + 50 = 60;
# 50 + 100 = 150;
# 10 + 50 + 100 = 160;
# 50 + 50 = 100;
# 10 + 50 + 50 = 110;
# 50 + 50 + 100 = 200;
# 10 + 50 + 50 + 100 = 210;
# 10 = 10;
# 100 = 100;
# 10 + 100 = 110.
# As you can see, there are 9 distinct sums that can be created from non-empty groupings of your coins.


def solution(coins, quantity):
    # Initialize a set to store the possible sums
    sums = set()
    # Add 0 to the set initially
    sums.add(0)
    
    # Iterate through each coin and quantity
    for coin, qty in zip(coins, quantity):
        # Initialize a set to store new sums
        new_sums = set()
        # Iterate through each sum in the current set
        for s in sums:
            # Generate new sums by adding multiples of the current coin value
            for i in range(1, qty + 1):
                new_sums.add(s + i * coin)
        # Update the main set with new sums
        sums.update(new_sums)
    
    # Return the number of distinct sums
    return len(sums) - 1  # Exclude 0 since it's not a valid sum

# Test cases
print(solution([10, 50, 100], [1, 2, 1]))  # Output: 9
