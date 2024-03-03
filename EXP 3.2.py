from queue import PriorityQueue

# Define the goal state
goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)

# Define the heuristic function (Manhattan distance)
def heuristic(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i*3 + j] != 0:
                goal_row, goal_col = (state[i*3 + j] - 1) // 3, (state[i*3 + j] - 1) % 3
                distance += abs(i - goal_row) + abs(j - goal_col)
    return distance

# Define the puzzle state representation
class PuzzleState:
    def __init__(self, state, parent=None, move=None, depth=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = self.depth + heuristic(self.state)

    def __lt__(self, other):
        return self.cost < other.cost

# Define possible moves
def possible_moves(state):
    moves = []
    zero_index = state.index(0)
    row, col = zero_index // 3, zero_index % 3
    for dr, dc, move in [(1, 0, 'down'), (-1, 0, 'up'), (0, 1, 'right'), (0, -1, 'left')]:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_state = list(state)
            new_state[row*3 + col], new_state[new_row*3 + new_col] = new_state[new_row*3 + new_col], new_state[row*3 + col]
            moves.append((tuple(new_state), move))
    return moves

# Define A* search algorithm
def astar(start_state):
    frontier = PriorityQueue()
    explored = set()
    start_node = PuzzleState(start_state)
    frontier.put(start_node)

    while not frontier.empty():
        current_node = frontier.get()
        current_state = current_node.state
        if current_state == goal_state:
            path = []
            while current_node.parent:
                path.append((current_node.move, current_node.state))
                current_node = current_node.parent
            path.reverse()
            return path
        explored.add(current_state)

        for next_state, move in possible_moves(current_state):
            if next_state not in explored:
                new_node = PuzzleState(next_state, current_node, move, current_node.depth + 1)
                frontier.put(new_node)

    return None

# Define initial state
initial_state = (1, 2, 3, 4, 5, 6, 0, 7, 8)

# Solve the puzzle
solution = astar(initial_state)

# Print the solution
if solution:
    for move, state in solution:
        print(f"Move: {move}")
        print(state[0:3])
        print(state[3:6])
        print(state[6:9])
        print()
else:
    print("No solution found.")
