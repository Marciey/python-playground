def dfs(grid, start, goal):
    stack = [start]
    visited = set() 
    parent = {} 

    visited.add(start)

    while stack:
        current = stack.pop()
        if current == goal:
            return reconstruct_path(parent, start, goal)
        for neighbor in get_neighbors(grid, current):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                stack.append(neighbor)
    return []

def get_neighbors(grid, node):
    x, y = node
    neighbors = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Up, Down, Left, Right
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != 1:
            neighbors.append((nx, ny))
    return neighbors

def reconstruct_path(parent, start, goal):
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = parent[current]
    path.append(start)
    path.reverse()
    return path
if __name__ == "__main__":

    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]

    start = (0, 0) 
    goal = (4, 4) 

    path = dfs(grid, start, goal)
    if path:
        print("Optimal Path:", path)
    else:
        print("No path found.")