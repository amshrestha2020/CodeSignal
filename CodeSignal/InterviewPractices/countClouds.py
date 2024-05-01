# Given a 2D grid skyMap composed of '1's (clouds) and '0's (clear sky), count the number of clouds. A cloud is surrounded by clear sky, and is formed by connecting adjacent clouds horizontally or vertically. You can assume that all four edges of the skyMap are surrounded by clear sky.

# Example

# For

# skyMap = [['0', '1', '1', '0', '1'],
#           ['0', '1', '1', '1', '1'],
#           ['0', '0', '0', '0', '1'],
#           ['1', '0', '0', '1', '1']]
# the output should be
# solution(skyMap) = 2;

# For

# skyMap = [['0', '1', '0', '0', '1'],
#           ['1', '1', '0', '0', '0'],
#           ['0', '0', '1', '0', '1'],
#           ['0', '0', '1', '1', '0'],
#           ['1', '0', '1', '1', '0']]
# the output should be
# solution(skyMap) = 5.

def solution(skyMap):
    def dfs(grid, row, col):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == '0':
            return
        grid[row][col] = '0'  # Mark as visited
        # Recursively visit adjacent cells
        dfs(grid, row + 1, col)
        dfs(grid, row - 1, col)
        dfs(grid, row, col + 1)
        dfs(grid, row, col - 1)

    clouds_count = 0
    for i in range(len(skyMap)):
        for j in range(len(skyMap[0])):
            if skyMap[i][j] == '1':
                dfs(skyMap, i, j)
                clouds_count += 1

    return clouds_count

