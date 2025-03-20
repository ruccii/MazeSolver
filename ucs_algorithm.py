import heapq
from visualization import visualize_grid

# UCS Algorithm for Graph Search
def ucs_graph_search(maze, start, goal):
    rows, cols = maze.shape
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    pq = [(0, start)]
    visited = set()
    parent_map = {} 

    while pq:
        cost, (x, y) = heapq.heappop(pq)

        # Build the current shortest path for visualization
        current_path = []
        node = (x, y)
        while node in parent_map:
            current_path.append(node)
            node = parent_map[node]
        current_path.append(start)

        visualize_grid(maze, start, goal, [node[1] for node in pq], current_path[::-1])

        # If goal is reached, reconstruct the path
        if (x, y) == goal:
            path = []
            while (x, y) != start:
                path.append((x, y))
                x, y = parent_map[(x, y)]
            path.append(start)
            visualize_grid(maze, start, goal, [], path[::-1])  
            return cost, path[::-1] 

        if (x, y) in visited:
            continue
        visited.add((x, y))

        # Explore neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx, ny] == 0:
                if (nx, ny) not in visited:
                    heapq.heappush(pq, (cost + 1, (nx, ny)))
                    parent_map[(nx, ny)] = (x, y)

    return float("inf"), [] 


# UCS Algorithm for Tree Search
def ucs_tree_search(maze, start, goal):
    rows, cols = maze.shape
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    pq = [(0, start)]
    visited = []
    parent_map = {}

    iteration = 0

    while pq:
        iteration += 1
        cost, (x, y) = heapq.heappop(pq)

        # Build the current shortest path for visualization
        if iteration % 10 == 0:
            current_path = []
            node = (x, y)
            while node in parent_map:
                current_path.append(node)
                node = parent_map[node]
            current_path.append(start)

            # Visualize the grid
            visualize_grid(maze, start, goal, [node[1] for node in pq], current_path[::-1])

        # If goal is reached, reconstruct the path
        if (x, y) == goal:
            path = []
            while (x, y) != start:
                path.append((x, y))
                x, y = parent_map[(x, y)]
            path.append(start)
            visualize_grid(maze, start, goal, [], path[::-1]) 
            return cost, visited

        visited.append((x, y))

        # Explore neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx, ny] == 0: 
                if (nx, ny) not in visited:
                    heapq.heappush(pq, (cost + 1, (nx, ny)))
                    parent_map[(nx, ny)] = (x, y)

    return float("inf"), [] 
