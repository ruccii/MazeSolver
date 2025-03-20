
import tracemalloc
from tkinter import Label, Toplevel

# ------------------------ Show Results in New Window ----------------------
def show_results(algo_name, algo_type, path, cost, time_taken):
    # Create a new top-level window to display results
    result_window = Toplevel()
    result_window.title("Search Results")

    result_text = f"Output result for {algo_name} using {algo_type} search"
    result_text += f"\nPath: {path}\nCost: {cost}\nTime: {time_taken:.2f} seconds"
    
    # Calculate memory usage
    current_memory, peak_memory = tracemalloc.get_traced_memory()
    result_text += f"\nCurrent Memory: {current_memory / (1024 ** 2):.6f} MB"
    result_text += f"\nPeak Memory: {peak_memory / (1024 ** 2):.6f} MB"

    # Display the result in a label widget with bold and highlighted text
    label = Label(result_window, text=result_text, padx=10, pady=10, 
                  font="Helvetica 12 bold", bg="#ADD8E6", relief="solid")
    label.pack()
