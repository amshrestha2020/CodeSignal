# You have two integer arrays, a and b, and an integer target value v. Determine whether there is a pair of numbers, where one number is taken from a and the other from b, that can be added together to get a sum of v. Return true if such a pair exists, otherwise return false.

# Example

# For a = [1, 2, 3], b = [10, 20, 30, 40], and v = 42, the output should be
# solution(a, b, v) = true.

def solution(a, b, v):
    # Create a set to store the elements of array a
    a_set = set(a)

    # Iterate over the elements in array b
    for num in b:
        # Calculate the complement of the current number with respect to v
        complement = v - num

        # If the complement is in a_set, return True
        if complement in a_set:
            return True

    # If no pair is found, return False
    return False
