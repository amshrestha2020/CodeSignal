# After long years of sharpening your programming skills and honing your physique you finally made it: as a member of the ProProgrammers team you've entered Fort Boyard!

# Your team has successfully completed several challenges so far, and one of your teammates is ready to face the next one. In this challenge the participant should make her way through a corridor covered in red laser rays. If she touches one of the rays, she will fail the challenge and become the prisoner of the Fort.

# The corridor has several levels, so it can be represented as an undirected graph of the known number of nodes with start at node 1 and finish at node nodes, both 1-based. Each move the participant can move to the node adjacent to her current position. Since you prepared for each challenge thoroughly, you know when and where the laser rays appear: on the ith (1-based) move the rays disappear from their previous locations and appear in all the nodes x, such that x % k = i % k, where % stands for the modulo operation and k is known. If your teammate ends up in node x when the rays appear there, she'll fail.

# Your goal is to calculate the minimum number of moves required to reach the last node from the node 1, or -1 if it's impossible.

# Example

# For nodes = 5, corridor = [1, 2, 1, 3, 2, 4, 3, 5, 4, 5],
# and k = 4, the output should be
# solution(nodes, corridor, k) = 2.

# As you can see in the image below, the optimal way is to go to node 1 on the first move and to node 5 on the second one.


# For nodes = 4, corridor = [1, 2, 1, 3, 2, 4, 3, 4],
# and k = 2, the output should be
# solution(nodes, corridor, k) = -1.

# As you can see in the following image, your teammate will inevitably end up at an even node on an even move, i.e. when the lasers appear there. Thus, the answer is -1.


from collections import defaultdict

def solution(nodes, corridor, k):
    # Create a graph from the corridor
    graph = defaultdict(set)
    for i in range(0, len(corridor), 2):
        x, y = corridor[i], corridor[i+1]
        graph[x].add(y)
        graph[y].add(x)

    # Initialize the queue and the set of seen nodes
    queue, seen = [(0, 1)], set()

    while queue:
        step, node = queue.pop(0)

        # If the number of steps exceeds the number of nodes, return -1
        if step > nodes:
            return -1

        # For each neighbor of the current node
        for v in graph[node]:
            # If the next step does not coincide with the appearance of the laser in the next node
            if (step + 1) % k != v % k:
                # If the next node is the target node, return the number of steps
                if v == nodes:
                    return step + 1
                # If the next step and node have not been seen before, add them to the queue and the seen set
                tmp = (step + 1, v)
                if tmp not in seen:
                    seen.add(tmp)
                    queue.append(tmp)

    # If the target node cannot be reached, return -1
    return -1
