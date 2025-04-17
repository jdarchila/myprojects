# todo_gui.py

import tkinter as tk
import os

# ------------------ FILE SETUP ------------------ #
FILENAME = "tasks.txt"

def load_tasks():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_tasks():
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# ------------------ WINDOW SETUP ------------------ #
window = tk.Tk()
window.title("To-Do List App")
window.geometry("400x400")

# ------------------ TASK STORAGE ------------------ #
tasks = load_tasks()  # Load existing tasks from file at startup

# ------------------ TASK ENTRY ------------------ #
task_entry = tk.Entry(window, width=30)
task_entry.pack(pady=10)

# ------------------ TASK DISPLAY ------------------ #
task_listbox = tk.Listbox(window, width=40, height=10)
task_listbox.pack(pady=10)

# Load tasks into the visual listbox too
for task in tasks:
    task_listbox.insert(tk.END, task)

# ------------------ FUNCTIONS ------------------ #

def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        task_listbox.insert(tk.END, task)
        save_tasks()  # ✅ Save to file
        task_entry.delete(0, tk.END)

def delete_task():
    try:
        selected_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_index)
        tasks.pop(selected_index)
        save_tasks()  # ✅ Save updated list to file
    except IndexError:
        print("No task selected to delete.")

# ------------------ BUTTONS ------------------ #
add_button = tk.Button(window, text="Add Task", command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(window, text="Delete Selected Task", command=delete_task)
delete_button.pack(pady=5)

# ------------------ MAIN LOOP ------------------ #
window.mainloop()
