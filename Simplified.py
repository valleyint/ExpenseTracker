#EXPENSES TRACKER


#Imports

import tkinter as tk
import matplotlib.pyplot as plot
import time
from PIL import Image, ImageTk

#Class

class ExpensesTracker():

    def __init__(self, root):
        self.root = root
        self.root.title("Expenses Tracker")
        self.root.state("zoomed")
        self.root.config(background = "#2C323A")
        self.incomes = [["salary1", "salary2", "salary3"], [100.0, 300.0, 500.0]]
        self.expenses = [["food1", "food2", "food3"], [200.0, 400.0, 600.0]]
        self.buttons = [1, ["INCOME", 0], ["EXPENSE", 0], ["GRAPHS", 0], ["QUIT", 0]]
        self.income_or_expense = ""
        self.img1 = Image.open("Header.png")
        self.img1 = ImageTk.PhotoImage(self.img1)
        self.intro()
        
    def intro(self):
        self.frame1 = tk.Frame(self.root)
        self.label_header = tk.Label(self.frame1, image = self.img1, bg = "#2C323A")
        self.label_header.pack()
        self.frame1.pack(anchor = "n", fill = "x")
        self.frame2 = tk.Frame(self.root, bg = "#2C323A", )
        self.entry = tk.Entry(self.root)
        self.create_buttons()
        self.frame2.pack(anchor = "nw", pady = 40)

    def create_buttons(self):
        for i in range(1, len(self.buttons)):
            self.buttons[i][1] = tk.Button(self.frame2, text = self.buttons[i][0], command = lambda i=i: self.button_command(self.buttons[0], i), padx = 10, pady = 5, width = 15, bg = "#1C1B23", fg = "#F2DFCB", activebackground = "#F2DFCB", activeforeground = "#1C1B23")
            self.buttons[i][1].grid(row = 0, column = i, padx = 50)
    
    def delete_buttons(self):
        for i in range(len(self.buttons), 1, -1):
            if isinstance(self.buttons[i-1][1], tk.Button):
                self.buttons[i-1][1].destroy()
                self.buttons.pop()

    def button_command(self, seq, num):
        if seq == 1:
            if num == 1:
                self.income_or_expense = "Income"
                self.delete_buttons()
                self.buttons = [11, ["↩", 0], ["ADD INCOME", 0], ["REMOVE INCOME", 0], ["UPDATE INCOME", 0], ["GET INCOME", 0]]
                self.frame3 = tk.Frame(self.root, bg = "#2C323A", relief = tk.GROOVE)
                self.label1 = tk.Label(self.frame3, borderwidth=1, relief="solid", width = 20, bg = "#1C1B23", fg = "#F2DFCB")
                self.label2 = tk.Label(self.frame3, borderwidth=1, relief="solid", width = 20, bg = "#1C1B23", fg = "#F2DFCB")
                self.entry1 = tk.Entry(self.frame3, borderwidth=1, relief="solid", width = 20, bg = "#1C1B23", fg = "#F2DFCB")
                self.entry2 = tk.Entry(self.frame3, borderwidth=1, relief="solid", width = 20, bg = "#1C1B23", fg = "#F2DFCB")
                self.button1 = tk.Button(self.frame3, text = "Submit", width = 15, bg = "#1C1B23", fg = "#F2DFCB", activebackground = "#F2DFCB", activeforeground = "#1C1B23")
                self.create_buttons()
            elif num == 2:
                self.income_or_expense = "Expense"
                self.delete_buttons()
                self.buttons = [12, ["↩", 0], ["ADD EXPENSE", 0], ["REMOVE EXPENSE", 0], ["UPDATE EXPENSE", 0], ["GET EXPENSE", 0]]
                self.frame3 = tk.Frame(self.root, bg = "#2C323A")
                self.label1 = tk.Label(self.frame3, borderwidth=1, relief="solid", width = 20, bg = "#1C1B23", fg = "#F2DFCB")
                self.label2 = tk.Label(self.frame3, borderwidth=1, relief="solid", width = 20, bg = "#1C1B23", fg = "#F2DFCB")
                self.entry1 = tk.Entry(self.frame3, borderwidth=1, relief="solid", width = 20, bg = "#1C1B23", fg = "#F2DFCB", insertbackground = "#F2DFCB")
                self.entry2 = tk.Entry(self.frame3, borderwidth=1, relief="solid", width = 20, bg = "#1C1B23", fg = "#F2DFCB", insertbackground = "#F2DFCB")
                self.button1 = tk.Button(self.frame3, text = "Submit", width = 15, bg = "#1C1B23", fg = "#F2DFCB", activebackground = "#F2DFCB", activeforeground = "#1C1B23")
                self.create_buttons()
            elif num == 3:
                self.delete_buttons()
                self.buttons = [13, ["↩", 0], ["INCOME CHART", 0], ["EXPENSE CHART", 0]]
                self.create_buttons()
            else:
                root.destroy()
        if seq == 11 or seq == 12:
            if num == 1:
                self.frame3.destroy()
                self.delete_buttons()
                self.buttons = [1, ["INCOME", 0], ["EXPENSE", 0], ["GRAPHS", 0], ["QUIT", 0]]
                self.create_buttons()
            elif num == 2:
                self.label1.config(text = f"Enter {self.income_or_expense} name: ")
                self.label1.grid(row = 0, column = 0, padx = 10, pady = 10)
                self.label2.config(text = f"Enter {self.income_or_expense} amount: ")
                self.label2.grid(row = 1, column = 0, padx = 10, pady = 10)
                self.entry1.grid(row = 0, column = 1, padx = 10, pady = 10)
                self.entry2.grid(row = 1, column = 1, padx = 10, pady = 10)
                self.button1.config(command = self.add)
                self.button1.grid(row = 2, column = 0)
                self.frame3.pack()
            elif num == 3:
                self.label2.grid_forget()
                self.entry2.grid_forget()
                self.label1.config(text = f"Enter {self.income_or_expense} name: ")
                self.label1.grid(row = 0, column = 0, padx = 10, pady = 10)
                self.entry1.grid(row = 0, column = 1, padx = 10, pady = 10)
                self.button1.config(command = self.remove)
                self.button1.grid(row = 1, column = 0)
                self.frame3.pack()
            elif num == 4:
                self.label1.config(text = f"Enter {self.income_or_expense} name: ")
                self.label1.grid(row = 0, column = 0, padx = 10, pady = 10)
                self.label2.config(text = f"Enter new {self.income_or_expense} amount: ")
                self.label2.grid(row = 1, column = 0, padx = 10, pady = 10)
                self.entry1.grid(row = 0, column = 1, padx = 10, pady = 10)
                self.entry2.grid(row = 1, column = 1, padx = 10, pady = 10)
                self.button1.config(command = self.update)
                self.button1.grid(row = 2, column = 0)
                self.frame3.pack()
            else:
                self.label2.grid_forget()
                self.entry2.grid_forget()
                self.label1.config(text = "Enter income name: ")
                self.label1.grid(row = 0, column = 0, padx = 10, pady = 10)
                self.entry1.grid(row = 0, column = 1, padx = 10, pady = 10)
                self.button1.config(command = self.show)
                self.button1.grid(row = 1, column = 0, padx = 10, pady = 10)
                self.frame3.pack()

        if seq == 13:
            if num == 1:
                self.delete_buttons()
                self.buttons = [1, ["INCOME", 0], ["EXPENSE", 0], ["GRAPHS", 0], ["QUIT", 0]]
                self.create_buttons()
            else:
                self.pie_chart(num)

    def add(self):
        name = str(self.entry1.get())
        amount = float(self.entry2.get())
        self.entry1.grid_forget()
        self.entry1.delete(0, "end")
        self.entry2.grid_forget()
        self.entry2.delete(0, "end")
        self.label2.grid_forget()
        if self.income_or_expense == "Income":
            if name in self.incomes[0]:
                self.incomes[1][self.incomes[0].index(name)] += amount
            else:
                self.incomes[0].append(name)
                self.incomes[1].append(amount)
        else:
            if name in self.expenses[0]:
                self.expenses[1][self.expenses[0].index(name)] += amount
            else:
                self.expenses[0].append(name)
                self.expenses[1].append(amount)
        self.label1.config(text = "Successfully added!")
        self.button1.grid_forget()

    def remove(self):
        name = str(self.entry1.get())
        self.entry1.grid_forget()
        self.entry1.delete(0, "end")
        self.button1.grid_forget()
        if self.income_or_expense == "Income":
            if name in self.incomes[0]:
                self.incomes[1].pop(self.incomes[0].index(name))
                self.incomes[0].remove(name)
                self.label1.config(text = "Successfully removed!")
            else:
                self.label1.config(text = "Income not found.")
        else:
            if name in self.expenses[0]:
                self.expenses[1].remove(self.expenses[0].index(name))
                self.expenses[0].remove(name)
                self.label1.config(text = "Successfully removed!")
            else:
                self.label1.config(text = "Expense not found.")

    def update(self):
        name = str(self.entry1.get())
        amount = float(self.entry2.get())
        self.entry1.grid_forget()
        self.entry1.delete(0, "end")
        self.entry2.grid_forget()
        self.entry2.delete(0, "end")
        self.label2.grid_forget()
        if self.income_or_expense == "Income":
            if name in self.incomes[0]:
                self.incomes[1][self.incomes[0].index(name)] = amount
            else:
                self.label1.config(text = "Income not found.")    
        else:
            if name in self.expenses[0]:
                self.expenses[1][self.expenses[0].index(name)] = amount
            else:
                self.label1.config(text = "Expense not found.")
        self.label1.config(text = "Successfully updated!")
        self.button1.grid_forget()

    def show(self):
        name = self.entry1.get()
        self.entry1.grid_forget()
        self.entry1.delete(0, "end")
        self.button1.grid_forget()
        if name in self.incomes[0] or name in self.expenses[0]:
            if self.income_or_expense == "Income":
                self.show_output = name + " : " + str(self.incomes[1][self.incomes[0].index(name)])
            else:
                self.show_output = name + " : " + str(self.expenses[1][self.expenses[0].index(name)])
        else:
            self.show_output = self.income_or_expense + " not found."
        self.label1.config(text = self.show_output)

    def pie_chart(self, type):
            plot.style.use("dark_background")
            if type == 2:
                plot.pie(self.incomes[1], labels = self.incomes[0], wedgeprops=dict(width=0.5))
                plot.title("INCOME GRAPH")
            if type == 3:
                plot.pie(self.expenses[1], labels = self.expenses[0], wedgeprops=dict(width=0.5))
                plot.title("EXPENSE GRAPH")
            plot.show()

#Main code

root = tk.Tk()
app = ExpensesTracker(root)
root.mainloop()