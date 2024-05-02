# In the Land Of Chess, bishops don't really like each other. In fact, when two bishops happen to stand on the same diagonal, they immediately rush towards the opposite ends of that same diagonal.

# Given the initial positions (in chess notation) of two bishops, bishop1 and bishop2, calculate their future positions. Keep in mind that bishops won't move unless they see each other along the same diagonal.

# Example

# For bishop1 = "d7" and bishop2 = "f5", the output should be
# solution(bishop1, bishop2) = ["c8", "h3"].



# For bishop1 = "d8" and bishop2 = "b5", the output should be
# solution(bishop1, bishop2) = ["b5", "d8"].

# The bishops don't belong to the same diagonal, so they don't move.


def solution(bishop1, bishop2):
    x1, y1 = ord(bishop1[0]) - 97, int(bishop1[1]) - 1
    x2, y2 = ord(bishop2[0]) - 97, int(bishop2[1]) - 1
    
    # Check if the bishops are on the same diagonal
    if x1 - x2 != 0 and (y1 - y2) / (x1 - x2) in [-1, 1]:
        m = (y1 - y2) / (x1 - x2)
        t = int(y1 - m * x1)
        
        if m == -1:
            if t < 8:
                return ['a' + str(t + 1), chr(97 + t) + '1']
            else:
                return [chr(t + 90) + '8', 'h' + str(t - 6)]
        elif m == 1:
            if t > -1:
                return ['a' + str(t + 1), chr(104 - t) + '8']
            else:
                return [chr(97 - t) + '1', 'h' + str(t + 8)]
    
    return sorted([bishop1, bishop2])