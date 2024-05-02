# Given a rectangular matrix of characters, add a border of asterisks(*) to it.

# Example

# For

# picture = ["abc",
#            "ded"]
# the output should be

# solution(picture) = ["*****",
#                      "*abc*",
#                      "*ded*",
#                      "*****"]


def solution(picture):

    newPicture = ["*" * (len(picture[0]) + 2)]
    
    for row in picture:
        newPicture.append("*" + row + "*")
        
    newPicture.append(newPicture[0])
        
    return newPicture