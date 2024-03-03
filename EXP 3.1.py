import numpy as np
from collections import deque

def is_valid_move(maze, x, y):
    rows, cols = len(maze), len(maze[0])
    return 0 <= x < rows and 0 <= y < cols and maze[x][y] == 0

def bfs(maze, start, end, path):
    queue = deque([start])
    visited = set([start])

    while queue:
        x, y = queue.popleft()
        if (x, y) == end:
            path.append((x, y))
            return True

        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if is_valid_move(maze, nx, ny) and (nx, ny) not in visited:
                queue.append((nx, ny))
                visited.add((nx, ny))
                maze[nx][ny] = 2  # Mark the cell as visited

    return False

def solve_maze_bfs(maze, start, end):
    print("Random Maze")
    print_maze(maze)
    path = []
    if bfs(maze, start, end, path):
        print("Path found:")
        print_maze(maze)
        for step in path:
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
solve_maze_bfs(maze, start_point, end_point)
