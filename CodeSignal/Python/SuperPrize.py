# Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
# In a large and famous supermarket a new major campaign was launched. From now on, each nth customer has a chance to win a prize: a brand new luxury car! However, it's not that simple. A customer wins a prize only if the total price of their purchase is divisible by d. This number is kept as a secret, so the customers don't know in advance how much they should spend on their purchases. The winners will be announced once the campaign is over.

# Your task is to implement a function that will determine the winners. Given the purchases of some customers over time, return the 1-based indices of all the customers who won the prize, i.e. each nth who spend on their purchases amount of money divisible by d.

# Example

# For purchases = [12, 43, 13, 465, 1, 13], n = 2, and d = 3,
# the output should be
# solution(purchases, n, d) = [4].

# Each second customer has a chance to win a car, which makes customers 2, 4 and 6 potential winners. Customer number 2 spent 43 on his purchase, which is not divisible by 3. 13 also is not divisible by 3, so the sixth customer also doesn't get the price. Customer 4, however, spent 465, which is divisible by 3, so he is the only lucky guy.

class Prizes(object):
    def __init__(self, purchases, n, d):
        self.purchases = purchases
        self.n = n
        self.d = d
        self.i = n - 1

    def __iter__(self):
        return self

    def __next__(self):
        while self.i < len(self.purchases):
            i = self.i
            self.i += self.n
            if self.purchases[i] % self.d == 0:
                return i + 1
        raise StopIteration

def solution(purchases, n, d):
    return list(Prizes(purchases, n, d))
    