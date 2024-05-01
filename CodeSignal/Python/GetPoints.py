# Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
# A new scoring system was introduced in your university: from now on, each test will consist of the predefined list of questions, and for the ith (1-based) question a student either gets i points, or loses p points as a penalty.

# Your task is to calculate the number of points a student got for some test. Implement a function that would calculate the number of points received for the test based on the given list of answers.

# Example

# For answers = [true, true, false, true]and p = 2, the output should be
# solution(answers, p) = 5.

# Here's why: 1 + 2 - 2 + 4 = 5.

def solution(answers, p):
    questionPoints = lambda i, ans: i + 1 if ans else -p

    res = 0
    for i, ans in enumerate(answers):
        res += questionPoints(i, ans)
    return res
