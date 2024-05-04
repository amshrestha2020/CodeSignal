# Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
# Sort an array of integers.

# Example

# For sequence = [3, 6, 1, 5, 3, 6], the output should be
# solution(sequence) = [1, 3, 3, 5, 6, 6].

def solution(sequence):
    def merge(sequence, left, middle, right):

        result = []

        i = left
        j = middle
        while i < middle and j < right:
            if sequence[i] < sequence[j]:
                result.append(sequence[i])
                i += 1
            else:
                result.append(sequence[j])
                j += 1

        while i < middle:
            result.append(sequence[i])
            i += 1

        while j < right:
            result.append(sequence[j])
            j += 1

        for i in range(left, right):
            sequence[i] = result[i - left]

    def split(sequence, left, right):
        middle = (left + right) // 2

        if right - left <= 1:
            return
            
        split(sequence, left, middle)
        split(sequence, middle, right)
        merge(sequence, left, middle, right)

    split(sequence, 0, len(sequence))

    return sequence
