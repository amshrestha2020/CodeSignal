# Suppose we represent our file system as a string. For example, the string "user\n\tpictures\n\tdocuments\n\t\tnotes.txt" represents:

# user
#     pictures
#     documents
#         notes.txt    
# The directory user contains an empty sub-directory pictures and a sub-directory documents containing a file notes.txt.

# The string "user\n\tpictures\n\t\tphoto.png\n\t\tcamera\n\tdocuments\n\t\tlectures\n\t\t\tnotes.txt" represents:

# user
#     pictures
#         photo.png
#         camera
#     documents
#         lectures
#             notes.txt
# The directory user contains two sub-directories pictures and documents. pictures contains a file photo.png and an empty second-level sub-directory camera. documents contains a second-level sub-directory lectures containing a file notes.txt.

# We want to find the longest (as determined by the number of characters) absolute path to a file within our system. For example, in the second example above, the longest absolute path is "user/documents/lectures/notes.txt", and its length is 33 (not including the double quotes).

# Given a string representing the file system in this format, return the length of the longest absolute path to a file in the abstracted file system. If there is not a file in the file system, return 0.

# Notes:

# Due to system limitations, test cases use form feeds ('\f', ASCII code 12) instead of newline characters.
# File names do not contain spaces at the beginning.
# Example

# For fileSystem = "user\f\tpictures\f\tdocuments\f\t\tnotes.txt", the output should be
# solution(fileSystem) = 24.

# The longest path is "user/documents/notes.txt", and it consists of 24 characters.



def solution(fileSystem):
    fileSystem = fileSystem.split('\f')
    stack = [0]  # stack to keep track of the current path length
    max_len = 0  # maximum length seen so far

    for line in fileSystem:
        depth = line.count('\t')  # depth is number of tabs
        while len(stack) > depth + 1:  # find parent
            stack.pop()
        stack.append(stack[-1] + len(line) - depth + 1)  # remove tabs, add '/', remove '\n'

        if '.' in line:  # update max_len if it's a file
            max_len = max(max_len, stack[-1] - 1)  # remove the trailing '/'

    return max_len
