import os

filepath = "log1_1.txt"

with open("log1_1.txt") as f:
    content = f.read()
    
with open("rename_by_python.txt" , "w") as f:
    f.write(content)
    
os.remove(filepath)