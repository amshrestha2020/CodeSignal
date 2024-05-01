# Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
# The Abanamama Version System (AVS) is a software versioning and revision control system used in highly secure environments. In this system, each commit is assigned a unique name, the first part of which consists of the username encrypted in the base-4 system using symbols '0', '?', '+', and '!', and the second part consists of symbols of English alphabet.

# Given such commit, your task is go remove the username part from it and return the second part as an answer.

# Example

# For commit = "0??+0+!!someCommIdhsSt", the output should be
# solution(commit) = "someCommIdhsSt".

def solution(commit):
    return ''.join(ch for ch in commit if ch.isalpha())
