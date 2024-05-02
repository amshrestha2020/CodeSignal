# You've been invited to a job interview at a famous company that tests programming challenges. To evaluate your coding skills, they have asked you to parse a given problem's input given as an inputString string, and count the number of primitive type elements within it.

# The inputString can be either a primitive type variable or an array (possibly multidimensional) that contains elements of the primitive types.
# A primitive type variable can be:

# an integer number;
# a string, which is surrounded by " characters (note that it may contain any character except ");
# a boolean, which is either true or false.
# Return the total number of primitive type elements inside inputString.

# Example

# For inputString = "[[0, 20], [33, 99]]", the output should be
# solution(inputString) = 4;
# For inputString = "[ "one", 2, "three" ]", the output should be
# solution(inputString) = 3;
# For inputString = "true", the output should be
# solution(inputString) = 1;
# For inputString = "[[1, 2, [3]], 4]", the output should be
# solution(inputString) = 4.


import json

def solution(inputString):
    # Parse the string into a Python object
    obj = json.loads(inputString)

    # Define a function to count elements in a list
    def count_elements(lst):
        return sum(count_elements(e) if isinstance(e, list) else 1 for e in lst)

    # Count the elements in the object
    return count_elements(obj) if isinstance(obj, list) else 1
