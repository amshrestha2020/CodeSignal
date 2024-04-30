# Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in a non-descending order without moving the trees. People can be very tall!

# Example

# For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
# solution(a) = [-1, 150, 160, 170, -1, -1, 180, 190].


def solution(a):
    # Extract the heights of people from the array
    heights = [h for h in a if h != -1]
    
    # Sort the heights in non-descending order
    sorted_heights = sorted(heights)
    
    # Create an iterator for the sorted heights
    height_iterator = iter(sorted_heights)
    
    # Replace non-tree elements in the original array with sorted heights
    result = [next(height_iterator) if elem != -1 else -1 for elem in a]
    
    return result

