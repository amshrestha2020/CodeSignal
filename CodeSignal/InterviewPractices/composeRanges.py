# Given a sorted integer array that does not contain any duplicates, return a summary of the number ranges it contains.

# Example

# For nums = [-1, 0, 1, 2, 6, 7, 9], the output should be
# solution(nums) = ["-1->2", "6->7", "9"].

def solution(nums):
    if not nums:
        return []
    ranges = []
    start = end = nums[0]
    for num in nums[1:]:
        if num == end + 1:
            end = num
        else:
            ranges.append(str(start) if start == end else f"{start}->{end}")
            start = end = num
    ranges.append(str(start) if start == end else f"{start}->{end}")
    return ranges
