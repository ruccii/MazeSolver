import numpy as np 
import heapq
from visualization import visualize_grid

# find the Euclidean distance(Heuristic)
def cal_heuristic(a, b):
    return np.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

 # Function for A-star Graph search alg
def a_star_graph(grid, start, goal, cal_heuristic):
    rows, cols = grid.shape
    open_list = []
    heapq.heappush(open_list, (0 + cal_heuristic(start, goal), 0, start, [start]))  # (f_cost, g_cost, current_node, path)
    visited = set()

    while open_list:
        _, cost, current, path = heapq.heappop(open_list)

        # do not visit the already visited node
        if current in visited:
            continue
        visited.add(current)

        # Find out the current state
        visualize_grid(grid, start, goal, [node[2] for node in open_list], path)

        # Goal reached, return the path and cost
        if current == goal:
            visualize_grid(grid, start, goal, [], path)
            return path, cost

        # neighbors code
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current[0] + dx, current[1] + dy)

            if (0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and grid[neighbor] == 0 and neighbor not in visited):
                new_cost = cost + 1
                heapq.heappush(open_list, (new_cost + cal_heuristic(neighbor, goal), new_cost, neighbor, path + [neighbor]))

    return None, float('inf')

def a_star_tree(grid, start, goal, cal_heuristic):
    separate_rows, separate_cols = grid.shape
    open_list = []
    heapq.heappush(open_list, (0 + cal_heuristic(start, goal), 0, start, [start]))

    all_visited_nodes = []

    iteration = 0

    while open_list:
        iteration += 1

        _, search_cost, current, search_path = heapq.heappop(open_list)

        all_visited_nodes.append(current)

        if iteration % 10 == 0:
            visualize_grid(grid, start, goal, [node[2] for node in open_list], search_path)

        if current == goal:
            visualize_grid(grid, start, goal, [], search_path)
            return all_visited_nodes, search_cost

        for a, b in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbour_element = (current[0] + a, current[1] + b)

            if 0 <= neighbour_element[0] < separate_rows and 0 <= neighbour_element[1] < separate_cols and grid[neighbour_element] == 0:
                new_cost = search_cost + 1
                heapq.heappush(open_list, (new_cost + cal_heuristic(neighbour_element, goal), new_cost, neighbour_element, search_path + [neighbour_element]))

    return None, float('inf')
