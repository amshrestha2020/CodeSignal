# Note: Write a solution with O(operations.length) complexity, since this is what you would be asked to do during a real interview.

# Implement a modified stack that, in addition to using push and pop operations, allows you to find the current minimum element in the stack by using a min operation.

# Example

# For operations = ["push 10", "min", "push 5", "min", "push 8", "min", "pop", "min", "pop", "min"], the output should be
# solution(operations) = [10, 5, 5, 5, 10].

# The operations array contains 5 instances of the min operation. The results array contains 5 numbers, each representing the minimum element in the stack at the moment when min was called.

def solution(operations):
    stack = []
    min_stack = []
    result = []

    for op in operations:
        if op.startswith("push"):
            num = int(op.split()[1])
            stack.append(num)
            if not min_stack or num <= min_stack[-1]:
                min_stack.append(num)
        elif op == "pop":
            popped = stack.pop()
            if popped == min_stack[-1]:
                min_stack.pop()
        elif op == "min":
            result.append(min_stack[-1])

    return result

# Test case
print(solution(["push 10", "min", "push 5", "min", "push 8", "min", "pop", "min", "pop", "min"]))  # Output: [10, 5, 5, 5, 10]

