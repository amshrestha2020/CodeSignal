# You're a crossword fanatic, and have finally decided to try and create your own. However, you also love symmetry and good design, so you come up with a set of rules they should follow:

# the crossword must contain exactly four words;
# these four words should form four pairwise intersections;
# all words must be written either left-to-right or top-to-bottom;
# the area of the rectangle formed by empty cells inside the intersections isn't equal to zero.
# Given 4 words, find the number of ways to make a crossword following the above-described rules. Note that two crosswords which differ by rotation are considered different.

# Example

# For words = ["crossword", "square", "formation", "something"], the output should be
# solution(words) = 6.

# The six crosswords can be formed as shown below:

#   f                         f                             f
#   o                     c r o s s w o r d     c r o s s w o r d
# c r o s s w o r d           r   o                   q     r
#   m   q                     m   m                   u     m
#   a   u            ;  s q u a r e          ;        a     a
#   t   a                     t   t                   r     t
#   i   r                     i   h             s o m e t h i n g
# s o m e t h i n g           o   i                         o
#   n                         n   n                         n
#                                 g                               
                                                              
#     c         s               s                                      
# f o r m a t i o n       c     q               c         s          
#     o         m         r     u               r         o      
#     s q u a r e       f o r m a t i o n       o         m            
#     s         t    ;    s     r            ;  s q u a r e                  
#     w         h         s o m e t h i n g     s         t         
#     o         i         w                     w         h     
#     r         n         o                   f o r m a t i o n            
#     d         g         r                     r         n         
#                         d              


from itertools import permutations

def solution(words):
    def count(a, b, c, d):        
        La, Lb, Lc, Ld = map(len, [a, b, c, d])
        result = 0
        for x in range(2, min(La, Lb)):
            top = [(a[i], a[i+x]) for i in range(La-x)]
            bottom = [(b[i], b[i+x]) for i in range(Lb-x)]
            for y in range(2, min(Lc, Ld)):
                left = [(c[i], c[i+y]) for i in range(Lc-y)]
                right = [(d[i], d[i+y]) for i in range(Ld-y)]
                for ul, ur in top:
                    for bl, br in bottom:
                        n1 = left.count((ul, bl))
                        n2 = right.count((ur, br))
                        result += n1 * n2
        return result
    return 2 * sum(count(words[0], w1, w2, w3) + count(w1, words[0], w2, w3)
                   for w1, w2, w3 in permutations(words[1:]))

