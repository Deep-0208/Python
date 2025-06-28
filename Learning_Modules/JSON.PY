'''
Build a simple app that:

Takes user input: name, age, city

Saves it to a JSON file

Then reads and prints the saved info
'''
'''
| Function  | Converts from → to    | Works with | Used for                  |
| --------- | --------------------- | ---------- | ------------------------- |
| `dumps()` | Python → JSON string  | String     | Store/send JSON as text   |
| `dump()`  | Python → JSON in file | File       | Save data to `.json` file |
| `loads()` | JSON string → Python  | String     | Read JSON from a string   |
| `load()`  | JSON file → Python    | File       | Read JSON from a file     |
'''    

import json

name = input("Enter your name : ")
age = int(input("Enter your age :"))
city = input("Enter Your city :")

user_data = {
    "name" : name ,
    "age" : age ,
    "city" : city
}

with open("data.json" , "w") as f:
    data = json.dump(user_data , f , indent=4)

with open ("data.json" , "r") as f:
    loaded_data = json.load(f)
    
print("\nSaved Info:")
print(f"Name: {loaded_data['name']}")
print(f"Age: {loaded_data['age']}")
print(f"City: {loaded_data['city']}")