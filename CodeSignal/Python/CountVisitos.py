# Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
# You've launched your brand new web application not long ago, and while in beta it got beta satisfied visitors. Encouraged by such success, you decided to go ahead and push the very first stable version live.

# You know that each beta visitor spent at least k minutes on your app, so now you'd like to keep track of new visitors of your web application that spent at least k minutes on it. Given the amount of time the visitors used your application and the value of k, return the total number of users that used your app for at least k minutes including those from beta.

# Example

# For beta = 22, k = 5, and visitors = [4, 6, 6, 5, 2, 2, 5],
# the output should be
# solution(beta, k, visitors) = 26.

# 4 new visitors spent at least 5 minutes on your application, which summed up with 22 satisfied beta users gives 26.

class Counter(object):
    def __init__(self, beta): 
        self.value = beta

    def inc(self):
        self.value += 1

    def get(self):
        return self.value


def solution(beta, k, visitors):
    counter = Counter(beta)
    for visitor in visitors:
        if visitor >= k:
            counter.inc()
    return counter.get()
