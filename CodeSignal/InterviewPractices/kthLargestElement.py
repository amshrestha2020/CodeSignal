# Note: Avoid using built-in std::nth_element (or analogous built-in functions in languages other than C++) when solving this challenge. Implement them yourself, since this is what you would be asked to do during a real interview.

# Find the kth largest element in an unsorted array. This will be the kth largest element in sorted order, not the kth distinct element.

# Example

# For nums = [7, 6, 5, 4, 3, 2, 1] and k = 2, the output should be
# solution(nums, k) = 6;
# For nums = [99, 99] and k = 1, the output should be
# solution(nums, k) = 99.


def partition(nums, low, high):
    pivot = nums[high]
    i = low - 1
    for j in range(low, high):
        if nums[j] >= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1], nums[high] = nums[high], nums[i + 1]
    return i + 1

def find_kth_largest(nums, k):
    low, high = 0, len(nums) - 1
    while low <= high:
        pivot_index = partition(nums, low, high)
        if pivot_index == k - 1:
            return nums[pivot_index]
        elif pivot_index > k - 1:
            high = pivot_index - 1
        else:
            low = pivot_index + 1
    return -1  # This should never be reached if k is valid

def solution(nums, k):
    return find_kth_largest(nums, k)

# Test cases
print(solution([7, 6, 5, 4, 3, 2, 1], 2))  # Output: 6
print(solution([99, 99], 1))              # Output: 99
