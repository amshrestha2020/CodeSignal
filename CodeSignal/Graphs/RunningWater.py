# After long years of sharpening your programming skills and honing your physique you finally made it: as a member of the ProProgrammers team you've entered Fort Boyard!

# It's your turn to show who's the boss: you're the one who will be participating in the next challenge. Here are the rules of this challenge.

# There's a treadmill hanging from the ceiling and going up. At its very top there are three buckets containing water. You can jog up the treadmill and perform one of the following operations:

# empty one of the buckets entirely and pour out all water from it;
# pour water from one bucket into another until either the first one is empty or the second one is full.
# The buckets are connected to one arm of the scales, and the key that your team should reach is hanging from another. The key will be reachable only when the total amount of water in all three buckets is equal to the given volume.

# The capacities (volumes) of all the buckets are stored in an array cap. Initially all three buckets are full, i.e. for each valid i the ith bucket has cap[i] units of water. You want to make sure that your efforts won't be vain and calculate in advance if it is possible to get the key. Given the cap array and the volume, determine if it is possible to obtain the volume amount of water in all three buckets performing only the allowed operations.

# Example

# For cap = [1, 1, 1] and volume = 2, the output should be
# solution(cap, volume) = true.
# Initially there are 3 units of water in all the buckets. The only action you can perform is to empty the water from one of the buckets, which will leave you with 2 units. At this point, pouring water from one bucket to another won't produce a different total amount of water, so the only remaining option is emptying one of the remaining buckets, which will leave you with 1 final unit of water. Now the total amount of the poured water is equal to the given volume, so the answer is true.

# For cap = [16, 5, 3] and volume = 20, the output should be
# solution(cap, volume) = false.
# Here is the list of all possible amounts of water across all three buckets: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 24. As you can see, you can't obtain the given volume.



from collections import deque

def solution(cap, volume):
    # Initialize visited set to keep track of visited states
    visited = set()
    
    # Initialize queue for BFS
    queue = deque([(cap[0], cap[1], cap[2])])
    
    # Perform BFS
    while queue:
        # Get current state of water in buckets
        state = queue.popleft()
        
        # Check if current state is the target volume
        if sum(state) == volume:
            return True
        
        # Explore all possible next states
        for i in range(3):
            # Empty bucket i
            empty_state = list(state)
            empty_state[i] = 0
            empty_state_tuple = tuple(empty_state)
            if empty_state_tuple not in visited:
                queue.append(empty_state_tuple)
                visited.add(empty_state_tuple)
            
            # Pour water from bucket i to bucket j
            for j in range(3):
                if i != j:
                    pour_state = list(state)
                    pour_amount = min(state[i], cap[j] - state[j])
                    pour_state[i] -= pour_amount
                    pour_state[j] += pour_amount
                    pour_state_tuple = tuple(pour_state)
                    if pour_state_tuple not in visited:
                        queue.append(pour_state_tuple)
                        visited.add(pour_state_tuple)
    
    # If no solution is found
    return False

# Example usage:
cap = [1, 1, 1]
volume = 2
print(solution(cap, volume))  # Output: True

cap = [16, 5, 3]
volume = 20
print(solution(cap, volume))  # Output: False
