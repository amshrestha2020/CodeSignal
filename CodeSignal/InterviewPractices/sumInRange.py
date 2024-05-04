# You have an array of integers nums and an array queries, where queries[i] is a pair of indices (0-based). Find the sum of the elements in nums from the indices at queries[i][0] to queries[i][1] (inclusive) for each query, then add all of the sums for all the queries together. Return that number modulo 109 + 7.

# Example

# For nums = [3, 0, -2, 6, -3, 2] and queries = [[0, 2], [2, 5], [0, 5]], the output should be
# solution(nums, queries) = 10.

# The array of results for queries is [1, 3, 6], so the answer is 1 + 3 + 6 = 10.


def solution(nums, queries):
    # Calculate the prefix sum array
    prefix_sum = [0]
    for num in nums:
        prefix_sum.append(prefix_sum[-1] + num)

    # Initialize the total sum to 0
    total_sum = 0

    # Iterate over the queries
    for query in queries:
        # Calculate the sum of the elements in nums from the indices at query[0] to query[1] (inclusive)
        query_sum = prefix_sum[query[1] + 1] - prefix_sum[query[0]]

        # Add the query sum to the total sum
        total_sum += query_sum

    # Return the total sum modulo 10^9 + 7
    return total_sum % (10**9 + 7)
