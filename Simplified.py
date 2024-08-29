#EXPENSES TRACKER


#Imports

import tkinter as tk
import matplotlib.pyplot as plot

#Class

class ExpensesTracker():

    def __init__(self, root):
        self.root = root
        self.root.title("Expenses Tracker")
        self.root.state("zoomed")
        self.root.configure(background = "black")
        self.income_name = ["salary1", "salary2", "salary3"]
        self.income_amount = [100.0, 300.0, 500.0]
        self.expense_name = ["food1", "food2", "food3"]
        self.expense_amount = [200.0, 400.0, 600.0]
        self.buttons = [1, ["INCOME", 0], ["EXPENSE", 0], ["GRAPHS", 0], ["QUIT", 0]]
        self.income_or_expense = ""
        self.width = self.root.winfo_screenwidth()
        self.intro()
        
    def intro(self):
        self.frame1 = tk.Frame(self.root, bg = "#222222")
        self.label1 = tk.Label(self.frame1, text= "EXPENSES TRACKER", font = ("Broadway", 46), anchor = "n", bg = "#222222", fg = "#ffffff").pack(pady = 15)
        self.frame2 = tk.Frame(self.root, bg = "black")
        self.entry = tk.Entry(self.root)
        self.create_buttons()
        self.frame1.pack(anchor = "n", fill = "x")
        self.frame2.pack(anchor = "n", pady = 40)

    def delete_buttons(self):
        for i in range(len(self.buttons), 1, -1):
            if isinstance(self.buttons[i-1][1], tk.Button):
                self.buttons[i-1][1].destroy()
                self.buttons.pop()

    def create_buttons(self):
        for i in range(1, len(self.buttons)):
            self.buttons[i][1] = tk.Button(self.frame2, text = self.buttons[i][0], command = lambda i=i: self.button_command(self.buttons[0], i))
            self.buttons[i][1].pack(side = "left", padx = 100, pady = 5)    

    def button_command(self, seq, num):
        if seq == 1:
            if num == 1:
                self.income_or_expense = "Income"
                self.delete_buttons()
                self.buttons = [11, ["↩", 0], ["ADD INCOME", 0], ["REMOVE INCOME", 0], ["UPDATE INCOME", 0], ["GET INCOME", 0]]
                self.create_buttons()
            elif num == 2:
                self.income_or_expense = "Expense"
                self.delete_buttons()
                self.buttons = [12, ["↩", 0], ["ADD EXPENSE", 0], ["REMOVE EXPENSE", 0], ["UPDATE EXPENSE", 0], ["GET EXPENSE", 0]]
                self.create_buttons()
            elif num == 3:
                self.delete_buttons()
                self.buttons = [13, ["↩", 0], ["INCOME CHART", 0], ["EXPENSE CHART", 0]]
                self.create_buttons()
            else:
                root.destroy()
        if seq == 11 or seq == 12:
            if num == 1:
                self.delete_buttons()
                self.buttons = [1, ["INCOME", 0], ["EXPENSE", 0], ["GRAPHS", 0], ["QUIT", 0]]
                self.create_buttons()
            elif num == 2:
                self.label_entry1 = tk.Label(self.root, text = f"Enter {self.income_or_expense} name: ")
                self.entry1 = tk.Entry(self.root)
                self.label_entry2 = tk.Label(self.root, text = f"Enter {self.income_or_expense} amount: ")
                self.entry2 = tk.Entry(self.root)
                self.button1 = tk.Button(self.root, text = "Submit", command = self.submit)
                self.label_entry1.pack()
                self.entry1.pack()
                self.label_entry2.pack()
                self.entry2.pack()
                self.button1.pack()
            elif num == 3:
                name = input(f"Enter {self.income_or_expense} name: ")
                self.remove(name)
            elif num == 4:
                name = input(f"Enter {self.income_or_expense} name: ")
                amount = float(input(f"Enter new {self.income_or_expense} amount: "))
                self.update(name, amount)
            else:
                self.label_entry1 = tk.Label(self.root, text = f"Enter {self.income_or_expense} name: ")
                self.entry1 = tk.Entry(self.root)
                self.button1 = tk.Button(self.root, text = "Submit", command = self.show)
                self.label_entry1.pack()
                self.entry1.pack()
                self.button1.pack()
        if seq == 13:
            if num == 1:
                self.delete_buttons()
                self.buttons = [1, ["INCOME", 0], ["EXPENSE", 0], ["GRAPHS", 0], ["QUIT", 0]]
                self.create_buttons()
            else:
                self.pie_chart(num)

    def submit(self):
        name = str(self.entry1.get())
        amount = float(self.entry2.get())
        self.entry1.destroy()
        self.entry2.destroy()
        self.label_entry1.configrure(text = "Successfully added!")
        self.label_entry2.destroy()
        self.add(name, amount)
        self.button1.destroy()

    def add(self, name, amount):
        if self.income_or_expense == "Income":
            if name in self.income[0][0]:
                self.income_amount[self.income[0][0].index(name)] += amount
            else:
                self.income[0][0].append(name)
                self.income_amount.append(amount)
        else:
            if name in self.expense_name:
                self.expense_amount[self.expense_name.index(name)] += amount
            else:
                self.expense_name.append(name)
                self.expense_amount.append(amount)
        print("Successfull added!\n")

    def remove(self, name):
        if self.income_or_expense == "Income":
            if name in self.income[0][0]:
                self.income_amount.remove(self.income[0][0].index(name))
                self.income[0][0].remove(name)
            else:
                print("Income not found.")
        else:
            if name in self.expense_name:
                    self.expense_amount.remove(self.expense_name.index(name))
                    self.expense_name.remove(name)
            else:
                print("Expense not found.")
        print("Successfully removed!\n")

    def update(self, name, amount):
        if self.income_or_expense == "Income":
            if name in self.income[0][0]:
                self.income_amount[self.income[0][0].index(name)] = amount
            else:
                print("Income not found.")
        else:        
            if name in self.expense_name:
                self.expense_amount[self.expense_name.index(name)] = amount
            else:
                print("Expense not found.")
        print(self.income_or_expense, "has been updated successfully.")

    def show(self):
        self.name = self.entry1.get()
        self.label_entry1.destroy()
        self.entry1.destroy()
        self.button1.destroy()
        if self.name in self.income[0][0] or self.name in self.expense_name:
            if self.income_or_expense == "Income":
                self.show_output = self.name + " : " + str(self.income_amount[self.income[0][0].index(self.name)])
            else:
                self.show_output = self.name + " : " + str(self.expense_amount[self.expense_name.index(self.name)])
        else:
            self.show_output = self.income_or_expense + " not found."
        self.label_output = tk.Label(self.root, text = self.show_output)
        self.label_output.pack()

    def pie_chart(self, type):
            plot.style.use("dark_background")
            if type == 2:
                plot.pie(self.income_amount, labels = self.income_name, wedgeprops=dict(width=0.5))
                plot.title("INCOME GRAPH")
            if type == 3:
                plot.pie(self.expense_amount, labels = self.expense_name, wedgeprops=dict(width=0.5))
                plot.title("EXPENSE GRAPH")
            plot.show()

#Main code

root = tk.Tk()
app = ExpensesTracker(root)
root.mainloop()