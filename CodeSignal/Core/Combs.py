# Miss X has only two combs in her possession, both of which are old and miss a tooth or two. She also has many purses of different length, in which she carries the combs. The only way they fit is horizontally and without overlapping. Given teeth' positions on both combs, find the minimum length of the purse she needs to take them with her.

# It is guaranteed that there is at least one tooth at each end of the comb.
# It is also guaranteed that the total length of two strings is smaller than 32.
# Note, that the combs can not be rotated/reversed.

# Example

# For comb1 = "*..*" and comb2 = "*.*", the output should be
# solution(comb1, comb2) = 5.

# Although it is possible to place the combs like on the first picture, the best way to do this is either picture 2 or picture 3.


def solution(comb1, comb2):
    i = 0
    j = 0
    a = convert_to_binary(comb1)
    b = convert_to_binary(comb2)

    while (a << i) & b:
        i += 1
    while (b << j) & a:
        j += 1

    return min(
        max(len(comb1) + i, len(comb2)),
        max(len(comb2) + j, len(comb1))
    )

def convert_to_binary(comb):
    return int(comb.replace('*', '1').replace('.', '0'), 2)
