# Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
# There are some students standing in a row, each has some number written on their back. The students are about to divide into two teams by counting off by twos: those standing at the even positions (0-based) will go to team A, and those standing at the odd position will join the team B.

# Your task is to calculate the difference between the sums of numbers written on the backs of the students that will join team A, and those written on the backs of the students that will join team B.

# Example

# For students = [1, 11, 13, 6, 14], the output should be
# solution(students) = 11.

# Students with numbers 1, 13 and 14 will join team A, and students with numbers 11 and 6 will join team B. Thus, the answer is (1 + 13 + 14) - (11 + 6) = 11.

def solution(students):
    return sum(students[::2]) - sum(students[1::2])
