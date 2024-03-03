import numpy as np
from heapq import heappop, heappush

# Define the goal state
goal_state = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

# Define heuristic function (Manhattan distance)
def heuristic(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                goal_pos = np.where(goal_state == state[i][j])
                distance += abs(i - goal_pos[0][0]) + abs(j - goal_pos[1][0])
    return distance

# Define function to get possible moves
def get_moves(state):
    moves = []
    zero_pos = np.where(state == 0)
    zero_x, zero_y = zero_pos[0][0], zero_pos[1][0]
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        new_x, new_y = zero_x + dx, zero_y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = state.copy()
            new_state[zero_x][zero_y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[zero_x][zero_y]
            moves.append(new_state)
    return moves

# Define A* search algorithm
def solve_puzzle(initial_state):
    open_list = [(heuristic(initial_state), 0, initial_state)]
    closed_list = set()
    while open_list:
        _, cost, state = heappop(open_list)
        if np.array_equal(state, goal_state):
            return cost
        closed_list.add(tuple(map(tuple, state)))
        for move in get_moves(state):
            if tuple(map(tuple, move)) not in closed_list:
                heappush(open_list, (cost + heuristic(move), cost + 1, move))
    return -1

# Example usage:
initial_state = np.array([[1, 2, 3], [4, 5, 6], [0, 7, 8]])
moves_needed = solve_puzzle(initial_state)
print("Number of moves needed to solve the puzzle:", moves_needed)
