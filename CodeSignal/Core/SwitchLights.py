# N candles are placed in a row, some of them are initially lit. For each candle from the 1st to the Nth the following algorithm is applied: if the observed candle is lit then states of this candle and all candles before it are changed to the opposite. Which candles will remain lit after applying the algorithm to all candles in the order they are placed in the line?

# Example

# For a = [1, 1, 1, 1, 1], the output should be
# solution(a) = [0, 1, 0, 1, 0].

# Check out the image below for better understanding:



# For a = [0, 0], the output should be
# solution(a) = [0, 0].

# The candles are not initially lit, so their states are not altered by the algorithm.



def solution(a):
    result = [0] * len(a)
    switch = True
    
    for i in range(len(a) - 1, -1, -1):
        
        if a[i] == 1:
            switch = not switch
            
        if switch:
            result[i] = a[i]
        else:
            result[i] = 1^a[i] # flip (or 1-a[i])

    return result
