from datetime import datetime

# 📥 1. Get user input
dob_input = input("Enter your date of birth (DD-MM-YYYY): ")

try:
    # 🧠 2. Convert to datetime object
    dob = datetime.strptime(dob_input, "%d-%m-%Y")
    today = datetime.now()

    # 📏 3. Calculate age
    age_years = (today - dob).days // 365
    total_days = (today - dob).days
    day_of_week = dob.strftime("%A")

    # 📤 4. Output results
    print("\n🎂 You were born on a", day_of_week)
    print("🧮 Your age is:", age_years, "years")
    print("📆 You've lived for:", total_days, "days")

except ValueError:
    print("⚠️ Invalid format. Please use DD-MM-YYYY.")
