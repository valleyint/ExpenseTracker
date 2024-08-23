import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        self.root.geometry("800x600")
        self.root.config(bg="#f0f0f0")

        self.income_data = []
        self.expense_data = []

        self.create_widgets()

    def create_widgets(self):
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(pady=10, expand=True)

        self.income_tab = self.create_income_tab()
        self.expense_tab = self.create_expense_tab()
        self.graph_tab = self.create_graph_tab()

        self.notebook.add(self.income_tab, text="Income")
        self.notebook.add(self.expense_tab, text="Expense")
        self.notebook.add(self.graph_tab, text="Graphs")

        self.header_frame = tk.Frame(self.root, bg="#333333")
        self.header_frame.pack(fill="x")

        self.header_label = tk.Label(self.header_frame, text="Expense Tracker", bg="#333333", fg="#ffffff", font=("Arial", 18))
        self.header_label.pack(pady=10)

    def create_income_tab(self):
        income_tab = tk.Frame(self.notebook)
        income_tab.config(bg="#f0f0f0")

        self.income_name_label = tk.Label(income_tab, text="Income Name:", bg="#f0f0f0", fg="#333333", font=("Arial", 12))
        self.income_name_label.grid(row=0, column=0, padx=10, pady=10)

        self.income_name_entry = tk.Entry(income_tab, width=30, bg="#ffffff", fg="#333333", font=("Arial", 12))
        self.income_name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.income_amount_label = tk.Label(income_tab, text="Income Amount:", bg="#f0f0f0", fg="#333333", font=("Arial", 12))
        self.income_amount_label.grid(row=1, column=0, padx=10, pady=10)

        self.income_amount_entry = tk.Entry(income_tab, width=30, bg="#ffffff", fg="#333333", font=("Arial", 12))
        self.income_amount_entry.grid(row=1, column=1, padx=10, pady=10)

        self.income_buttons_frame = tk.Frame(income_tab, bg="#f0f0f0")
        self.income_buttons_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.add_income_button = tk.Button(self.income_buttons_frame, text="Add Income", command=self.add_income, bg="#4CAF50", fg="#fff", font=("Arial", 12))
        self.add_income_button.pack(side="left", padx=10)

        self.remove_income_button = tk.Button(self.income_buttons_frame, text="Remove Income", command=self.remove_income, bg="#f44336", fg="#fff", font=("Arial", 12))
        self.remove_income_button.pack(side="left", padx=10)

        self.update_income_button = tk.Button(self.income_buttons_frame, text="Update Income", command=self.update_income, bg="#2196F3", fg="#fff", font=("Arial", 12))
        self.update_income_button.pack(side="left", padx=10)

        self.get_income_button = tk.Button(self.income_buttons_frame, text="Get Income", command=self.show_income, bg="#009688", fg="#fff", font=("Arial", 12))
        self.get_income_button.pack(side="left", padx=10)

        return income_tab

    def create_expense_tab(self):
        expense_tab = tk.Frame(self.notebook)
        expense_tab.config(bg="#f0f0f0")

        self.expense_name_label = tk.Label(expense_tab, text="Expense Name:", bg="#f0f0f0", fg="#333333", font=("Arial", 12))
        self.expense_name_label.grid(row=0, column=0, padx=10, pady=10)

        self.expense_name_entry = tk.Entry(expense_tab, width=30, bg="#ffffff", fg="#333333", font=("Arial", 12))
        self.expense_name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.expense_amount_label = tk.Label(expense_tab, text="Expense Amount:", bg="#f0f0f0", fg="#333333", font=("Arial", 12))
        self.expense_amount_label.grid(row=1, column=0, padx=10, pady=10)

        self.expense_amount_entry = tk.Entry(expense_tab, width=30, bg="#ffffff", fg="#333333", font=("Arial", 12))
        self.expense_amount_entry.grid(row=1, column=1, padx=10, pady=10)

        self.expense_buttons_frame = tk.Frame(expense_tab, bg="#f0f0f0")
        self.expense_buttons_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.add_expense_button = tk.Button(self.expense_buttons_frame, text="Add Expense", command=self.add_expense, bg="#4CAF50", fg="#fff", font=("Arial", 12))
        self.add_expense_button.pack(side="left", padx=10)

        self.remove_expense_button = tk.Button(self.expense_buttons_frame, text="Remove Expense", command=self.remove_expense, bg="#f44336", fg="#fff", font=("Arial", 12))
        self.remove_expense_button.pack(side="left", padx=10)

        self.update_expense_button = tk.Button(self.expense_buttons_frame, text="Update Expense", command=self.update_expense, bg="#2196F3", fg="#fff", font=("Arial", 12))
        self.update_expense_button.pack(side="left", padx=10)

        self.get_expense_button = tk.Button(self.expense_buttons_frame, text="Get Expense", command=self.show_expense, bg="#009688", fg="#fff", font=("Arial", 12))
        self.get_expense_button.pack(side="left", padx=10)

        return expense_tab

    def create_graph_tab(self):
        graph_tab = tk.Frame(self.notebook)
        graph_tab.config(bg="#f0f0f0")

        self.graph_canvas = FigureCanvasTkAgg(plot.Figure(figsize=(6, 5)), master=graph_tab)
        self.graph_canvas.draw()
        self.graph_canvas.get_tk_widget().pack(side="top", fill="both", expand=True)

        self.income_graph_button = tk.Button(graph_tab, text="Income Graph", command=self.income_graph, bg="#4CAF50", fg="#fff", font=("Arial", 12))
        self.income_graph_button.pack(side="left", padx=10)

        self.expense_graph_button = tk.Button(graph_tab, text="Expense Graph", command=self.expense_graph, bg="#f44336", fg="#fff", font=("Arial", 12))
        self.expense_graph_button.pack(side="left", padx=10)

        return graph_tab

    def add_income(self):
        name = self.income_name_entry.get()
        amount = float(self.income_amount_entry.get())
        self.income_data.append((name, amount))
        self.income_name_entry.delete(0, tk.END)
        self.income_amount_entry.delete(0, tk.END)

    def remove_income(self):
        name = self.income_name_entry.get()
        for data in self.income_data:
            if data[0] == name:
                self.income_data.remove(data)
                break
        self.income_name_entry.delete(0, tk.END)
        self.income_amount_entry.delete(0, tk.END)

    def update_income(self):
        name = self.income_name_entry.get()
        amount = float(self.income_amount_entry.get())
        for i, data in enumerate(self.income_data):
            if data[0] == name:
                self.income_data[i] = (name, amount)
                break
        self.income_name_entry.delete(0, tk.END)
        self.income_amount_entry.delete(0, tk.END)

    def show_income(self):
        print("Income:")
        for data in self.income_data:
            print(f"{data[0]}: {data[1]}")

    def add_expense(self):
        name = self.expense_name_entry.get()
        amount = float(self.expense_amount_entry.get())
        self.expense_data.append((name, amount))
        self.expense_name_entry.delete(0, tk.END)
        self.expense_amount_entry.delete(0, tk.END)

    def remove_expense(self):
        name = self.expense_name_entry.get()
        for data in self.expense_data:
            if data[0] == name:
                self.expense_data.remove(data)
                break
        self.expense_name_entry.delete(0, tk.END)
        self.expense_amount_entry.delete(0, tk.END)

    def update_expense(self):
        name = self.expense_name_entry.get()
        amount = float(self.expense_amount_entry.get())
        for i, data in enumerate(self.expense_data):
            if data[0] == name:
                self.expense_data[i] = (name, amount)
                break
        self.expense_name_entry.delete(0, tk.END)
        self.expense_amount_entry.delete(0, tk.END)

    def show_expense(self):
        print("Expense:")
        for data in self.expense_data:
            print(f"{data[0]}: {data[1]}")

    def income_graph(self):
        labels = [data[0] for data in self.income_data]
        sizes = [data[1] for data in self.income_data]
        explode = [0.1 if i == 0 else 0 for i in range(len(labels))]
        fig, ax = plot.subplots()
        ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%')
        ax.axis('equal')
        self.graph_canvas.draw()

    def expense_graph(self):
        labels = [data[0] for data in self.expense_data]
        sizes = [data[1] for data in self.expense_data]
        explode = [0.1 if i == 0 else 0 for i in range(len(labels))]
        plot.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%')
        plot.show()

if __name__ == "__main__":
    root = tk.Tk()
    root.state("zoomed")
    app = ExpenseTracker(root)
    root.mainloop()