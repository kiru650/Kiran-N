class Expense:
    def __init__(self, date, category, amount, description):
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description

expenses = []

def add_expense(date, category, amount, description):
    expense = Expense(date, category, amount, description)
    expenses.append(expense)
    print("Expense added successfully.")

def view_expenses():
    if not expenses:
        print("No expenses recorded.")
    else:
        for expense in expenses:
            print(f"Date: {expense.date}, Category: {expense.category}, Amount: ${expense.amount:.2f}, Description: {expense.description}")

def summarize_expenses():
    if not expenses:
        print("No expenses to summarize.")
    else:
        total = sum(expense.amount for expense in expenses)
        print(f"Total expenses: ${total:.2f}")
        
        categories = {}
        for expense in expenses:
            if expense.category in categories:
                categories[expense.category] += expense.amount
            else:
                categories[expense.category] = expense.amount
        
        print("\nExpenses by category:")
        for category, amount in categories.items():
            print(f"{category}: ${amount:.2f}")

def main():
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Summarize Expenses")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")
            add_expense(date, category, amount, description)
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            summarize_expenses()
        elif choice == '4':
            print("Thank you for using the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
