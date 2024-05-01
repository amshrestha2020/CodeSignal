# Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
# As a professional and respected database programmer, you implemented a low-level API for your front-end colleagues to use. One of them, however, appeared to be quite an ungrateful exemplar, and had the nerve to criticize your work: it seems to him that the functionality your API provides is too basic, and he has to implement several additional functions on his end to make things work.

# You don't like to leave the users of your ingenious work disgruntled, so you have to update your API. It can be done quite simple: most of the high-level functionality can be added by combining several basic functions. Now you need to implement a function that will compose an arbitrary number of functions, and test it on some variable x.

# Example

# For functions = ["abs", "math.sin", "lambda x: 3 * x / 2"]
# and x = 3.1415, the output should be
# solution(functions, x) = 1.

# abs(math.sin(3 * 3.1415 / 2)) = abs(sin(4.71225)) ≈ abs(-1) = 1.


import functools


def compose(functions):
    return functools.reduce(lambda f, g: lambda x: f(g(x)), functions)

def solution(functions, x):
    return compose(map(eval, functions))(x)
