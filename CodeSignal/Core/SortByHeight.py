# Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in a non-descending order without moving the trees. People can be very tall!

# Example

# For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
# solution(a) = [-1, 150, 160, 170, -1, -1, 180, 190].

def solution(a):
    for i in range(len(a)):
        if a[i] == -1:
            continue
        min_value_index = i
        for j in range(i + 1, len(a)):
            if a[j] == -1:
                continue
            if a[j] < a[min_value_index]:
                min_value_index = j
        swap(i, min_value_index, a)
    return a

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
