
import time
import tracemalloc
from tkinter import Tk, Button, Label, Radiobutton, IntVar
from tkinter import PhotoImage
from PIL import Image, ImageTk

# Importing user-defined libraries
from maze_dim import maze_env
from result_display import show_results
from aStar_algorithm import cal_heuristic, a_star_graph, a_star_tree
from dfs_algorithm import dfs_graph, dfs_tree
from bfs_algorithm import bfs_graph_search, bfs_tree_search
from ucs_algorithm import ucs_graph_search, ucs_tree_search


# Global variable to track search progress
search_in_progress = False

# ----------------------- Button ----------------------------
def start_button():
    global search_in_progress
    if not search_in_progress:
        print("Start Button Pressed")
        
        if algo_name_choice.get() == 1:
            algo_name = "A-STAR"
            # Get selected algorithm type (Graph or Tree)
            if algo_type_choice.get() == 1:
                algo_type = "Graph"
            else:
                algo_type = "Tree"
            search_in_progress = True
            run_algo(algo_name, algo_type, maze_env, start, goal, cal_heuristic)
        
        elif algo_name_choice.get() == 2:
            algo_name = "DFS"
            # Get selected algorithm type (Graph or Tree)
            if algo_type_choice.get() == 1:
                algo_type = "Graph"
            else:
                algo_type = "Tree"    
            search_in_progress = True
            run_algo(algo_name, algo_type, maze_env, start, goal, cal_heuristic)

        elif algo_name_choice.get() == 3:
            algo_name = "BFS"
            # Get selected algorithm type (Graph or Tree)
            if algo_type_choice.get() == 1:
                algo_type = "Graph"
            else:
                algo_type = "Tree"    
            search_in_progress = True
            run_algo(algo_name, algo_type, maze_env, start, goal, cal_heuristic)

        elif algo_name_choice.get() == 4:
            algo_name = "UCS"
            # Get selected algorithm type (Graph or Tree)
            if algo_type_choice.get() == 1:
                algo_type = "Graph"
            else:
                algo_type = "Tree"    
            search_in_progress = True
            run_algo(algo_name, algo_type, maze_env, start, goal, cal_heuristic)

    else:
        print("Search already in progress!")


# ---------------------- Run Algorithm ----------------------------
def run_algo(algo_name, algo_type, env, start_pos, goal_pos, calculation):
    global search_in_progress
    tracemalloc.start()
    print(f"Running {algo_name} for {algo_type} search Result")

    # A-STAR BLOCK
    if algo_name == 'A-STAR':
        if algo_type == "Graph":
            start_time = time.time()
            path, cost = a_star_graph(env, start_pos, goal_pos, calculation)
            end_time = time.time()
            if search_in_progress:
                if path:
                    print(f"Path: {path}\nCost: {cost}")
                    print(f"Time used: {end_time - start_time:.2f} seconds")
                    show_results(algo_name, algo_type, path, cost, end_time - start_time)
                else:
                    print("No path found.")
                    show_results(algo_name, algo_type, None, None, None)
            else:
                print("Search interrupted by user.")
        else:
            start_time = time.time()
            path, cost = a_star_tree(env, start_pos, goal_pos, calculation)
            end_time = time.time()
            if search_in_progress:
                if path:
                    print(f"Path: {path}\nCost: {cost}")
                    print(f"Time used: {end_time - start_time:.2f} seconds")
                    show_results(algo_name, algo_type, path, cost, end_time - start_time)
                else:
                    print("No path found.")
                    show_results(algo_name, algo_type, None, None, None)
            else:
                print("Search interrupted by user.")
    
    # DFS - BlOCK
    elif algo_name == 'DFS':     
        if algo_type == "Graph":
            start_time = time.time()
            path = dfs_graph(env, start_pos, goal_pos)
            end_time = time.time()
            if search_in_progress:
                if path:
                    print(f"Path: {path}")
                    print(f"Time used: {end_time - start_time:.2f} seconds")
                    show_results(algo_name, algo_type, path, None, end_time - start_time)
                else:
                    print("No path found.")
                    show_results(algo_name, algo_type, None, None, None)
            else:
                print("Search interrupted by user.")
        else:
            start_time = time.time()
            path = dfs_tree(env, start_pos, goal_pos)
            end_time = time.time()
            if search_in_progress:
                if path:
                    print(f"Path: {path}")
                    print(f"Time used: {end_time - start_time:.2f} seconds")
                    show_results(algo_name, algo_type, path, None, end_time - start_time)
                else:
                    print("No path found.")
                    show_results(algo_name, algo_type, None, None, None)
            else:
                print("Search interrupted by user.")

    #BFS - BLOCK
    elif algo_name == 'BFS':
        if algo_type == "Graph":
            start_time = time.time()
            path, cost = bfs_graph_search(env, start_pos, goal_pos)
            end_time = time.time()
            if search_in_progress:
                if path:
                    print(f"Path: {path}\nCost: {cost}")
                    print(f"Time used: {end_time - start_time:.2f} seconds")
                    show_results(algo_name, algo_type, path, cost, end_time - start_time)
                else:
                    print("No path found.")
                    show_results(algo_name, algo_type, None, None, None)
            else:
                print("Search interrupted by user.")
        else:
            start_time = time.time()
            path, cost = bfs_tree_search(env, start_pos, goal_pos)
            end_time = time.time()
            if search_in_progress:
                if path:
                    print(f"Path: {path}\nCost: {cost}")
                    print(f"Time used: {end_time - start_time:.2f} seconds")
                    show_results(algo_name, algo_type, path, cost, end_time - start_time)
                else:
                    print("No path found.")
                    show_results(algo_name, algo_type, None, None, None)
            else:
                print("Search interrupted by user.")

    # UCS - BlOCK
    elif algo_name == 'UCS':     
        if algo_type == "Graph":
            start_time = time.time()
            cost, path = ucs_graph_search(env, start_pos, goal_pos)
            end_time = time.time()
            if search_in_progress:
                if path:
                    print(f"Path: {path}\nCost: {cost}")
                    print(f"Time used: {end_time - start_time:.2f} seconds")
                    show_results(algo_name, algo_type, path, cost, end_time - start_time)
                else:
                    print("No path found.")
                    show_results(algo_name, algo_type, None, None, None)
            else:
                print("Search interrupted by user.")
        else:
            start_time = time.time()
            cost, path = ucs_tree_search(env, start_pos, goal_pos)
            end_time = time.time()
            if search_in_progress:
                if path:
                    print(f"Path: {path}\nCost: {cost}")
                    print(f"Time used: {end_time - start_time:.2f} seconds")
                    show_results(algo_name, algo_type, path, cost, end_time - start_time)
                else:
                    print("No path found.")
                    show_results(algo_name, algo_type, None, None, None)
            else:
                print("Search interrupted by user.")

    # ------------------------- Calculate Memory ---------------------------
    current_memory, peak_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print("Memory Used Results")
    print(f"Current memory usage is {current_memory / (1024 ** 2):.6f}MB; "
          f"Peak was {peak_memory / (1024 ** 2):.6f}MB")

    search_in_progress = False  # Reset the flag when search completes


# -------------------------- Main Function ---------------------------
if __name__ == "__main__":
    print("Running Algorithm on Maze")

    # Define start and goal nodes
    start = (1, 1)
    goal = (8, 8)

    # Create Tkinter main window
    root = Tk()
    root.title("Maze Solver")
    
    # Add Title Label
    title_label = Label(root, text="Welcome to Maze Solver", font=("Helvetica", 20, "bold"))
    title_label.pack(pady=20)

    # Load the image and display below the title
    img = Image.open("maze-png.png")  # Replace with your image path
    img = img.resize((300, 200))  # Resize the image if needed
    img_tk = ImageTk.PhotoImage(img)

    image_label = Label(root, image=img_tk)
    image_label.img = img_tk  # Keep a reference to avoid garbage collection
    image_label.pack(pady=10)

    # Add Algorithm Label
    Algo_label = Label(root, text="Select Algorithm:", font=("Helvetica", 10))
    Algo_label.pack(pady=10)

    # Create radio button to select between aStar, DFS, BFS and UCS
    algo_name_choice = IntVar()
    algo_name_choice.set(1)  # Default to "ASTAR"

    # Create a frame for algorithm selection radio buttons
    algo_name_frame = Label(root)
    algo_name_frame.pack(pady=5)

    astar_radio = Radiobutton(algo_name_frame, text="A*", 
                              variable=algo_name_choice, value=1, font=("Helvetica", 12))
    astar_radio.grid(row=0, column=0, padx=10)  # first column
    
    dfs_radio = Radiobutton(algo_name_frame, text="DFS", 
                            variable=algo_name_choice, value=2, font=("Helvetica", 12))
    dfs_radio.grid(row=0, column=1, padx=10)  # second column

    bfs_radio = Radiobutton(algo_name_frame, text="BFS", 
                            variable=algo_name_choice, value=3, font=("Helvetica", 12))
    bfs_radio.grid(row=0, column=2, padx=10)  # third column

    ucs_radio = Radiobutton(algo_name_frame, text="UCS", 
                            variable=algo_name_choice, value=4, font=("Helvetica", 12))
    ucs_radio.grid(row=0, column=3, padx=10)  # fourth column


    # Create radio button to select between Graph and Tree
    algo_type_choice = IntVar()
    algo_type_choice.set(1)  # Default to "Graph"

    # Create a frame for graph/tree type radio buttons
    algo_type_frame = Label(root)
    algo_type_frame.pack(pady=5)
    
    graph_radio = Radiobutton(algo_type_frame, text="Graph Search", 
                              variable=algo_type_choice, value=1, font=("Helvetica", 10))
    graph_radio.grid(row=0, column=0, padx=10)  # Place in first column
    
    tree_radio = Radiobutton(algo_type_frame, text="Tree Search", 
                             variable=algo_type_choice, value=2, font=("Helvetica", 10))
    tree_radio.grid(row=0, column=1, padx=10)  # Place in second column

    # Create Start button below the radio buttons
    start_button_widget = Button(root, text="Start", font=("Helvetica", 14), command=start_button)
    start_button_widget.pack(pady=20)

    # Start the Tkinter main loop
    root.mainloop()




