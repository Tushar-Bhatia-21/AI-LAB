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
    path = []
    if dfs(maze, start, end, path):
        print("Path found:")
        for step in reversed(path):
            print(step)
    else:
        print("No path found.")

# Example usage:
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

start_point = (0, 0)
end_point = (4, 4)

solve_maze(maze, start_point, end_point)
