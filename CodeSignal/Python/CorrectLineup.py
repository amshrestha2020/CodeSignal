# Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
# For the opening ceremony of an upcoming sports event, an even number of athletes from two teams A and B were picked to put on a performance. They start by forming a correct lineup in which an athlete from one team stands next to an athlete from the other team (i.e., in an alternating pattern). As a part of the performance, adjacent pairs of athletes (i.e. the first one together with the second one, the third one together with the fourth one, etc.) have to swap positions with each other.

# Given a list of athletes, return the list of athletes after the changes, i.e. after each adjacent pair of athletes is swapped.

# Example

# For athletes = [1, 2, 3, 4, 5, 6], the output should be
# solution(athletes) = [2, 1, 4, 3, 6, 5].

def solution(athletes):
    return [athlete for pair in zip(athletes[1::2], athletes[::2]) for athlete in pair]
