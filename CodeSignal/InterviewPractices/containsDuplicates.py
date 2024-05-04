# Given an array of integers, write a function that determines whether the array contains any duplicates. Your function should return true if any element appears at least twice in the array, and it should return false if every element is distinct.

# Example

# For a = [1, 2, 3, 1], the output should be
# solution(a) = true.

# There are two 1s in the given array.

# For a = [3, 1], the output should be
# solution(a) = false.

# The given array contains no duplicates.


def solution(a):
    # Convert the list to a set
    unique_elements = set(a)

    # If the length of the set is equal to the length of the list,
    # it means all elements are distinct
    if len(unique_elements) == len(a):
        return False
    else:
        return True
