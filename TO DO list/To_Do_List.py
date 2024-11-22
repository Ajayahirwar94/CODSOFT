import tkinter as tk
from tkinter import messagebox
import json

class TODOLIst:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.tasks = []
        self.load_TASK()

        
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        
        self.task_input = tk.Entry(self.frame, width=30)
        self.task_input.pack(pady=10)

        
        self.add_button = tk.Button(self.frame, text="Add Task", command=self.add_TAsk)
        self.add_button.pack(pady=5)

        self.update_button = tk.Button(self.frame, text="Update Task", command=self.update_Task)
        self.update_button.pack(pady=5)

        self.remove_button = tk.Button(self.frame, text="Remove Task", command=self.remove_TASk)
        self.remove_button.pack(pady=5)

        
        self.task_listbox = tk.Listbox(self.frame, width=50, height=10)
        self.task_listbox.pack(pady=10)

        self.refresh_taSKS()

    def load_TASK(self):
        try:
            with open('todo_list.json', 'r') as file:
                self.tasks = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.tasks = []

    def save_TASK(self):
        with open('todo_list.json', 'w') as file:
            json.dump(self.tasks, file)

    def refresh_taSKS(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def add_TAsk(self):
        task = self.task_input.get()
        if task:
            self.tasks.append(task)
            self.save_TASK()
            self.refresh_taSKS()
            self.task_input.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def update_Task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.tasks[selected_index] = self.task_input.get()
            self.save_TASK()
            self.refresh_taSKS()
            self.task_input.delete(0, tk.END)
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to update.")

    def remove_TASk(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_index]
            self.save_TASK()
            self.refresh_taSKS()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to remove.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TODOLIst(root)
    root.mainloop()
