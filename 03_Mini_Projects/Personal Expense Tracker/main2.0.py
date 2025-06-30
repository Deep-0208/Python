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

# Get current date
current_date = datetime.now().strftime("%d/%m/%Y")
path = "expenses.json"  # Simplified path for better portability


def load_data():
    """Load expense data from JSON file"""
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


def save_data(data):
    """Save expense data to JSON file"""
    with open(path, 'w') as file:
        json.dump(data, file, indent=4)


def show_category():
    """Display available categories"""
    print("\nSelect Category:")
    for i, category in enumerate(categories, start=1):
        print(f"{i}. {category}")


def add_expenses(data):
    """Add a new expense record"""
    try:
        # Get user input
        expense = float(input("Enter expense amount: ₹ "))
        
        if expense <= 0:
            print("❌ Amount must be greater than 0")
            return
        
        show_category()
        category_input = int(input("Enter category number: "))
        
        if not (1 <= category_input <= len(categories)):
            print("❌ Invalid category number selected.")
            return
        
        category = categories[category_input - 1]
        note = input("Enter a note or description for this expense: ")
        
        # Create expense record
        expense_record = {
            "date": current_date,
            "amount": expense,
            "category": category,
            "note": note
        }
        
        # Add to data and save
        data.append(expense_record)
        save_data(data)
        
        print("\n✅ Expense recorded successfully!")
        
    except ValueError:
        print("❌ Invalid input. Please enter valid numbers.")
    except Exception as e:
        print(f"❌ Error adding expense: {e}")


def view_all_expense(data):
    """View all expenses"""
    if not data:
        print("\n📄 No expenses recorded yet.")
        return
    
    print("\n📄 View All Expenses:")
    print(f"{'Date':<12} | {'Amount (₹)':<10} | {'Category':<18} | Note")
    print("-" * 70)
    
    total = 0
    for exp in data:
        print(f"{exp['date']:<12} | ₹{exp['amount']:<9.2f} | {exp['category']:<18} | {exp['note']}")
        total += exp['amount']
    
    print("-" * 70)
    print(f"{'TOTAL':<12} | ₹{total:<9.2f}")


def view_today_expenses(data):
    """View today's expenses"""
    today_expenses = [exp for exp in data if exp['date'] == current_date]
    
    if not today_expenses:
        print(f"\n📅 No expenses recorded for today ({current_date}).")
        return
    
    print(f"\n📅 Today's Expenses ({current_date}):")
    print(f"{'Amount (₹)':<10} | {'Category':<18} | Note")
    print("-" * 50)
    
    total = 0
    for exp in today_expenses:
        print(f"₹{exp['amount']:<9.2f} | {exp['category']:<18} | {exp['note']}")
        total += exp['amount']
    
    print("-" * 50)
    print(f"Total Today: ₹{total:.2f}")


def filter_by_category(data):
    """Filter expenses by category"""
    if not data:
        print("\n📄 No expenses recorded yet.")
        return
    
    try:
        print("\nFilter by category:")
        show_category()
        category_input = int(input("Enter category number: "))
        
        if not (1 <= category_input <= len(categories)):
            print("❌ Invalid category number selected.")
            return
        
        selected_category = categories[category_input - 1]
        filtered_expenses = [exp for exp in data if exp['category'] == selected_category]
        
        if not filtered_expenses:
            print(f"\n📄 No expenses found for category: {selected_category}")
            return
        
        print(f"\n📄 Expenses for Category: {selected_category}")
        print(f"{'Date':<12} | {'Amount (₹)':<10} | Note")
        print("-" * 50)
        
        total = 0
        for exp in filtered_expenses:
            print(f"{exp['date']:<12} | ₹{exp['amount']:<9.2f} | {exp['note']}")
            total += exp['amount']
        
        print("-" * 50)
        print(f"Category Total: ₹{total:.2f}")
        
    except ValueError:
        print("❌ Invalid input. Please enter a valid number.")


def show_total_spent(data):
    """Show total amount spent"""
    if not data:
        print("\n💰 No expenses recorded yet.")
        return
    
    try:
        print("\n💰 Show Total Spent")
        print("1. Today's total")
        print("2. This month's total")
        print("3. Overall total")
        
        spent_input = int(input("Enter your choice (1-3): "))
        
        if spent_input == 1:
            # Today's total
            today_total = sum(exp['amount'] for exp in data if exp['date'] == current_date)
            print(f"\n📅 Today's Total ({current_date}): ₹{today_total:.2f}")
            
        elif spent_input == 2:
            # This month's total
            current_month = datetime.now().month
            current_year = datetime.now().year
            monthly_total = 0
            
            for exp in data:
                exp_date = datetime.strptime(exp['date'], "%d/%m/%Y")
                if exp_date.month == current_month and exp_date.year == current_year:
                    monthly_total += exp['amount']
            
            print(f"\n📅 This Month's Total: ₹{monthly_total:.2f}")
            
        elif spent_input == 3:
            # Overall total
            overall_total = sum(exp['amount'] for exp in data)
            print(f"\n📊 Overall Total: ₹{overall_total:.2f}")
            
        else:
            print("❌ Invalid choice. Please select 1, 2, or 3.")
            
    except ValueError:
        print("❌ Invalid input. Please enter a valid number.")


def show_summary(data):
    """Show expense summary by category"""
    if not data:
        print("\n📊 No expenses recorded yet.")
        return
    
    print("\n📊 Expense Summary by Category:")
    print(f"{'Category':<18} | {'Total (₹)':<10} | {'Count':<5}")
    print("-" * 40)
    
    category_totals = {}
    for exp in data:
        category = exp['category']
        if category not in category_totals:
            category_totals[category] = {'total': 0, 'count': 0}
        category_totals[category]['total'] += exp['amount']
        category_totals[category]['count'] += 1
    
    # Sort by total amount (descending)
    sorted_categories = sorted(category_totals.items(), key=lambda x: x[1]['total'], reverse=True)
    
    overall_total = 0
    for category, data_dict in sorted_categories:
        print(f"{category:<18} | ₹{data_dict['total']:<9.2f} | {data_dict['count']:<5}")
        overall_total += data_dict['total']
    
    print("-" * 40)
    print(f"{'TOTAL':<18} | ₹{overall_total:<9.2f}")


def show_menu():
    """Display main menu"""
    print("\n" + "="*50)
    print("📋 PERSONAL EXPENSE TRACKER")
    print("="*50)
    print("1. Add new expense")
    print("2. View all expenses")
    print("3. View today's expenses")
    print("4. Filter by category")
    print("5. Show total spent")
    print("6. Show expense summary")
    print("7. Exit")
    print("="*50)


def main():
    """Main application loop"""
    print("Welcome to Personal Expense Tracker! 💰")
    
    while True:
        show_menu()
        
        try:
            choice = int(input("\nEnter your choice (1-7): "))
            
            # Load data fresh each time to ensure consistency
            data = load_data()
            
            if choice == 1:
                add_expenses(data)
                
            elif choice == 2:
                view_all_expense(data)
                
            elif choice == 3:
                view_today_expenses(data)
                
            elif choice == 4:
                filter_by_category(data)
                
            elif choice == 5:
                show_total_spent(data)
                
            elif choice == 6:
                show_summary(data)
                
            elif choice == 7:
                print("\n👋 Thank you for using Personal Expense Tracker!")
                print("Stay financially organized! 💪")
                break
                
            else:
                print("❌ Invalid choice. Please select a number between 1-7.")
                
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ An error occurred: {e}")
        
        # Pause before showing menu again
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()