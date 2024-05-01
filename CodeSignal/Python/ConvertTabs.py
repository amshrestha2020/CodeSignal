# Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
# You found an awesome customizable Python IDE that has almost everything you'd like to see in your working environment. However, after a couple days of coding you discover that there is one important feature that this IDE lacks: it cannot convert tabs to spaces. Luckily, the IDE is easily customizable, so you decide to write a plugin that would convert all tabs in the code into the given number of whitespace characters.

# Implement a function that, given a piece of code and a positive integer x will turn each tabulation character in code into x whitespace characters.

# Example

# For code = "\treturn False" and x = 4, the output should be

# solution(code, x) = "    return False"

def solution(code, x):
    return code.replace('\t', ' ' * x)
