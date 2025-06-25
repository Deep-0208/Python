import os

def write_table(n):
    output = ""
    for i in range(1, 11):
        output += f"{n} X {i} = {n*i}\n"
        
    with open(f"tables/table{n}.txt", "w") as f:
        f.write(output)

# Ensure the directory exists
os.makedirs("tables", exist_ok=True)

for i in range(2, 21):
    write_table(i)
