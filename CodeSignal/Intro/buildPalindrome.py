# Given a string, find the shortest possible string which can be achieved by adding characters to the end of initial string to make it a palindrome.

# Example

# For st = "abcdc", the output should be
# solution(st) = "abcdcba".

def solution(st):
    # Check if the string is already a palindrome
    if st == st[::-1]:
        return st

    # Find the longest suffix that is a palindrome
    for i in range(len(st)):
        if st[i:] == st[i:][::-1]:
            # Append the remainder of the string in reverse
            return st + st[:i][::-1]


