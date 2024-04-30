# Define a word as a sequence of consecutive English letters. Find the longest word from the given string.

# Example

# For text = "Ready, steady, go!", the output should be
# solution(text) = "steady".


import re

def solution(text):
    words = re.findall(r'\b[a-zA-Z]+\b', text)
    longest_word = max(words, key=len, default="")
    return longest_word

