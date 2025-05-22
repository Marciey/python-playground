import heapq

def manhattan_distance(x1, y1, x2, y2):
    """Calculate Manhattan distance."""
    return abs(x1 - x2) + abs(y1 - y2)

def best_first_search(grid, start, goal):
    """Find the treasure using Best-First Search."""
    rows, cols = len(grid), len(grid[0])
    visited = set()
    pq = []  # Priority queue for the cells to explore
    came_from = {}  # To reconstruct the path
    
    # Add the start cell to the queue with its heuristic value
    heapq.heappush(pq, (manhattan_distance(*start, *goal), start))
    
    while pq:
        _, current = heapq.heappop(pq)
        x, y = current
        
        if current in visited:
            continue
        
        visited.add(current)
        
        # Check if we have reached the treasure
        if current == goal:
            break
        
        # Explore neighbors
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_cell = (x + dx, y + dy)
            nx, ny = next_cell
            if 0 <= nx < rows and 0 <= ny < cols and next_cell not in visited:
                heapq.heappush(pq, (manhattan_distance(nx, ny, *goal), next_cell))
                came_from[next_cell] = current
    
    # Reconstruct path
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = came_from.get(current, start)
    path.append(start)
    path.reverse()
    return path

# Define the grid and start/goal positions
grid = [
    [0, 0, 0, 0, 0],
    [0, 0, "T", 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]
start = (0, 0)
goal = (1, 2)  # Location of the treasure

# Run the Best-First Search algorithm
path = best_first_search(grid, start, goal)
print("Path to the treasure:", path)