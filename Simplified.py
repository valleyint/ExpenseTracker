#EXPENSES TRACKER


#Imports

import tkinter as tk
import matplotlib.pyplot as plot
import csv

#Global Variables

Loops = [True, True]
income_name = ["salary1", "salary2", "salary3"]
income_amount = [100.0, 300.0, 500.0]
expense_name = ["food1", "food2", "food3"]
expense_amount = [200.0, 400.0, 600.0]

#Functions

def option():
    if choice in "1234567":
        if choice == "1":
            name = input(f"Enter {income_or_expense} name: ")
            amount = float(input(f"Enter {income_or_expense} amount: "))
            add(name, amount)
        elif choice == "2":
            name = input(f"Enter {income_or_expense} name: ")
            remove(name)
        elif choice == "3":
            name = input(f"Enter {income_or_expense} name: ")
            amount = float(input(f"Enter new {income_or_expense} amount: "))
            update(name, amount)
        elif choice == "4":
            name = input(f"Enter {income_or_expense} name: ")
            show(name)
        elif choice == "5":
            show("everything")
        elif choice == "6":
            Loops[1] = False
        else:
            print("THANK YOU\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            Loops[0] = False
            Loops[1] = False
    else:
        print("Invalid option. Please choose again.")

def add(name, amount):
    if income_or_expense == "Income":
        if name in income_name:
            income_amount[income_name.index(name)] += amount
        else:
            income_name.append(name)
            income_amount.append(amount)
    else:
        if name in expense_name:
            expense_amount[expense_name.index(name)] += amount
        else:
            expense_name.append(name)
            expense_amount.append(amount)
    print("Successfull added!\n")

def remove(name):
    if income_or_expense == "Income":
        if name in income_name:
            income_amount.remove(income_name.index(name))
            income_name.remove(name)
        else:
            print("Income not found.")
    else:
        if name in expense_name:
                expense_amount.remove(expense_name.index(name))
                expense_name.remove(name)
        else:
            print("Expense not found.")
    print("Successfully removed!\n")

def update(name, amount):
    if income_or_expense == "Income":
        if name in income_name:
            income_amount[income_name.index(name)] = amount
        else:
            print("Income not found.")
    else:        
        if name in expense_name:
            expense_amount[expense_name.index(name)] = amount
        else:
            print("Expense not found.")
    print(income_or_expense, "has been updated successfully.")

def show(name):
    if name in income_name or name in expense_name or name == "everything":
        if income_or_expense == "Income":
            if name == "everything":
                print("-------------------------------------")
                for i in range(len(income_name)):
                    print(income_name[i], ":", income_amount[i])
                print("-------------------------------------")

            else:
                print(name, ":", income_amount[income_name.index(name)])
        else:
            if name == "everything":
                print("-------------------------------------")
                for i in range(len(expense_name)):
                    print(expense_name[i], ":", expense_amount[i])
                print("-------------------------------------")

            else:
                print(name, ":", expense_amount[expense_name.index(name)])
    else:
        print(income_or_expense, "not found.")

def pie_chart(type) :
        plot.style.use("dark_background")
        if type == "1":
            plot.pie(income_amount, labels = income_name, wedgeprops=dict(width=0.5))
            plot.title("INCOME GRAPH")
        elif type == "2":
            plot.pie(expense_amount, labels = expense_name, wedgeprops=dict(width=0.5))
            plot.title("EXPENSE GRAPH")
        else:
            print("Error")
        plot.show()

#Main code

print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("WELCOME TO EXPENSES TRACKER\nOne place to manage all your expenses!")
while Loops[0] == True:
    Loops[1] = True
    while True:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        income_or_expense = input("1. Income\n2. Expense\n3. Overall\n4. Graphs\n5. Quit\n\nChoice: ")
        if income_or_expense == "1":
            income_or_expense = "Income"
            break
        elif income_or_expense == "2":
            income_or_expense = "Expense"
            break
        elif income_or_expense == "4":
            pie_chart(input("Do you wish to see:\n1. Income chart\n2. Expense chart\n\nChoice: "))
        elif income_or_expense == "5":
            print("\nTHANK YOU\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            Loops[0] = False
            break
        else:
            print("Error in input, please try again.")
    while (Loops[1] == True) and (income_or_expense == "Income" or income_or_expense == "Expense") and (Loops[0] == True):
        choice = input(f"\nWhat would you like to do?\n1. Add {income_or_expense}\n2. Remove {income_or_expense}\n3. Update {income_or_expense}\n4. Get {income_or_expense}\n5. Get All {income_or_expense}\n6. Return\n7. Quit\n\nChoice: ")
        print()
        option()