#EXPENSES TRACKER


#Imports

import tkinter
import ttkbootstrap as ttkb
import matplotlib.pyplot as plot

#Class

class ExpensesTracker():

    def __init__(self, root):
        self.root = root
        self.income_name = ["salary1", "salary2", "salary3"]
        self.income_amount = [100.0, 300.0, 500.0]
        self.expense_name = ["food1", "food2", "food3"]
        self.expense_amount = [200.0, 400.0, 600.0]
        self.button_names = [1, "INCOME", "EXPENSE", "GRAPHS", "QUIT"]
        self.button_list = []
        self.income_or_expense = ""
        self.root.title("Expenses Tracker")
        self.root.state("zoomed")
        self.intro()
        
    def intro(self):
        self.stly = ttkb.Style()
        self.frame1 = ttkb.Frame(self.root)
        self.label1 = ttkb.Label(self.frame1, text= "EXPENSES TRACKER", font = ("Helvetica", 28), bootstyle = "cosmo", anchor = "n")
        self.label1.pack(pady = 50)
        self.frame1.pack(anchor = "n", fill = "x")
        self.frame2 = ttkb.Frame(self.root)
        self.entry = ttkb.Entry(self.root)
        self.create_buttons()
        self.frame2.pack(anchor = "n", fill = "x")

    def create_buttons(self):
        for j in range(len(self.button_list), 0, -1):
            self.button_list[j-1].destroy()
            self.button_list.pop()
        for i in range(1, len(self.button_names)):
            self.button_list.append(ttkb.Button(self.frame2, text = self.button_names[i], command = lambda i=i: self.button_command(str(self.button_names[0]), i), bootstyle = ("warning", "outline")))
            self.button_list[i-1].pack(side = "left", padx = 100, pady = 5)    

    def button_command(self, seq, num):
        if seq == "1":
            if num == 1:
                self.income_or_expense = "Income"
                self.button_names = [11, "↩", "ADD INCOME", "REMOVE INCOME", "UPDATE INCOME", "GET INCOME"]
                self.create_buttons()
            elif num == 2:
                self.income_or_expense = "Expense"
                self.button_names = [12, "↩", "ADD EXPENSE", "REMOVE EXPENSE", "UPDATE EXPENSE", "GET EXPENSE"]
                self.create_buttons()
            elif num == 3:
                self.button_names = [13, "↩", "INCOME CHART", "EXPENSE CHART"]
                self.create_buttons()
            else:
                root.destroy()
        if seq == "11" or seq == "12":
            if num == 1:
                self.button_names = [1, "INCOME", "EXPENSE", "GRAPHS", "QUIT"]
                self.label_output.destroy()
                self.label_entry1.destroy()
                self.create_buttons()
            elif num == 2:
                self.label_entry1 = ttkb.Label(self.root, text = f"Enter {self.income_or_expense} name: ")
                self.entry1 = ttkb.Entry(self.root)
                self.label_entry2 = ttkb.Label(self.root, text = f"Enter {self.income_or_expense} amount: ")
                self.entry2 = ttkb.Entry(self.root)
                self.button1 = ttkb.Button(self.root, text = "Submit", command = self.submit, bootstyle = ("warning", "outline"))
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
                self.label_entry1 = ttkb.Label(self.root, text = f"Enter {self.income_or_expense} name: ")
                self.entry1 = ttkb.Entry(self.root)
                self.button1 = ttkb.Button(self.root, text = "Submit", command = self.show)
                self.label_entry1.pack()
                self.entry1.pack()
                self.button1.pack()
        if seq == "13":
            if num == 1:
                self.button_names = [1, "INCOME", "EXPENSE", "GRAPHS", "QUIT"]
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
            if name in self.income_name:
                self.income_amount[self.income_name.index(name)] += amount
            else:
                self.income_name.append(name)
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
            if name in self.income_name:
                self.income_amount.remove(self.income_name.index(name))
                self.income_name.remove(name)
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
            if name in self.income_name:
                self.income_amount[self.income_name.index(name)] = amount
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
        if self.name in self.income_name or self.name in self.expense_name:
            if self.income_or_expense == "Income":
                self.show_output = self.name + " : " + str(self.income_amount[self.income_name.index(self.name)])
            else:
                self.show_output = self.name + " : " + str(self.expense_amount[self.expense_name.index(self.name)])
        else:
            self.show_output = self.income_or_expense + " not found."
        self.label_output = ttkb.Label(self.root, text = self.show_output)
        self.label_output.pack()

    def pie_chart(self, type):
            self.canvas = ttkb.Canvas()
            plot.style.use("dark_background")
            if type == 2:
                plot.pie(self.income_amount, labels = self.income_name, wedgeprops=dict(width=0.5))
                plot.title("INCOME GRAPH")
            if type == 3:
                plot.pie(self.expense_amount, labels = self.expense_name, wedgeprops=dict(width=0.5))
                plot.title("EXPENSE GRAPH")
            plot.show()
            self.canvas.pack()

#Main code

root = ttkb.Window(themename = "darkly")
app = ExpensesTracker(root)
root.mainloop()