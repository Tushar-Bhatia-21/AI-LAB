import numpy as np

def is_valid_move(maze, x, y):
    rows, cols = len(maze), len(maze[0])
    return 0 <= x < rows and 0 <= y < cols and maze[x][y] == 0

def dfs(maze, start, end, path):
    x, y = start

    if start == end:
        path.append(end)
        return True

    if not is_valid_move(maze, x, y):
        return False

    maze[x][y] = 2  # Mark the current cell as visited

    if dfs(maze, (x + 1, y), end, path) or dfs(maze, (x, y + 1), end, path) or \
       dfs(maze, (x - 1, y), end, path) or dfs(maze, (x, y - 1), end, path):
        path.append((x, y))
        return True

    return False

def solve_maze(maze, start, end):
    print("Random Maze")
    print_maze(maze)
    path = []
    if dfs(maze, start, end, path):
        print("Path found:")
        print_maze(maze)
        for step in reversed(path):
            print(step)
    else:
        print("No path found.")

def print_maze(maze):
    for row in maze:
        print(" ".join(map(str, row)))

# Example usage:
n = int(input("Enter the number dimension of maze: "))
obstacle_count = float(input("Enter the obstacle density (between 0 and 1): "))
maze = np.zeros((n, n), dtype=int)

for i in range(n):
    for j in range(n):
        if np.random.rand() < obstacle_count:
            maze[i, j] = 1

start_point = (0, 0)
end_point = (n - 1, n - 1)
solve_maze(maze, start_point, end_point)
