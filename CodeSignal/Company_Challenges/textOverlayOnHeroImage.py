# Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
# The GoDaddy Website Builder product helps small businesses easily create websites. Let's say we are going to add a feature where the name of a business is automatically placed on top of a large "hero" image on the landing page of the site.

# To do so, we need to find a position on the image where the text will be the most readable. If the text is placed on an area of the image that is too dark, it will be difficult for the site visitors to read it (for simplicity's sake, let's only consider black text on a grayscale image). We will define the optimal position of the text as the position where the mean pixel brightness inside the bounding box for the text is maximized.

# You are given a grayscale image as a 2D array of pixels with the height and width of the text's rectangular bounding box. You must return the bounding box's top-left corner coordinates for the optimal text position. If there is more than one optimal position, return the top-left-most one.

# Example

# For

# image = [[10,  50,  90, 65],
#          [10, 200, 255, 30],
#          [10, 150,  30, 25]]
# height = 2, and width = 3, the output should be
# solution(image, height, width) = [0, 1].

# Both bounding boxes with top-left coordinates at [0, 1] and at [1, 1] have a maximal mean pixel brightness equal to 690 / 6 = 115. Thus, the answer is [0, 1], as it is the topmost one.

# See the resulting bounding box in the image below.


# Input/Output

# [execution time limit] 4 seconds (py3)

# [memory limit] 1 GB

# [input] array.array.integer image

# Array of non-negative integers less than 256.

# Guaranteed constraints:
# 1 ≤ image.length ≤ 20,
# 1 ≤ image[0].length ≤ 20,
# 0 ≤ image[i][j] ≤ 255.

# [input] integer height

# Guaranteed constraints:
# 1 ≤ height ≤ image.length.

# [input] integer width

# Guaranteed constraints:
# 1 ≤ width ≤ image[0].length.

# [output] array.integer

# Array of two integers: indices of row and column for the optimal position, respectively.

def solution(image, height, width):
    def columnSum(x, y1, y2):
        result = 0
        for y in range(y1, y2):
            result += image[y][x]
        return result

    def rowSum(y, x1, x2):
        result = 0
        for x in range(x1, x2):
            result += image[y][x]
        return result

    bestSum = -1
    bestPos = []
    bboxSum = 0
    lastRowLeftmostSum = 0

    for i in range(len(image) - height + 1):
        for j in range(len(image[0]) - width + 1):
            if i == 0 and j == 0:
                for y in range(height):
                    bboxSum += rowSum(y, 0, width)
                lastRowLeftmostSum = bboxSum
            elif j == 0:
                bboxSum = lastRowLeftmostSum - rowSum(i - 1, 0, width) + rowSum(i + height - 1, 0, width)
                lastRowLeftmostSum = bboxSum
            else:
                bboxSum = (bboxSum - columnSum(j - 1, i, i + height)
                                   + columnSum(j + width - 1, i, i + height))
            if bboxSum > bestSum:
                bestSum = bboxSum
                bestPos = [i, j]

    return bestPos
