import csv

FILENAME = "people.csv"

# 1. Write data to CSV
def write_data():
    data = [
        ["Name", "Age", "City"],
        ["Ravi", 22, "Ahmedabad"],
        ["Kavya", 25, "Rajkot"],
        ["Amit", 30, "Surat"]
    ]
    with open(FILENAME, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    print("✅ File created and data written.\n")

# 2. Read all rows
def read_data():
    print("📖 Reading All Data:")
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
    print()

# 3. Append a new person
def append_person():
    new_person = ["Dhruv", 28, "Vadodara"]
    with open(FILENAME, "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(new_person)
    print("➕ New person added.\n")

# 4. Search by name
def search_person(name):
    print(f"🔍 Searching for '{name}':")
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row[0].lower() == name.lower():
                print("🎯 Found:", row)
                return
    print("❌ Not found.\n")

# 5. Count people
def count_people():
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        next(reader)
        count = sum(1 for _ in reader)
    print(f"📊 Total people (excluding header): {count}\n")

# 6. Filter people by city
def filter_by_city(city):
    print(f"🏙️ People from {city.capitalize()}:")
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        header = next(reader)
        print(header)
        found = False
        for row in reader:
            if row[2].strip().lower() == city.lower():
                print(row)
                found = True
        if not found:
            print("❌ No matches found.\n")
    print()

# 🚀 Run all functions in order
def main():
    write_data()
    read_data()
    append_person()
    read_data()
    search_person("Amit")
    search_person("Ketan")
    count_people()
    filter_by_city("Surat")
    filter_by_city("Rajkot")

main()
