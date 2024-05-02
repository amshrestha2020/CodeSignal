# You have k apple boxes full of apples. Each square box of size m contains m × m apples. You just noticed two interesting properties about the boxes:

# The smallest box is size 1, the next one is size 2,..., all the way up to size k.
# Boxes that have an odd size contain only yellow apples. Boxes that have an even size contain only red apples.
# Your task is to calculate the difference between the number of red apples and the number of yellow apples.

# Example

# For k = 5, the output should be
# solution(k) = -15.

# There are 1 + 3 * 3 + 5 * 5 = 35 yellow apples and 2 * 2 + 4 * 4 = 20 red apples, making the answer 20 - 35 = -15.

def solution(k):
    yellow_apples = 0
    red_apples = 0
    
    # Iterate through box sizes from 1 to k
    for size in range(1, k + 1):
        # Calculate the number of apples in the current box
        apples_in_box = size * size
        
        # Add the apples to the corresponding color count
        if size % 2 == 1:  # Odd size box (yellow apples)
            yellow_apples += apples_in_box
        else:  # Even size box (red apples)
            red_apples += apples_in_box
    
    # Calculate the difference between red and yellow apples
    difference = red_apples - yellow_apples
    
    return difference
