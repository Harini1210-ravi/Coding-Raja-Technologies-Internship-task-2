import os
import json
from collections import defaultdict

# Function to load transactions from file
def load_transactions():
    if os.path.exists("transactions.json"):
        with open("transactions.json", "r") as file:
            return json.load(file)
    else:
        return {"expenses": [], "income": []}

# Function to save transactions to file
def save_transactions(transactions):
    with open("transactions.json", "w") as file:
        json.dump(transactions, file, indent=4)

# Function to record an expense
def record_expense(transactions):
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    transactions["expenses"].append({"category": category, "amount": amount})
    save_transactions(transactions)
    print("Expense recorded successfully.")

# Function to record income
def record_income(transactions):
    amount = float(input("Enter income amount: "))
    transactions["income"].append(amount)
    save_transactions(transactions)
    print("Income recorded successfully.")

# Function to calculate total income
def calculate_income(transactions):
    return sum(transactions["income"])

# Function to calculate total expenses
def calculate_expenses(transactions):
    return sum(item["amount"] for item in transactions["expenses"])

# Function to calculate remaining budget
def calculate_budget(transactions):
    return calculate_income(transactions) - calculate_expenses(transactions)

# Function to analyze expenses by category
def analyze_expenses(transactions):
    expense_categories = defaultdict(float)
    for expense in transactions["expenses"]:
        expense_categories[expense["category"]] += expense["amount"]
    
    print("\nExpense Analysis:")
    for category, amount in expense_categories.items():
        print(f"{category}: {amount}")
        
# Main function
def main():
    transactions = load_transactions()
    while True:
        print("\n===== Budget Tracker Menu =====")
        print("1. Record Expense")
        print("2. Record Income")
        print("3. View Budget Summary")
        print("4. Analyze Expenses")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            record_expense(transactions)
        elif choice == "2":
            record_income(transactions)
        elif choice == "3":
            print("\n===== Budget Summary =====")
            print(f"Total Income: {calculate_income(transactions)}")
            print(f"Total Expenses: {calculate_expenses(transactions)}")
            print(f"Remaining Budget: {calculate_budget(transactions)}")
        elif choice == "4":
            analyze_expenses(transactions)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
