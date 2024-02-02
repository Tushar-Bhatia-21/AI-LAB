from collections import deque

def water_jug_bfs(capacity_jug1, capacity_jug2, target_amount):
    visited_states = set()
    queue = deque([(0, 0)])

    while queue:
        current_state = queue.popleft()
        jug1, jug2 = current_state

        if current_state in visited_states:
            continue

        visited_states.add(current_state)

        if jug1 == target_amount or jug2 == target_amount:
            print(f"Target amount {target_amount} achieved. Steps: {visited_states}")
            return

        # Fill jug 1
        if jug1 < int(capacity_jug1):
            queue.append((int(capacity_jug1), jug2))

        # Fill jug 2
        if jug2 < int(capacity_jug2):
            queue.append((jug1, int(capacity_jug2)))

        # Empty jug 1
        if jug1 > 0:
            queue.append((0, jug2))

        # Empty jug 2
        if jug2 > 0:
            queue.append((jug1, 0))

        # Pour water from jug 1 to jug 2
        pour_amount = min(jug1, int(capacity_jug2) - jug2)
        queue.append((jug1 - pour_amount, jug2 + pour_amount))

        # Pour water from jug 2 to jug 1
        pour_amount = min(jug2, int(capacity_jug1) - jug1)
        queue.append((jug1 + pour_amount, jug2 - pour_amount))

    print("Target amount not achievable with the given jug capacities.")

# Example usage
j1 = input("Enter the water level in the first jug: ")
j2 = input("Enter the water level in the second jug: ")
target = input("Enter the target value: ")

water_jug_bfs(j1, j2, int(target))
