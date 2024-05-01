# Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
# It is believed by some tribes of South Codelenica that only two events determine the person's destiny: the first time he picked a flower, and the first time he planted one. They also believe in the power of prime numbers and in the power of sums (and a bunch of other most probably unrelated stuff), so you are wondering if it has something to do with their belief in the destiny-determining events.

# You know that you first picked a flower in year a of the Codelenican calendar, and planted it in year b. Now you're curious about the sum of all the prime numbers in the range [a, b], to see if this number could possibly affect your life.

# Example

# For a = 10 and b = 20, the output should be
# solution(a, b) = 60.

# There are 4 prime numbers in the range [10, 20]: 11, 13, 17 and 19. Their sum is equal to 11 + 13 + 17 + 19 = 60. It's a round number, maybe it does mean something?..

def solution(a, b):
    return sum(filter(lambda x: all(x % i for i in range(2, int(x**0.5) + 1)), range(max(2, a), b+1)))
