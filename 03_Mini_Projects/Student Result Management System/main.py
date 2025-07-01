'''
| # | Feature                      | Description                      |
| - | --------------------------   | -------------------------------- |
| 1 | ➕ Add student              | Name, Roll No, Marks in subjects |
| 2 | 📋 View all students       | Print all records nicely         |
| 3 | 🔍 Search by roll no/name  | Show data of one student         |
| 4 | 🛠️ Update student data    | Change marks or name             |
| 5 | 🗑 Delete student          | Remove a record                  |
| 6 | 📊 Grade system            | Auto grade: A, B, C, etc.        |
| 7 | 💾 Save to `students.json` | Use JSON file for records        |

'''
import json

path = "D:\\Python\\03_Mini_Projects\\Student Result Management System\\student.json"

student_name = input("Enter Student Name :") 
student_roll_number = int(input("Enter Student Roll Number :") )
math_mark = int(input("Enter your score in Maths out of 100: "))
phy_mark = int(input("Enter your score in Physics out of 100: "))
che_mark = int(input("Enter your score in Chemistry out of 100: "))



student_info = {
    "Name" : student_name ,
    "Roll Number" : student_roll_number ,
    "Obtained Marks In Maths (Out of 100)" : math_mark ,
    "Obtained Marks In Physics (Out of 100)" : phy_mark ,
    "Obtained Marks In Chemistry (Out of 100)" : che_mark ,   
}
try:
    with open(path , 'w') as file :
        json.dumps(student_info , indent=4)

except FileNotFoundError as f:
    print("File Not Found Please Create \"student.json.\" file ")
