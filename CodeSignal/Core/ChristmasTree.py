# It's Christmas time! To share his Christmas spirit with all his friends, the young Christmas Elf decided to send each of them a Christmas e-mail with a nice Christmas tree. Unfortunately, Internet traffic is very expensive in the North Pole, so instead of sending an actual image he got creative and drew the tree using nothing but asterisks ('*' symbols). He has given you the specs (see below) and your task is to write a program that will generate trees following the spec and some initial parameters.

# Here is a formal definition of how the tree should be built, but before you read it the Elf HIGHLY recommends first looking at the examples that follow:

# Each tree has a crown as follows:

#  *
#  *
# ***
# Define a line as a horizontal group of asterisks and a level as a collection of levelHeight lines stacked one on top of the other.

# Below the crown there are levelNum levels.

# The tree is perfectly symmetrical so all the middle asterisks of the lines lie on the center of the tree.

# Each line of the same level (excluding the first one) has two more asterisks than the previous one (one added to each end);

# The number of asterisks in the first line of each level is chosen as follows:

# the first line of the first level has 5 asterisks;
# the first line of each consecutive level contains two more asterisks than the first line of the previous level.
# And finally there is the tree foot which has a height of levelNum and a width of:

# levelHeight asterisks if levelHeight is odd;
# levelHeight + 1 asterisks if levelHeight is even.
# Given levelNum and levelHeight, return the Christmas tree of the young elf.

# Example

# For levelNum = 1 and levelHeight = 3, the output should be

# solution(levelNum, levelHeight) =
#     ["    *",
#      "    *",
#      "   ***",
#      "  *****",
#      " *******",
#      "*********",
#      "   ***"]
# , which represents the following tree:

#             ___
#       *        |
#       *        |-- the crown      
#      ***    ___|       
#     *****      |
#    *******     |-- level 1
#   ********* ___|
#      ***    ___|-- the foot
# For levelNum = 2 and levelHeight = 4, the output should be

# solution(levelNum, levelHeight) = 
#     ["      *", 
#      "      *", 
#      "     ***", 
#      "    *****", 
#      "   *******", 
#      "  *********", 
#      " ***********", 
#      "   *******", 
#      "  *********", 
#      " ***********", 
#      "*************", 
#      "    *****", 
#      "    *****"]
# , which represents the following tree:

#                 ___ 
#         *          |
#         *          | -- the crown
#        ***      ___|
#       *****        |
#      *******       | -- level 1
#     *********      |
#    ***********  ___|
#      *******       |
#     *********      | -- level 2
#    ***********     |
#   ************* ___|
#       *****        | -- the foot
#       *****     ___|



def solution(level_num, level_height):
    middle = level_num + level_height
    tree = [
        s := ' ' * middle + '*',
        s,
        t := ' ' * (middle - 1) + '***'
    ]
    for l in range(level_num):
        for h in range(level_height):
            tree.append(' ' * (middle - 2 - l - h) + '*' * (5 + (l + h) * 2))
    foot_width = level_height if level_height % 2 == 1 else level_height + 1
    foot = ' ' * (middle - foot_width // 2) + '*' * foot_width
    for _ in range(level_num):
        tree.append(foot)
    return tree
