
from collections import deque
import heapq
import numpy as np
from visualization import visualize_grid

# Function for DFS Graph Search
def dfs_graph(grid, start, goal):
    rows, cols = grid.shape
    stack = [(start, [start])]  
    visited = set()

    while stack:
        current, path = stack.pop()

        # Skip if the node is already visited
        if current in visited:
            continue
        visited.add(current)

        visualize_grid(grid, start, goal, [node[0] for node in stack], path)

        # Check if the goal is reached
        if current == goal:
            visualize_grid(grid, start, goal, [], path)
            return path

        # Explore neighbors
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  
            neighbor = (current[0] + dx, current[1] + dy)


            if (0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and 
                grid[neighbor] == 0 and neighbor not in visited):
                stack.append((neighbor, path + [neighbor]))

    return None  


# Function for DFS Tree Search
def dfs_tree(grid, start, goal):
    rows, cols = grid.shape
    stack = [(start, [start])]  
    visited = set()

    while stack:
        current, path = stack.pop()

        visualize_grid(grid, start, goal, [node[0] for node in stack], path)

        # Goal reached, return the path
        if current == goal:
            visualize_grid(grid, start, goal, [], path)
            return path

        # Mark the current node as visited globally
        visited.add(current)

        # Explore neighbors (avoid nodes already in the path or visited)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]: 
            neighbor = (current[0] + dx, current[1] + dy)

            if (0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and 
                grid[neighbor] == 0 and neighbor not in path):
                stack.append((neighbor, path + [neighbor]))

    return None


