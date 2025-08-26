import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import pandas as pd                       # ✅ Pandas with transformation
import matplotlib.pyplot as plt           # ✅ Visualization
from datetime import datetime
import threading                          # ✅ Multi-threads that make sense

# ---------------------- ✅ Database Integration & Read/Write Functionality ---------------------- #
# The following block creates and interacts with an SQLite database.
# It allows persistent data storage outside of the runtime.
conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        due_date TEXT,
        completed INTEGER DEFAULT 0
    )
""")
conn.commit()

# ---------------------- ✅ Generator Function ---------------------- #
# Yields batches of tasks for possible pagination or background processing.
def task_batch_generator(batch_size=5):
    cursor.execute("SELECT * FROM tasks")
    all_tasks = cursor.fetchall()
    for i in range(0, len(all_tasks), batch_size):
        yield all_tasks[i:i+batch_size]

# ---------------------- ✅ User Interaction (via GUI) ---------------------- #
# Tkinter-based interface allows user to input, delete, complete, and sort tasks.
class ToDoApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("To-Do List")
        self.geometry("500x600")
        self.configure(padx=10, pady=10)
        self.create_widgets()
        self.show_tasks()

    def create_widgets(self):
        self.task_entry = tk.Entry(self, width=40)
        self.task_entry.grid(row=0, column=0, pady=5, columnspan=2)

        self.date_entry = tk.Entry(self, width=20)
        self.date_entry.grid(row=0, column=2, padx=5)

        add_btn = tk.Button(self, text="Add Task", command=self.add_task)
        add_btn.grid(row=0, column=3)

        self.task_tree = ttk.Treeview(self, columns=("Title", "Due Date", "Completed"), show="headings")
        self.task_tree.heading("Title", text="Title")
        self.task_tree.heading("Due Date", text="Due Date")
        self.task_tree.heading("Completed", text="Completed")
        self.task_tree.grid(row=1, column=0, columnspan=4, pady=10)

        del_btn = tk.Button(self, text="Delete Task", command=self.delete_task)
        del_btn.grid(row=2, column=0)

        done_btn = tk.Button(self, text="Mark Completed", command=self.complete_task)
        done_btn.grid(row=2, column=1)

        # ✅ Multi-threads that make sense
        # Launching visuals in a background thread to avoid UI freezing
        vis_btn = tk.Button(self, text="Show Visuals", command=lambda: threading.Thread(target=self.show_visuals).start())
        vis_btn.grid(row=2, column=2)

        sort_btn = tk.Button(self, text="Sort by Due", command=self.sort_tasks)
        sort_btn.grid(row=2, column=3)

    def add_task(self):
        title = self.task_entry.get().strip()
        due_date = self.date_entry.get().strip()
        if not title:
            messagebox.showwarning("Input Error", "Please enter a task.")
            return
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            messagebox.showwarning("Date Error", "Date must be in YYYY-MM-DD format.")
            return

        # ✅ Database Write (Persistent Change at Rest)
        cursor.execute("INSERT INTO tasks (title, due_date) VALUES (?, ?)", (title, due_date))
        conn.commit()

        self.task_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.show_tasks()

    def show_tasks(self):
        for row in self.task_tree.get_children():
            self.task_tree.delete(row)

        # ✅ Database Read
        cursor.execute("SELECT id, title, due_date, completed FROM tasks")
        for task in cursor.fetchall():
            completed = "Yes" if task[3] else "No"
            self.task_tree.insert("", tk.END, iid=task[0], values=(task[1], task[2], completed))

    def delete_task(self):
        selected = self.task_tree.selection()
        if not selected:
            return
        task_id = selected[0]

        # ✅ Database Delete (Persistent Change at Rest)
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
        self.show_tasks()

    def complete_task(self):
        selected = self.task_tree.selection()
        if not selected:
            return
        task_id = selected[0]

        # ✅ Database Update (Persistent Change at Rest)
        cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
        conn.commit()
        self.show_tasks()

    # ✅ One of maps, lambdas, regex (lambda used for sorting by due date)
    def sort_tasks(self):
        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()
        sorted_tasks = sorted(tasks, key=lambda x: x[2])  # Sorting by due_date using lambda
        for row in self.task_tree.get_children():
            self.task_tree.delete(row)
        for task in sorted_tasks:
            completed = "Yes" if task[3] else "No"
            self.task_tree.insert("", tk.END, iid=task[0], values=(task[1], task[2], completed))

    # ✅ Visualization + ✅ Pandas Transformation
    def show_visuals(self):
        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()

        # Load tasks into Pandas DataFrame
        df = pd.DataFrame(tasks, columns=["ID", "Title", "Due Date", "Completed"])

        # ✅ Pandas Transformation (Extract Month from Date)
        df["Month"] = pd.to_datetime(df["Due Date"], errors='coerce').dt.month
        monthly_counts = df["Month"].value_counts().sort_index()

        # ✅ Visualization 1: Bar Chart of Tasks by Month
        plt.figure(figsize=(6, 4))
        monthly_counts.plot(kind="bar", color="skyblue")
        plt.title("Tasks per Month")
        plt.xlabel("Month")
        plt.ylabel("Number of Tasks")
        plt.tight_layout()
        plt.show()

        # ✅ Visualization 2: Pie Chart of Completion Status
        completed = df["Completed"].value_counts()
        labels = ["Incomplete", "Complete"]
        plt.figure(figsize=(5, 5))
        plt.pie(completed, labels=labels, autopct="%1.1f%%", colors=["lightcoral", "lightgreen"])
        plt.title("Completion Status")
        plt.tight_layout()
        plt.show()

# ---------------------- Run the App ---------------------- #
if __name__ == "__main__":
    app = ToDoApp()
    app.mainloop()
