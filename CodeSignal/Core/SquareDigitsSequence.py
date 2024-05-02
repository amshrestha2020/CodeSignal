# Consider a sequence of numbers a0, a1, ..., an, in which an element is equal to the sum of squared digits of the previous element. The sequence ends once an element that has already been in the sequence appears again.

# Given the first element a0, find the length of the sequence.

# Example

# For a0 = 16, the output should be
# solution(a0) = 9.

# Here's how elements of the sequence are constructed:

# a0 = 16
# a1 = 12 + 62 = 37
# a2 = 32 + 72 = 58
# a3 = 52 + 82 = 89
# a4 = 82 + 92 = 145
# a5 = 12 + 42 + 52 = 42
# a6 = 42 + 22 = 20
# a7 = 22 + 02 = 4
# a8 = 42 = 16, which has already occurred before (a0)
# Thus, there are 9 elements in the sequence.

# For a0 = 103, the output should be
# solution(a0) = 4.

# The sequence goes as follows: 103 -> 10 -> 1 -> 1, 4 elements altogether.


def solution(a0):
    
    seen = [ a0 ]
    
    while True:
        
        tsum = 0
        
        for c in str(seen[-1]):
            tsum += int(c)**2
        
        #print(seen)
        
        if tsum in seen:
            return len(seen) + 1
        else:
            seen += [ tsum ]
