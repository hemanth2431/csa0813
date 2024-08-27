import json
import os

# Define file path for saving data
DATA_FILE = 'budget_data.json'

def load_data():
    """Load data from the JSON file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return {"income": [], "expenses": []}

def save_data(data):
    """Save data to the JSON file."""
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def add_income(data):
    """Add income to the budget."""
    source = input("Enter income source: ")
    amount = float(input("Enter income amount: "))
    data['income'].append({"source": source, "amount": amount})
    print(f"Income from '{source}' of amount ${amount:.2f} added.")

def add_expense(data):
    """Add expense to the budget."""
    description = input("Enter expense description: ")
    amount = float(input("Enter expense amount: "))
    data['expenses'].append({"description": description, "amount": amount})
    print(f"Expense '{description}' of amount ${amount:.2f} added.")

def view_summary(data):
    """View the budget summary."""
    total_income = sum(item['amount'] for item in data['income'])
    total_expenses = sum(item['amount'] for item in data['expenses'])
    balance = total_income - total_expenses

    print("\n--- Budget Summary ---")
    print(f"Total Income: ${total_income:.2f}")
    for income in data['income']:
        print(f"  {income['source']}: ${income['amount']:.2f}")
    
    print(f"Total Expenses: ${total_expenses:.2f}")
    for expense in data['expenses']:
        print(f"  {expense['description']}: ${expense['amount']:.2f}")

    print(f"Balance: ${balance:.2f}")

def main():
    data = load_data()
    
    while True:
        print("\n--- Budget Planner ---")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_income(data)
        elif choice == '2':
            add_expense(data)
        elif choice == '3':
            view_summary(data)
        elif choice == '4':
            save_data(data)
            print("Data saved. Exiting...")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 4.")

if __name__ == "__main__":
    main()
