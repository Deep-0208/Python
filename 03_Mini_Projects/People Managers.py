import csv

FILENAME = "people.csv"

# 🔁 Load data from file (or create with header)
def load_data():
    try:
        with open(FILENAME, 'r') as file:
            reader = csv.reader(file)
            return list(reader)
    except FileNotFoundError:
        return [["Name", "Age", "City"]]  # header row

# 💾 Save data to file
def save_data(data):
    with open(FILENAME, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

# 👥 Show all people
def show_data(data):
    print("\n📄 People Data:")
    for row in data:
        print(row)
    print(f"Total people: {len(data) - 1}\n")  # excluding header

# ➕ Add a person
def add_person(data):
    name = input("Enter name: ")
    age = input("Enter age: ")
    city = input("Enter city: ")
    data.append([name, age, city])
    save_data(data)
    print("✅ Person added!\n")

# 🔍 Search person
def search_person(data):
    name = input("Enter name to search: ").lower()
    for row in data[1:]:
        if row[0].lower() == name:
            print("🎯 Found:", row)
            return
    print("❌ Person not found.\n")

# 🛠 Update person
def update_person(data):
    name = input("Enter name to update: ").lower()
    for i in range(1, len(data)):
        if data[i][0].lower() == name:
            print("Current data:", data[i])
            data[i][1] = input("Enter new age: ")
            data[i][2] = input("Enter new city: ")
            save_data(data)
            print("✅ Person updated!\n")
            return
    print("❌ Person not found.\n")

# 🗑 Delete person
def delete_person(data):
    name = input("Enter name to delete: ").lower()
    for i in range(1, len(data)):
        if data[i][0].lower() == name:
            print("🗑 Deleting:", data[i])
            del data[i]
            save_data(data)
            print("✅ Person deleted!\n")
            return
    print("❌ Person not found.\n")

# 🚀 Main program
def main():
    data = load_data()

    while True:
        print("📋 Menu:")
        print("1. Add person")
        print("2. Show people")
        print("3. Search by name")
        print("4. Update person")
        print("5. Delete person")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_person(data)
        elif choice == '2':
            show_data(data)
        elif choice == '3':
            search_person(data)
        elif choice == '4':
            update_person(data)
        elif choice == '5':
            delete_person(data)
        elif choice == '6':
            print("👋 Exiting...")
            break
        else:
            print("⚠️ Invalid choice. Try again.\n")

main()
