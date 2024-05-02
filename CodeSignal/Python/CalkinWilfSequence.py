# Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
# The Calkin-Wilf tree is a tree in which the vertices correspond 1-for-1 to the positive rational numbers. The tree is rooted at the number 1, and any rational number expressed in simplest terms as the fraction a / b has as its two children the numbers a / (a + b) and (a + b) / b. Every positive rational number appears exactly once in the tree. Here's what it looks like:



# The Calkin-Wilf sequence is the sequence of rational numbers generated by a breadth-first traversal of the Calkin-Wilf tree, where the vertices of the same level are traversed from left to right (as displayed in the image above). The sequence thus also contains each rational number exactly once, and can be represented as follows:



# Given a rational number, your task is to return its 0-based index in the Calkin-Wilf sequence.

# Example

# For number = [1, 3], the output should be
# solution(number) = 3.

# As you can see in the image above, 1 / 3 is the 3rd 0-based number in the sequence.


def solution(number):
    def fractions():
        n, d = 1, 1
        
        while True:
            yield [n, d]
            n, d = d, 2 * (n - n % d) + d - n
            # n, d = d, 2 * (n // d) * d + d - n

    gen = fractions()
    res = 0
    while next(gen) != number:
        res += 1
    return res