# Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
# You've come up with a really cool name for your future startup company, and already have an idea about its logo. This logo will represent a circle, with the prefix of a cyclic string formed by the company name written around it.

# The length n of the prefix you need to take depends on the size of the logo. You haven't yet decided on it, so you'd like to try out various options. Given the name of your company, return the prefix of the corresponding cyclic string containing n characters.

# Example

# For name = "nicecoder" and n = 15, the output should be
# solution(name, n) = "nicecoderniceco"


from itertools import cycle

def solution(name, n):
    gen = cycle(name)
    res = [next(gen) for _ in range(n)]
    return ''.join(res)
