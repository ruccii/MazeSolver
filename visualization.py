
import matplotlib.pyplot as plt

#--------------------- below code is used for visualization purpose ---------------------
def visualize_grid(grid, start, goal, open_set, path=None):
    plt.clf()
    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            # below code is use to draw walls
            if grid[x, y] == 1:
                plt.fill([y, y+1, y+1, y], [x, x, x+1, x+1], color='gray', edgecolor='black', linewidth=0.5)
            
            # below code is use to draw start point
            elif (x, y) == start:
                plt.fill([y, y+1, y+1, y], [x, x, x+1, x+1], color='red', edgecolor='black', linewidth=0.5)
            
            # below code is use to draw goal point
            elif (x, y) == goal:
                plt.fill([y, y+1, y+1, y], [x, x, x+1, x+1], color='green', edgecolor='black', linewidth=0.5)
    
    # below code is used to draw the box which has yellow colour with blue border(exploring grid box)
    for node in open_set:
        center_x, center_y = node[0] + 0.5, node[1] + 0.5  # Center of the grid cell
        square_size = 0.25  # Half size of the grid
        plt.fill([center_y - square_size, center_y + square_size, center_y + square_size, center_y - square_size],
                 [center_x - square_size, center_x - square_size, center_x + square_size, center_x + square_size],
                 facecolor='yellow', edgecolor='blue', linewidth=1.5)
    
    # below code is used to draw a purple colour (grid exploring) line 
    if path:
        for i in range(len(path) - 1):
            p1 = path[i]
            p2 = path[i + 1]
            plt.plot([p1[1] + 0.5, p2[1] + 0.5], [p1[0] + 0.5, p2[0] + 0.5], color='purple', linewidth=3)
    plt.grid(True, linewidth=0.2)
    plt.pause(0.5)