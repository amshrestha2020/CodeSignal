# Yesterday you found some shoes in the back of your closet. Each shoe is described by two values:

# type indicates if it's a left or a right shoe;
# size is the size of the shoe.
# Your task is to check whether it is possible to pair the shoes you found in such a way that each pair consists of a right and a left shoe of an equal size.

# Example

# For

# shoes = [[0, 21], 
#          [1, 23], 
#          [1, 21], 
#          [0, 23]]
# the output should be
# solution(shoes) = true;

# For

# shoes = [[0, 21], 
#          [1, 23], 
#          [1, 21], 
#          [1, 23]]
# the output should be
# solution(shoes) = false.


def solution(shoes):
    seen_shoes = {}

    for type, size in shoes:
        if size not in seen_shoes:
            seen_shoes[size] = [0, 0]

        seen_shoes[size][type] += 1

    for size in seen_shoes:
        if seen_shoes[size][0] != seen_shoes[size][1]:
            return False

    return True
