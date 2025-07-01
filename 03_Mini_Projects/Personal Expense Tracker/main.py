from datetime import datetime
import json
import os

# Predefined categories
categories = [
    "Food", "Groceries", "Snacks", "Medicine",
    "Auto/Taxi", "Petrol", "Rent", "Electricity Bill", "Mobile Recharge",
    "Shopping", "Entertainment", "Dining Out",
    "Books", "Online Courses", "Gifts", "Savings", "Miscellaneous"
]

date = datetime.now().strftime("%d/%m/%Y")
path = "D:\\Python\\03_Mini_Projects\\Personal Expense Tracker\\expenses.json"


def load_data():
    if os.path.exists(path):
        with open(path, 'r') as file:
            try:
                content = file.read().strip()
                data = json.loads(content) if content else []
            except json.JSONDecodeError:
                print("⚠️  JSON file is corrupt or empty. Starting with a fresh list.")
                data = []
    else:
        data = []
    return data


def show_category():
    print("\nSelect Category:")
    for i, category in enumerate(categories, start=1):
        print(f"{i}. {category}")


def add_expenses(data):
    try:
        # Get user input
        expense = float(input("Enter expense amount: ₹ "))

        if expense <= 0:
            print("❌ Amount must be greater than 0")
            return

        show_category()
        category_input = int(input("Enter category number: "))

        if not (1 <= category_input <= len(categories)):
            raise ValueError("❌ Invalid category number selected.")

        category = categories[category_input - 1]
        note = input("Enter a note or description for this expense: ")

        # Create expense record
        expense_record = {
            "date": date,
            "amount": expense,
            "category": category,
            "note": note
        }

        # Add to data and save
        data.append(expense_record)
        with open(path, 'w') as file:
            json.dump(data, file, indent=4)

        print("\n✅ Expense recorded successfully!")
        return expense, category, note

    except Exception as error:
        print("Unexpected input error:", error)


def view_all_expense(data):
    print("\n📄 View All Expenses:")
    print(f"{'Date & Time':<20} | {'Amount (₹)':<10} | {'Category':<18} | Note")
    print("-" * 80)

    for exp in data:
        print(
            f"{exp['date']:<20} | ₹{exp['amount']:<9.2f} | {exp['category']:<18} | {exp['note']}")


def View_today_expenses(data):
    print("\nView todays's expenses :")
    for exp in data:
        if (date == exp['date']):
            print(
                f"₹{exp['amount']:<9} | {exp['category']:<18} | {exp['note']}")


def filter_by_category(data):
    print("\fileter by category")
    show_category()
    category_input_for_fileter = int(input("Enter category number: "))
    category_for_fileter = categories[category_input_for_fileter - 1]
    print(f"{'Date & Time':<20} | {'Amount (₹)':<10} | {'Category':<18} | Note")
    print("-" * 80)

    for exp in data:
        if (category_for_fileter == exp['category']):
            print(
                f"{exp['date']:<20} | ₹{exp['amount']:<9.2f} | {exp['category']:<18} | {exp['note']}")


def show_total_spent(data):
    print("Show total spent")
    print("Enter 1 for today and select 2 for monthly")
    spent_input = int(input("Enter : "))
    today_spent = 0
    monthly_spent = 0
    if (spent_input == 1):
        for exp in data:
            if (date == exp['date']):
                today_spent += int(exp['amount'])
        print(today_spent)

    if (spent_input == 2):
        for exp in data:
            if (datetime.now().month == int(str(exp['date']).split("/")[1])):
                monthly_spent += int(exp['amount'])
        print(monthly_spent)


def show_menu():
    print("📋 Expense Tracker")
    print('''
1. Add new expense
2. View all expenses
3. View today's expenses
4. Filter by category
5. Show total spent
6. Exit''')


if __name__ == "__main__":
    show_menu()
    while True:
        choice = int(input("Enter Your Choice :"))

        data = load_data()
        if choice == 1:
            add_expenses(data)
            show_menu()

        if choice == 2:
            view_all_expense(data)
            show_menu()

        if choice == 3:
            View_today_expenses(data)

        if choice == 4:
            filter_by_category(data)
            show_menu()

        if choice == 5:
            show_total_spent(data)
            show_menu()

        if choice == 6:
            break
