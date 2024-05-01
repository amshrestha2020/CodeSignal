# In a block storage system, new data is written in blocks. We are going to represent the flash memory as one sequential array. We have a list of block writes coming in the form of arrays of size 2: writes[i] = [first_block_written, last_block_written].

# Each block has a rewrite limit. If rewrites on a block reach a certain specified threshold we should run a special diagnostic.

# Given blockCount (an integer representing the total number of blocks), writes (the list of block-write arrays of size 2), and threshold, your task is to return the list of disjoint block segments, each consisting of blocks that have reached the rewrite threshold. The list of block segments should be sorted in increasing order by their left ends.

# Example

# For blockCount = 10, writes = [[0, 4], [3, 5], [2, 6]], and threshold = 2, the output should be
# solution(blockCount, writes, threshold) = [[2, 5]].

# After the first write, the blocks 0, 1, 2, 3 and 4 were written in once;
# After the second write, the blocks 0, 1, 2 and 5 were written in once, and the blocks 3 and 4 reached the rewrite threshold;
# After the final write, the blocks 2 and 5 reached the rewrite threshold as well, so the blocks that should be diagnosed are 2, 3, 4 and 5.
# Blocks 2, 3, 4 and 5 form one consequent segment [2, 5].
# For blockCount = 10, writes = [[0, 4], [3, 5], [2, 6]], and threshold = 3, the output should be
# solution(blockCount, writes, threshold) = [[3, 4]];

# For blockCount = 10, writes = [[3, 4], [0, 1], [6, 6]], and threshold = 1, the output should be
# solution(blockCount, writes, threshold) = [[0, 1], [3, 4], [6, 6]].



def solution(blockCount, writes, threshold):
    # Initialize the number of writes for each block
    writes_count = [0] * blockCount

    # Update the number of writes for each block
    for start, end in writes:
        writes_count[start] += 1
        if end + 1 < blockCount:
            writes_count[end + 1] -= 1

    # Calculate the prefix sum of writes_count
    for i in range(1, blockCount):
        writes_count[i] += writes_count[i - 1]

    # Find the disjoint segments of blocks that have reached the rewrite threshold
    segments = []
    segment_start = -1
    for i in range(blockCount):
        if writes_count[i] >= threshold and segment_start == -1:
            segment_start = i
        elif writes_count[i] < threshold and segment_start != -1:
            segments.append([segment_start, i - 1])
            segment_start = -1
    if segment_start != -1:
        segments.append([segment_start, blockCount - 1])

    return segments
