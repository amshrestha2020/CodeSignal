# Some people run along a straight line in the same direction. They start simultaneously at pairwise distinct positions and run with constant speed (which may differ from person to person).

# If two or more people are at the same point at some moment we call that a meeting. The number of people gathered at the same point is called meeting cardinality.

# For the given starting positions and speeds of runners find the maximum meeting cardinality assuming that people run infinitely long. If there will be no meetings, return -1 instead.

# Example

# For startPosition = [1, 4, 2] and speed = [27, 18, 24], the output should be
# solution(startPosition, speed) = 3.

# In 20 seconds after the runners start running, they end up at the same point. Check out the gif below for better understanding:



def solution(start_position, speed):
    res = 1

    for i in range(len(start_position)):
        for j in range(i + 1, len(start_position)):
            dist_diff = start_position[j] - start_position[i]
            speed_diff = speed[i] - speed[j]
            cnt = 0

            if speed_diff == 0 and dist_diff != 0:
                continue

            for k in range(len(start_position)):
                if start_position[k] * speed_diff + speed[k] * dist_diff == start_position[i] * speed_diff + speed[i] * dist_diff:
                    cnt += 1

            if cnt == 0:
                continue

            if cnt > res:
                res = cnt

    if res < 2:
        return -1
    return res
