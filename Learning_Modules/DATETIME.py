from datetime import datetime,date

#  Print today’s date and time in format:
# 📅 DD-MM-YYYY  
# ⏰ HH:MM:SS  
now = datetime.now()
print("📅 Date:", now.strftime("%d-%m-%Y"))
print("⏰ Time:", now.strftime("%H:%M:%S"))

# Get just the current year, month, and day as separate values

today = date.today()
print("📆 Year:", today.year)
print("📆 Month:", today.month)
print("📆 Day:", today.day)

# . Convert string "05-06-2025" into a datetime object
date_str = "05-06-2025"
dt_obj = datetime.strptime(date_str, "%d-%m-%Y")
print("🎯 Converted:", dt_obj)

# Calculate number of days between two dates

d1 = datetime.strptime("31-07-2024" , "%d-%m-%Y")
d2 = datetime.strptime("28-06-2025" , "%d-%m-%Y")
# d2 = date.today()
delta = d2 - d1
print("📏 Days difference:", delta.days)


# Calculate age of person born on "14-03-2000"
dob = datetime.strptime("14-03-2000" , "%d-%m-%Y")
today = datetime.today()

age_years = (today - dob).days // 365
print("🎂 Age:", age_years, "years") 