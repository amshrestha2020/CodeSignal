# You are the head zookeeper at a large zoo. You've been contacted by schools in the area that want to bring in classes so that students can feed the animals. The animals can only be fed once a day, so no two classes can come on the same day if they want to feed the same animals.

# You have a list classes, such that classes[i] is a list of animals that the ith class wants to feed. Classes i and j cannot come on the same day if an animal in classes[i] also appears in classes[j] (for i ≠ j). Your job is to determine the minimum number of days you would need to have all the classes come to feed the animals if they can all come within 5 days. If it isn't possible for all the classes to come within 5 days, return -1 instead.

# Example

# For classes = [["Tiger", "Lima", "Frog"], ["Tiger", "Zebra","Lion"], ["Tiger", "Rabbit"], ["Emu", "Zebra", "Rabbit"]], the output should be
# solution(classes) = 3.
# Classes 0, 1, and 2 all want to feed the Tiger, so they have to come on different days. Class 3 cannot come on the same day as class 1 (because of the Zebra) or class 2 (because of the Rabbit), but they can come on the same day as class 0. Therefore it only takes 3 days for all the classes to visit the zoo.

# For classes = [["Tiger", "Lima", "Frog"], ["Tiger", "Zebra", "Lion"], ["Tiger", "Rabbit"], ["Lima", "Zebra", "Rabbit"]], the output should be
# solution(classes) = 4.
# Each class has to come on a separate day, because every pair of classes has at least one animal in common.

# For classes = [["Lion", "Emu"], ["Giraffe", "Peacock"], ["Lima"], ["Tiger", "Cheetah", "Slugs"], ["Snakes", "Sealion"]], the output should be
# solution(classes) = 1.
# No classes have animals in common, so they can all come on the same day.


from itertools import combinations

def solution(classes):
    n = len(classes)
    g = [set() for _ in range(n)]
    animal_to_classes = {}

    # Create a graph
    for i, animals in enumerate(classes):
        for animal in animals:
            if animal in animal_to_classes:
                for j in animal_to_classes[animal]:
                    g[i].add(j)
                    g[j].add(i)
            else:
                animal_to_classes[animal] = []
            animal_to_classes[animal].append(i)

    # Try to color the graph with at most 5 colors
    for k in range(1, 6):
        if color_graph(g, k):
            return k

    return -1

def color_graph(g, k):
    n = len(g)
    color = [0] * n

    def valid_color(v, c):
        for neighbor in g[v]:
            if color[neighbor] == c:
                return False
        return True

    def color_node(v):
        if v == n:
            return True
        for c in range(1, k+1):
            if valid_color(v, c):
                color[v] = c
                if color_node(v+1):
                    return True
                color[v] = 0
        return False

    return color_node(0)
