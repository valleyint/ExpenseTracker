#EXPENSES TRACKER


#Imports

from tkinter import *
from tkinter import ttk
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
        self.button_names = ["INCOME", "EXPENSE", "GRAPHS", "QUIT"]
        self.button_list = []
        self.income_or_expense = ""
        self.root.title("Expenses Tracker")
        self.root.config(bg = "#333333")
        self.root.state("zoomed")
        self.intro()
        
    def intro(self):
        self.notebook = ttk.Notebook(root)
        self.frame = ttk.Frame(self.notebook)
        self.create_buttons()
        self.frame.pack(padx = 5, pady = 5)
        self.notebook.add(self.frame)
        self.notebook.pack(padx = 5, pady = 5)
        while (self.Loops[1] == True) and (self.income_or_expense == "Income" or self.income_or_expense == "Expense") and (self.Loops[0] == True):
            self.choice = input(f"\nWhat would you like to do?\n1. Add {self.income_or_expense}\n2. Remove {self.income_or_expense}\n3. Update {self.income_or_expense}\n4. Get {self.income_or_expense}\n5. Get All {self.income_or_expense}\n6. Return\n7. Quit\n\nChoice: ")
            print()
            self.option()

    def button_command(self, num):
        if num == 0:
            self.income_or_expense = "Income"
            self.button_names[0] == "blah"
        elif num == 1:
            self.income_or_expense = "Expense"
        elif num == 2:
            self.pie_chart(input("Do you wish to see:\n1. Income chart\n2. Expense chart\n\nChoice: "))
        else:
            root.destroy()

    def create_buttons(self):
        for i in range(len(self.button_names)):
            self.button_list.append(Button(self.frame, text = self.button_names[i], command = lambda: self.button_command(frozenset(i))))
            self.button_list[i].pack(padx = 5, pady = 5)

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

    def pie_chart(self, type) :
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

#Main code

root = Tk()
app = ExpensesTracker(root)
root.mainloop()