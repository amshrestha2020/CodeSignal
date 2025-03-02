# Determine if the given number is a power of some non-negative integer.

# Example

# For n = 125, the output should be
# solution(n) = true;
# For n = 72, the output should be
# solution(n) = false.

def solution(n):

    if n == 1: return True 
    for i in range(2, int(n**0.5) + 1) : 
        x = i 
  
        while x <= n: 
            x = x * i 
              
            if x == n: 
                return True
    
    return False
