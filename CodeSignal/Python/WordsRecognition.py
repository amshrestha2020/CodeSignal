# Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
# You are working on an AI that can recognize words. To begin with, you'd like to try the following approach: for the given pair of words the AI should find two strings of sorted letters that uniquely identify these words.

# Given words word1 and word2, return an array of two strings sorted lexicographically, where the first string contains characters present only in word1, and the second string contains characters present only in word2.

# Example

# For word1 = "program" and word2 = "develop",
# the output should be
# solution(word1, word2) = ["agmr", "delv"].

# Letters 'o' and 'p' are present in both words, and other letters identify them uniquely.


def solution(word1, word2):
    def getIdentifier(w1, w2):
        return ''.join(sorted(set(w1) - set(w2)))

    return [getIdentifier(word1, word2), getIdentifier(word2, word1)]
