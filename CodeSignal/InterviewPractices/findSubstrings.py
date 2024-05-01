# You have two arrays of strings, words and parts. Return an array that contains the strings from words, modified so that any occurrences of the substrings from parts are surrounded by square brackets [], following these guidelines:

# If several parts substrings occur in one string in words, choose the longest one. If there is still more than one such part, then choose the one that appears first in the string.

# Example

# For words = ["Apple", "Melon", "Orange", "Watermelon"] and parts = ["a", "mel", "lon", "el", "An"], the output should be
# solution(words, parts) = ["Apple", "Me[lon]", "Or[a]nge", "Water[mel]on"].

# While "Watermelon" contains three substrings from the parts array, "a", "mel", and "lon", "mel" is the longest substring that appears first in the string.



class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

def add_word(root, word):
    node = root
    for letter in word:
        if letter not in node.children:
            node.children[letter] = TrieNode()
        node = node.children[letter]
    node.is_end = True

def find_part(word, root):
    node = root
    length = 0
    for i, letter in enumerate(word):
        if letter not in node.children:
            return length
        node = node.children[letter]
        if node.is_end:
            length = i + 1
    return length

def solution(words, parts):
    root = TrieNode()
    for part in parts:
        add_word(root, part)

    for i, word in enumerate(words):
        max_length = 0
        max_part = ''
        for j in range(len(word)):
            part_length = find_part(word[j:], root)
            if part_length > max_length:
                max_length = part_length
                max_part = word[j:j+max_length]
        if max_part:
            words[i] = word.replace(max_part, '[' + max_part + ']', 1)
    return words
