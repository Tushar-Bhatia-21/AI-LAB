from queue import PriorityQueue

class PuzzleNode:
    def __init__(self, state, parent=None, move=None):
        self.state = state
        self.parent = parent
        self.move = move
        self.cost = 0
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def __lt__(self, other):
        return self.cost < other.cost

    def __eq__(self, other):
        return self.state == other.state

def is_goal(state):
    return state == (1, 2, 3, 4, 5, 6, 7, 8, 0)

def get_manhattan_distance(state):
    goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i * 3 + j]
            if value != 0:
                goal_position = goal_state.index(value)
                distance += abs(i - goal_position // 3) + abs(j - goal_position % 3)
    return distance

def get_possible_moves(state):
    moves = []
    zero_index = state.index(0)
    row, col = zero_index // 3, zero_index % 3
    if row > 0:
        moves.append((-3, 'up'))
    if row < 2:
        moves.append((3, 'down'))
    if col > 0:
        moves.append((-1, 'left'))
    if col < 2:
        moves.append((1, 'right'))
    return moves

def apply_move(state, move):
    new_state = list(state)
    zero_index = new_state.index(0)
    new_index = zero_index + move[0]
    new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
    return tuple(new_state)

def solve_puzzle(initial_state):
    start_node = PuzzleNode(initial_state)
    start_node.cost = get_manhattan_distance(initial_state)
    frontier = PriorityQueue()
    frontier.put(start_node)

    while not frontier.empty():
        current_node = frontier.get()
        current_state = current_node.state

        if is_goal(current_state):
            path = []
            while current_node.parent:
                path.append((current_node.move, current_node.state))
                current_node = current_node.parent
            path.reverse()
            return path

        possible_moves = get_possible_moves(current_state)
        for move in possible_moves:
            new_state = apply_move(current_state, move)
            new_node = PuzzleNode(new_state, current_node, move[1])
            new_node.cost = new_node.depth + get_manhattan_distance(new_state)
            frontier.put(new_node)

    return None

# Example usage:
initial_state = (1, 2, 3, 4, 5, 6, 0, 7, 8)
solution = solve_puzzle(initial_state)
if solution:
    for move, state in solution:
        print(f"Move: {move}")
        print(state[0:3])
        print(state[3:6])
        print(state[6:9])
        print()
else:
    print("No solution found.")
