#Imports
import tkinter as tk
import matplotlib.pyplot as plt
import copy

class storeMap :
    def __init__ (self) :
        self.valarr = []
        self.labelarr = []
        self.total = 0
    def add (self,name,amount) :
        if name in self.labelarr:
            raise Exception('label previously used in this map')
        else:
            self.labelarr.append(name)
            self.valarr.append(amount)
            self.total += amount
    def remove (self,name) :
        if name in self.labelarr :
            pos = self.labelarr.index(name)
            self.total -= self.valarr[pos]
            self.valarr.remove(pos)
            self.labelarr.remove(name)
        else:
            raise Exception("Income not found.")
    def update (self,name,value) :
        if name in self.labelarr :
            self.valarr[self.labelarr.index(name)] = value
        else:
            raise Exception("Income not found.")
    def get (self,name) :
        if name in self.labelarr:
            return self.valarr[self.labelarr.index(name)]
        else:
            raise Exception("Income not found.")
    def getAll (self) :
        str = ""
        for loop in range(len(self.valarr)) :
            str += self.labelarr[loop]
            str += ','
            str += self.valarr[loop]
            str += '\n'
        return str
    def pie_chart (self) :
        plt.style.use('_mpl-gallery-nogrid')
        plt.pie(x = self.valarr, labels =self.labelarr)
        plt.show()

#Class
class ExpenseTracker:
    def __init__(self):
        self.expense = storeMap()
        self.income = storeMap()
        #self.totalincome = 0
        #self.totalexpense = 0
    def add_income (self, name, amount) :
        self.income.add(name,amount)
    def remove_income(self, name):
        self.income.remove(name)
    def update_income(self, name, amount):
        self.income.update(name,amount)
    def get_income (self, name):
        self.income.get(name)
    def get_all_expenses(self):
        return self.income.getAll
    def add_expense(self, name, amount):
        self.expense.add(name,amount)
    def remove_expense(self, name):
        self.expense.remove(name)
    def update_expense(self, name, amount):
        self.expense.update(name,amount)
    def get_expense(self, name):
        return self.expense.get(name)
    def get_all_expenses(self):
        return self.expense
    def get_residual_income (self) :
        return (self.income.total-self.expense.total)
    #Pie Charts
    def pie_chart_breakup (self) :
        expences = copy.deepcopy(self.expense)
        expences.add('residual income',self.get_residual_income())
        expences.pie_chart()

#Main
def main():
    tracker = ExpenseTracker()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("WELCOME TO EXPENSES TRACKER\nOne place to manage all your expenses!")
    while True:
        choice = input("\nWhat would you like to do?\n1. Add Expense\n2. Remove Expense\n3. Update Expense\n4. Get Expense\n5. Get All Expenses\n6. Add Income\n7. Show chart\n8. Get income graph\n9. Get expenditure graph\n10. Quit\n\nOption: ")
        if choice == "1":
            name = input("Enter expense name: ")
            amount = float(input("Enter expense amount: "))
            tracker.add_expense(name, amount)
        elif choice == "2":
            name = input("Enter expense name: ")
            tracker.remove_expense(name)
        elif choice == "3":
            name = input("Enter expense name: ")
            amount = float(input("Enter new expense amount: "))
            tracker.update_expense(name, amount)
        elif choice == "4":
            name = input("Enter expense name: ")
            print(tracker.get_expense(name))
        elif choice == "5":
            print(tracker.get_all_expenses())
        elif choice == "6" :
            name = input("Enter income source name: ")
            amount = float(input("Enter income: "))
            tracker.add_income(name, amount)
        elif choice == '7' :
            tracker.pie_chart_breakup()
        elif choice == '8' :
            tracker.income.pie_chart()
        elif choice == '9' :
            tracker.expense.pie_chart()
        elif choice == "10":
            print("THANK YOU\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            break
        else:
            print("Invalid option. Please choose again.")

main()