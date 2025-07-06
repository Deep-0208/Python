import json

path = "D:\\Python\\03_Mini_Projects\\Student Result Management System\\student.json"

# Grade function
def get_grade(pr):
    if 90 < pr <= 100:
        return "A+"
    elif pr >= 80:
        return "A"
    elif pr >= 70:
        return "B"
    elif pr >= 60:
        return "C"
    elif pr >= 50:
        return "D"
    elif pr >= 40:
        return "E"
    else:
        return "F (Fail)"

# Load data
def load_data():
    try:
        with open(path, 'r') as file:
            data = json.load(file)
            if not isinstance(data, list):
                data = [data]
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    return data

# Add student
def add_student(data):
    try:
        student_name = input("Enter Student Name: ")
        student_roll_number = int(input("Enter Student Roll Number: "))
        math_marks = int(input("Enter your score in Maths out of 100: "))
        phy_marks = int(input("Enter your score in Physics out of 100: "))
        che_marks = int(input("Enter your score in Chemistry out of 100: "))
    except ValueError:
        print("❌ Please enter valid numeric values.")
        return

    pr = round((math_marks + phy_marks + che_marks) / 3, 2)
    student_grade = get_grade(pr)

    student_info = {
        "Name": student_name,
        "Roll Number": student_roll_number,
        "Marks": [math_marks, phy_marks, che_marks],
        "Percentage": pr,
        "Grade": student_grade
    }

    data.append(student_info)

    try:
        with open(path, 'w') as file:
            json.dump(data, file, indent=4)
            print("✅ Student info stored successfully.")
    except Exception as e:
        print("❌ Error writing to file:", e)

# Show all students
def show_students(data):
    if not data:
        print("No student records found.")
        return

    print("\n📋 Students Record:")
    print()
    print(f"{'#':<3} | {'Name':<15} | {'Roll No':<8} | {'Math':<5} | {'Phy':<5} | {'Chem':<5} | {'%':<8} | {'Grade'}")
    print("-" * 76)
    for i, st in enumerate(data, start=1):
        print(f"{i:<3} | {st['Name']:<15} | {st['Roll Number']:<8} | {st['Marks'][0]:<5} | {st['Marks'][1]:<5} | {st['Marks'][2]:<5} | {st['Percentage']:<8.2f} | {st['Grade']}")

def find_student():
    find_student = input("Enter Student Name OR Roll Number: ").strip().lower()
    found = False
    for student in students:
        name = student['Name'].strip().lower()
        roll = str(student['Roll Number']).strip()
        
        if find_student == name or find_student == roll:
            print("\n🎯 Student Found:")
            print(f"Name       : {student['Name']}")
            print(f"Roll Number: {student['Roll Number']}")
            print(f"Math Marks : {student['Marks'][0]}")
            print(f"Physics    : {student['Marks'][1]}")
            print(f"Chemistry  : {student['Marks'][2]}")
            print(f"Percentage : {student['Percentage']}%")
            print(f"Grade      : {student['Grade']}")
            found = True
            break
        
    if not found:
        print("❌ Student not found.")
    

def show_menu():
    print("\n📘 Student Result System")
    print("1. Add Student")
    print("2. Show All Students")
    print("3. Search Student")
    print("4. Exit")

if __name__ == "__main__":
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        students = load_data()

        if choice == '1':
            add_student(students)
        elif choice == '2':
            show_students(students)
        elif choice == '3':
            find_student()
        elif choice == '4':
            print("👋 Exiting program.")
            break
        else:
            print("❌ Invalid choice.")
