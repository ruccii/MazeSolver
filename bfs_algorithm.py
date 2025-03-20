from collections import deque
from visualization import visualize_grid

def bfs_graph_search(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    queue = deque([(start, [start])]) 
    visited = set()
    visited.add(start)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        (current_row, current_col), path = queue.popleft()

        # Visualize the grid
        visualize_grid(maze, start, end, [node[0] for node in queue], path)

        if (current_row, current_col) == end:
            cost = len(path) - 1
            visualize_grid(maze, start, end, [], path)
            return path, cost

        for update_row, update_col in directions:
            next_row, next_col = current_row + update_row, current_col + update_col
            if (
                0 <= next_row < rows
                and 0 <= next_col < cols
                and maze[next_row][next_col] == 0
            ):
                if (next_row, next_col) not in visited:
                    visited.add((next_row, next_col))
                    queue.append(((next_row, next_col), path + [(next_row, next_col)]))

    return None, float("inf")



def bfs_tree_search(grid, start, goal):
    rows, cols = grid.shape
    open_list = deque([(start, [start])])
    all_visited_nodes = set()

    while open_list:
        current, path = open_list.popleft()

        # Mark current node as visited
        all_visited_nodes.add(current)

        # Visualize the current state (every 10 iterations)
        if len(open_list) % 10 == 0:
            visualize_grid(grid, start, goal, [node[0] for node in open_list], path)

        # Check if goal is reached
        if current == goal:
            visualize_grid(grid, start, goal, [], path)
            cost = len(path) - 1
            return all_visited_nodes, cost

        # Explore neighbors (no need to check visited nodes for BFS)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]: 
            neighbor = (current[0] + dx, current[1] + dy)

            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and grid[neighbor] == 0 and neighbor not in all_visited_nodes:
                open_list.append((neighbor, path + [neighbor]))

    return None, float('inf')