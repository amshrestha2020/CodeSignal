# Court is in session. We got a group of witnesses who have all taken an oath to tell the truth. The prosecutor is pointing at the defendants one by one and asking each witnesses a simple question - "guilty or not?". The witnesses are allowed to respond in one of the following three ways:

# I am sure he/she is guilty.
# I am sure he/she is innocent.
# I have no idea.
# The prosecutor has a hunch that one of the witnesses might not be telling the truth so she decides to cross-check all of their testimonies and see if the information gathered is consistent, i.e. there are no two witnesses A and B and a defendant C such that A says C is guilty while B says C is innocent.

# Example

# For

# evidences = [[ 0, 1, 0, 1], 
#              [-1, 1, 0, 0], 
#              [-1, 0, 0, 1]]
# the output should be
# solution(evidences) = true;

# For

# evidences = [[ 1, 0], 
#              [-1, 0], 
#              [ 1, 1],
#              [ 1, 1]]
# the output should be
# solution(evidences) = false.

def solution(evidences):
    is_information_consistent = True

    for col in range(len(evidences[0])):
        prev_answer = 0

        for row in range(len(evidences)):
            is_prev_answer_zero = prev_answer == 0
            is_evidence_zero = evidences[row][col] == 0
            are_prev_answer_and_evidence_equal = prev_answer == evidences[row][col]

            if not is_prev_answer_zero and not is_evidence_zero and not are_prev_answer_and_evidence_equal:
                is_information_consistent = False
                break

            if prev_answer == 0:
                prev_answer = evidences[row][col]

        if not is_information_consistent:
            break

    return is_information_consistent
