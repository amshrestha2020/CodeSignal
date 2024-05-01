# Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
# You've been preparing all night for the upcoming test and entered the class certain that you will ace it. Now that you received the test questions, you died inside a little: looks like you prepared for the test on a completely different topic.

# You're not even sure if you should bother to answer the questions. You still have some hope though: it is known that there's a glitch in the test preparing system, so that if the sum of digits of question ids is divisible by k, the answer to each question has a 90% probability to be an A.

# Given the list of question ids, determine if the sum of their digits is divisible by k to see if it's worth trying to pass the test.

# Example

# For ids = [529665, 909767, 644200] and k = 3, the output should be
# solution(ids, k) = true.

# The sum of digits is

# (5 + 2 + 9 + 6 + 6 + 5) + (9 + 0 + 9 + 7 + 6 + 7) + (6 + 4 + 4 + 2 + 0 + 0) = 87
# which is divisible by 3. Today is your lucky day after all!


def solution(ids, k):
    digitSum = lambda n: sum(int(digit) for digit in str(n))

    sm = 0
    for questionId in ids:
        sm += digitSum(questionId)
    return sm % k == 0
