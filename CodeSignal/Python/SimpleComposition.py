# Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
# In computer science, function composition is a mechanism of combining simple functions to build more complicated ones. Here's the deal: your colleague working on the databases implemented a low-level API that you have to deal with, and there's no way for you to update it and make it more sophisticated (or simply useful). Now you need to make a function that will be able to combine low-level functions into a single one using the function composition.

# Given two functions f and g that you need to combine and a variable x, return the result of the applying the function to x, i.e. f(g(x)).

# Example

# For f = "math.log10", g = "abs", and x = -100,
# the output should be
# solution(f, g, x) = 2.

# math.log10(abs(x)) = log10(abs(-100)) = log10(100) = 2.


def compose(f, g):
    return lambda a: f(g(a))

def solution(f, g, x):
    return compose(eval(f), eval(g))(x)
