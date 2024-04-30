# Write a function that reverses characters in (possibly nested) parentheses in the input string.

# Input strings will always be well-formed with matching ()s.

# Example

# For inputString = "(bar)", the output should be
# solution(inputString) = "rab";
# For inputString = "foo(bar)baz", the output should be
# solution(inputString) = "foorabbaz";
# For inputString = "foo(bar)baz(blim)", the output should be
# solution(inputString) = "foorabbazmilb";
# For inputString = "foo(bar(baz))blim", the output should be
# solution(inputString) = "foobazrabblim".
# Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim".


def solution(inputString):
    stack = []
    result = list(inputString)
    
    for i, char in enumerate(inputString):
        if char == '(':
            stack.append(i)
        elif char == ')':
            start = stack.pop()
            result[start+1:i] = reversed(result[start+1:i])
    
    # Remove parentheses from the final result
    result = [char for char in result if char not in '()']
    
    return ''.join(result)
