class ExpenseTracker:
    def __init__(self):
        self.expenses = {}

    def add_expense(self, name, amount):
        if name in self.expenses:
            self.expenses[name] += amount
        else:
            self.expenses[name] = amount

    def remove_expense(self, name):
        if name in self.expenses:
            del self.expenses[name]
        else:
            print("Expense not found.")

    def update_expense(self, name, amount):
        if name in self.expenses:
            self.expenses[name] = amount
        else:
            print("Expense not found.")

    def get_expense(self, name):
        if name in self.expenses:
            return self.expenses[name]
        else:
            print("Expense not found.")

    def get_all_expenses(self):
        return self.expenses


def main():
    tracker = ExpenseTracker()

    while True:
        print("\n1. Add Expense")
        print("2. Remove Expense")
        print("3. Update Expense")
        print("4. Get Expense")
        print("5. Get All Expenses")
        print("6. Quit")

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
        elif choice == "6":
            break
        else:
            print("Invalid option. Please choose again.")


if __name__ == "__main__":
    main()
