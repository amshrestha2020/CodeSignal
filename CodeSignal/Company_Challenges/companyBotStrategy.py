# Each CodeSignal Company Bot is trained by engineers from that specific company. The way it works is that a representative group of engineers from each company is identified as trainers before the bot goes live, and they CodeFight against the bot during a training phase. The current training algorithm is definitely more complex, but let's assume it works this way:

# For each trainer we collect two pieces of information per task [answerTime, correctness], where correctness is 1 if the answer was correct, -1 if the answer was wrong, and 0 if no answer was given. In this case, the bot's correct answer time for a given task would be the average of the answer times from the trainers who answered correctly. Given all of the training information for a specific task, calculate the bot's answer time.

# Example

# For

# trainingData = [[3, 1],
#                 [6, 1],
#                 [4, 1],
#                 [5, 1]]
# the output should be solution(trainingData) = 4.5.

# All four trainers have solved the task correctly, so the answer is (3 + 6 + 4 + 5) / 4 = 4.5.

# For

# trainingData = [[4, 1],
#                 [4, -1],
#                 [0, 0],
#                 [6, 1]]
# the output should be solution(trainingData) = 5.0.

# Only the 1st and the 4th trainers (1-based) submitted correct solutions, so the answer is (4 + 6) / 2 = 5.0.

# For

# trainingData = [[4, -1],
#                 [0, 0],
#                 [5, -1]]
# the output should be solution(trainingData) = 0.0.

# No correct answers were given for the task.



def solution(trainingData):
    total_time = 0
    correct_count = 0
    
    for time, correctness in trainingData:
        if correctness == 1:
            total_time += time
            correct_count += 1
    
    if correct_count == 0:
        return 0
    else:
        return total_time / correct_count

# Test cases
trainingData1 = [[3, 1], [6, 1], [4, 1], [5, 1]]
print(solution(trainingData1))  # Output: 4.5

trainingData2 = [[4, 1], [4, -1], [0, 0], [6, 1]]
print(solution(trainingData2))  # Output: 5.0

trainingData3 = [[4, -1], [0, 0], [5, -1]]
print(solution(trainingData3))  # Output: 0.0
