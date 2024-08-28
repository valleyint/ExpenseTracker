#EXPENSES TRACKER


#Imports

import tkinter
import ttkbootstrap as ttkb
#from tkinter import ttk
import matplotlib.pyplot as plot

#Class

class ExpensesTracker():

    def __init__(self, root):
        self.root = root
        self.Loops = [True, True]
        self.income_name = ["salary1", "salary2", "salary3"]
        self.income_amount = [100.0, 300.0, 500.0]
        self.expense_name = ["food1", "food2", "food3"]
        self.expense_amount = [200.0, 400.0, 600.0]
        self.button_names = [0, "INCOME", "EXPENSE", "GRAPHS", "QUIT"]
        self.button_list = []
        self.income_or_expense = ""
        self.root.title("Expenses Tracker")
        self.root.state("zoomed")
        self.intro()
        
    def intro(self):
        self.stly = ttkb.Style()
        self.frame1 = ttkb.Frame(self.root)
        self.label1 = ttkb.Label(self.frame1, text = "EXPENSES TRACKER", anchor = "n")
        self.label1.pack(pady = 50)
        self.frame1.pack(anchor = "n", fill = "x")
        self.frame2 = ttkb.Frame(self.root)
        self.create_buttons()
        self.frame2.pack(anchor = "n", fill = "x")

    def create_buttons(self):
        for j in range(len(self.button_list), 0, -1):
            self.button_list[j-1].destroy()
            self.button_list.pop()
        for i in range(1, len(self.button_names)+1):
            self.button_list.append(ttkb.Button(self.frame2, text = self.button_names[i-1], command = lambda i=i: self.button_command(str(self.button_names[0]), i), bootstyle = ("warning", "outline")))
            self.button_list[i-1].pack(side = "left", padx = 100, pady = 5)    

    def button_command(self, seq, num):
        if seq == "0":
            if num == 1:
                self.income_or_expense = "Income"
                self.button_names = [1, "↩", "ADD INCOME", "REMOVE INCOME", "UPDATE INCOME", "GET INCOME"]
                self.create_buttons()
            elif num == 2:
                self.income_or_expense = "Expense"
            elif num == 3:
                self.pie_chart(input("Do you wish to see:\n1. Income chart\n2. Expense chart\n\nChoice: "))
            else:
                root.destroy()
        if seq == "1":
            if num == 1:
                self.button_names = [0, "INCOME", "EXPENSE", "GRAPHS", "QUIT"]
                self.create_buttons()
            elif num == 2:
                name = input("Enter income name: ")
                amount = float(input("Enter income amount: "))
                self.add(name, amount)
            elif num == 3:
                name = input("Enter income name: ")
                self.remove(name)
            elif num == 4:
                name = input("Enter income name: ")
                amount = float(input("Enter new income amount: "))
                self.update(name, amount)
            else:
                name = input("Enter income name: ")
                self.show(name)

    def option(self):
        if self.choice in "1234567":
            if self.choice == "1":
                name = input(f"Enter {self.income_or_expense} name: ")
                amount = float(input(f"Enter {self.income_or_expense} amount: "))
                self.add(name, amount)
            elif self.choice == "2":
                name = input(f"Enter {self.income_or_expense} name: ")
                self.remove(name)
            elif self.choice == "3":
                name = input(f"Enter {self.income_or_expense} name: ")
                amount = float(input(f"Enter new {self.income_or_expense} amount: "))
                self.update(name, amount)
            elif self.choice == "4":
                name = input(f"Enter {self.income_or_expense} name: ")
                self.show(name)
            elif self.choice == "5":
                self.show("everything")
            elif self.choice == "6":
                self.Loops[1] = False
            else:
                print("THANK YOU\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                self.Loops[0] = False
                self.Loops[1] = False
        else:
            print("Invalid option. Please choose again.")

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

    def show(self, name):
        if name in self.income_name or name in self.expense_name or name == "everything":
            if self.income_or_expense == "Income":
                if name == "everything":
                    print("-------------------------------------")
                    for i in range(len(self.income_name)):
                        print(self.income_name[i], ":", self.income_amount[i])
                    print("-------------------------------------")

                else:
                    print(name, ":", self.income_amount[self.income_name.index(name)])
            else:
                if name == "everything":
                    print("-------------------------------------")
                    for i in range(len(self.expense_name)):
                        print(self.expense_name[i], ":", self.expense_amount[i])
                    print("-------------------------------------")

                else:
                    print(name, ":", self.expense_amount[self.expense_name.index(name)])
        else:
            print(self.income_or_expense, "not found.")

    def pie_chart(self, type):
            self.canvas = ttkb.Canvas()
            plot.style.use("dark_background")
            if type == "1":
                plot.pie(self.income_amount, labels = self.income_name, wedgeprops=dict(width=0.5))
                plot.title("INCOME GRAPH")
            elif type == "2":
                plot.pie(self.expense_amount, labels = self.expense_name, wedgeprops=dict(width=0.5))
                plot.title("EXPENSE GRAPH")
            else:
                print("Error")
            plot.show()
            self.canvas.pack()

#Main code

root = ttkb.Window(themename = "darkly")
app = ExpensesTracker(root)
root.mainloop()