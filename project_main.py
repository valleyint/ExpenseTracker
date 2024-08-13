import matplotlib.pyplot as plt
import copy

class ExpenseTracker:
    def __init__(self):
        self.expenses = {}
        self.income = {}
        self.totalincome = 0
        self.totalexpense = 0
    
    def add_income (self, name,  amount) :
        self.totalincome += amount

        if name in self.income:
            self.income[name] += amount
        else:
            self.income[name] = amount

    def remove_income(self, name):
        if name in self.income:
            self.totalincome -= self.income[name]
            del self.income[name]
        else:
            print("Income not found.")

    def update_income(self, name, amount):
        if name in self.income:
            self.totalincome -= self.income[name]
            self.income[name] = amount
            self.totalincome += amount
        
        else:
            print("Income not found.")
    
    def get_income (self, name):
        if name in self.income:
            return self.income[name]
        else:
            print("Income not found.")
    
    def get_all_expenses(self):
        return self.income
    
    def add_expense(self, name, amount):
        self.totalexpense += amount
        if name in self.expenses:
            self.expenses[name] += amount
        else:
            self.expenses[name] = amount
    
    def remove_expense(self, name):
        if name in self.expenses:
            self.totalexpense -= self.expenses[name]
            del self.expenses[name]
        else:
            print("Expense not found.")
    
    def update_expense(self, name, amount):
        if name in self.expenses:
            self.totalincome -= self.income[name]
            self.expenses[name] = amount
            self.totalincome += amount
            
        else:
            print("Expense not found.")
    
    def get_expense(self, name):
        if name in self.expenses:
            return self.expenses[name]
        else:
            print("Expense not found.")
    
    def get_all_expenses(self):
        return self.expenses
    
    def get_residual_income (self) :
        difference = (self.totalincome-self.totalexpense)
        return difference

def pie_chart (exp) :
    expences = {}
    expences = copy.deepcopy(exp.expenses)
    expences['residual_income'] = exp.get_residual_income()

    labels = []
    sizes = []

    for x, y in expences.items() :
        labels.append(x)
        sizes.append(y)
    
    plt.style.use('_mpl-gallery-nogrid')
    plt.pie(sizes, labels=labels)

    plt.show()

def main():
    tracker = ExpenseTracker()
    while True:
        print("\n1. Add Expense\n2. Remove Expense\n3. Update Expense\n4. Get Expense\n5. Get All Expenses\n6. Add Income\n7. Show chart\n8. Quit")
        choice = input("Choose an option: ")
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
            tracker.add_income(name,amount)
        elif choice == '7' :
            pie_chart(tracker)
        elif choice == "8":
            break
        else:
            print("Invalid option. Please choose again.")
        
if __name__ == "__main__":
    main()