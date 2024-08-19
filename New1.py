

import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plot

class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        self.root.geometry("800x600")
        self.root.config(bg="#f0f0f0")

        self.income_name = []
        self.income_amount = []
        self.expense_name = []
        self.expense_amount = []

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
        expense_tab.config(bg="#ffcccc")

        tk.Label(expense_tab, text="Expense Name:", bg="#ffcccc", fg="#660000").grid(row=0, column=0)
        tk.Label(expense_tab, text="Expense Amount:", bg="#ffcccc", fg="#660000").grid(row=1, column=0)

        self.expense_name_entry = tk.Entry(expense_tab, width=30, bg="#ffe6e6", fg="#660000")
        self.expense_amount_entry = tk.Entry(expense_tab, width=30, bg="#ffe6e6", fg="#660000")

        self.expense_name_entry.grid(row=0, column=1)
        self.expense_amount_entry.grid(row=1, column=1)

        tk.Button(expense_tab, text="Add Expense", command=self.add_expense, bg="#4CAF50", fg="#fff").grid(row=2, column=0)
        tk.Button(expense_tab, text="Remove Expense", command=self.remove_expense, bg="#f44336", fg="#fff").grid(row=2, column=1)
        tk.Button(expense_tab, text="Update Expense", command=self.update_expense, bg="#2196F3", fg="#fff").grid(row=3, column=0)
        tk.Button(expense_tab, text="Get Expense", command=self.show_expense, bg="#009688", fg="#fff").grid(row=3, column=1)

        return expense_tab

    def create_graph_tab(self):
        graph_tab = tk.Frame(self.notebook)
        graph_tab.config(bg="#ccffcc")

        tk.Button(graph_tab, text="Income Graph", command=self.income_graph, bg="#4CAF50", fg="#fff").grid(row=0, column=0)
        tk.Button(graph_tab, text="Expense Graph", command=self.expense_graph, bg="#f44336", fg="#fff").grid(row=0, column=1)

        return graph_tab
    
    def add_income(self):
        name = self.income_name_entry.get()
        amount = float(self.income_amount_entry.get())
        self.income_name.append(name)
        self.income_amount.append(amount)

    def remove_income(self):
        name = self.income_name_entry.get()
        if name in self.income_name:
            self.income_amount.remove(self.income_amount[self.income_name.index(name)])
            self.income_name.remove(name)

    def update_income(self):
        name = self.income_name_entry.get()
        amount = float(self.income_amount_entry.get())
        if name in self.income_name:
            self.income_amount[self.income_name.index(name)] = amount

    def show_income(self):
        name = self.income_name_entry.get()
        if name in self.income_name:
            print(f"{name}: {self.income_amount[self.income_name.index(name)]}")

    def add_expense(self):
        name = self.expense_name_entry.get()
        amount = float(self.expense_amount_entry.get())
        self.expense_name.append(name)
        self.expense_amount.append(amount)

    def remove_expense(self):
        name = self.expense_name_entry.get()
        if name in self.expense_name:
            self.expense_amount.remove(self.expense_amount[self.expense_name.index(name)])
            self.expense_name.remove(name)

    def update_expense(self):
        name = self.expense_name_entry.get()
        amount = float(self.expense_amount_entry.get())
        if name in self.expense_name:
            self.expense_amount[self.expense_name.index(name)] = amount

    def show_expense(self):
        name = self.expense_name_entry.get()
        if name in self.expense_name:
            print(f"{name}: {self.expense_amount[self.expense_name.index(name)]}")

    def income_graph(self):
        plot.pie(self.income_amount, labels=self.income_name, wedgeprops=dict(width=0.5))
        plot.title("INCOME GRAPH")
        plot.show()

    def expense_graph(self):
        plot.pie(self.expense_amount, labels=self.expense_name, wedgeprops=dict(width=0.5))
        plot.title("EXPENSE GRAPH")
        plot.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTracker(root)
    root.mainloop()