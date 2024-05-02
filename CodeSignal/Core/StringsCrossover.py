# Define crossover operation over two equal-length strings A and B as follows:

# the result of that operation is a string of the same length as the input strings
# result[i] is either A[i] or B[i], chosen at random
# Given array of strings inputArray and a string result, find for how many pairs of strings from inputArray the result of the crossover operation over them may be equal to result.

# Note that (A, B) and (B, A) are the same pair. Also note that the pair cannot include the same element of the array twice (however, if there are two equal elements in the array, they can form a pair).

# Example

# For inputArray = ["abc", "aaa", "aba", "bab"] and result = "bbb", the output should be
# solution(inputArray, result) = 2.


def solution(inputArray, result):
    crossover = 0

    for indexOne in range(len(inputArray)):
        if inputArray[indexOne] == result:
            crossover += len(inputArray) - indexOne - 1
            continue

        for indexTwo in range(indexOne + 1, len(inputArray)):
            for charIndex in range(len(result)):
                if (
                    inputArray[indexOne][charIndex] != result[charIndex] and
                    inputArray[indexTwo][charIndex] != result[charIndex]
                ):
                    break
            else:
                crossover += 1

    return crossover
