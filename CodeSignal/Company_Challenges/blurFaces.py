# Your Verkada security camera has captured a funny video of a hummingbird. You'd like to post the clip on your social media account, but there were some people visible in the background. Since the image on a Verkada camera is so sharp and crisp, their faces are clearly identifiable, which you think might be an invasion of privacy. So you've decided to blur their faces before posting the clip

# You are given an image, represented as a matrix of integers, where each integer corresponds to a color. The number in the ith (0-based) row and jth (0-based) column represents the color of the pixel in the ith row and jth column of the image.

# Your task is to blur the image. In order to do that, you need to replace each number of the matrix with the average of the numbers in the neighboring cells. We assume that two cells are neighbors if they share at least one corner. The cell itself is not considered part of the average; only the 8 surrounding neighbors (or fewer if the cell is against an edge).

# Example

# For img = [[1, 4], [7, 10]], the output should be solution(img) = [[7, 6], [5, 4]].

# newImg[0][0] = (4 + 7 + 10) / 3 = 21 / 3 = 7
# newImg[0][1] = (1 + 7 + 10) / 3 = 18 / 3 = 6
# newImg[1][0] = (1 + 4 + 10) / 3 = 15 / 3 = 5
# newImg[1][1] = (1 + 4 + 7) / 3 = 12 / 3 = 4
# For img = [[3, 0, 2, 5], [1, 2, 3, 4], [2, 3, 2, 3]], the output should be solution(img) = [[1, 2.2, 2.8, 3], [2, 2, 2.625, 3], [2, 2, 3, 3]].

# newImg[0][0] = (0 + 1 + 2) / 3 = 3 / 3 = 1
# newImg[0][1] = (1 + 2 + 2 + 3 + 3) / 5 = 11 / 5 = 2.2
# newImg[0][2] = (0 + 2 + 3 + 4 + 5) / 5 = 14 / 5 = 2.8
# newImg[0][3] = (2 + 3 + 4) / 3 = 9 / 3 = 3
# newImg[1][0] = (0 + 2 + 2 + 3 + 3) / 5 = 10 / 5 = 2
# newImg[1][1] = (0 + 1 + 2 + 2 + 2 + 3 + 3 + 3) / 8 = 16 / 8 = 2
# newImg[1][2] = (0 + 2 + 2 + 2 + 3 + 3 + 4 + 5) / 8 = 21 / 8 = 2.625
# newImg[1][3] = (2 + 2 + 3 + 3 + 5) / 5 = 15 / 5 = 3
# newImg[2][0] = (1 + 2 + 3) / 3 = 6 / 3 = 2
# newImg[2][1] = (1 + 2 + 2 + 2 + 3) / 5 = 10 / 5 = 2
# newImg[2][2] = (2 + 3 + 3 + 3 + 4) / 5 = 15 / 5 = 3
# newImg[2][3] = (2 + 3 + 4) / 3 = 9 / 3 = 3
# Input/Output

# [execution time limit] 4 seconds (py3)

# [memory limit] 1 GB

# [input] array.array.integer img

# A matrix of integers representing the colors of each pixel of the image.

# Guaranteed constraints:
# 1 ≤ img.length ≤ 50,
# 1 ≤ img[i].length ≤ 50,
# 0 ≤ img[i][j] ≤ 100.

# [output] array.array.float

# A matrix containing the colors of the resulting image. Your answer will be considered correct if for each matrix cell its absolute error doesn't exceed 10-5.


def solution(img):
    # Get the dimensions of the image
    rows = len(img)
    cols = len(img[0])

    # Initialize the new image with the same dimensions
    new_img = [[0 for _ in range(cols)] for _ in range(rows)]

    # Iterate over each pixel in the image
    for i in range(rows):
        for j in range(cols):
            # Get the neighboring pixels
            neighbors = [
                img[x][y]
                for x in range(max(0, i - 1), min(rows, i + 2))
                for y in range(max(0, j - 1), min(cols, j + 2))
                if (x, y) != (i, j)
            ]

            # Calculate the average color of the neighboring pixels
            new_img[i][j] = sum(neighbors) / len(neighbors)

    return new_img
