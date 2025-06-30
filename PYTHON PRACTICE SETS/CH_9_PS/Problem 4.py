word = "donkey"

with open("donkey.txt") as f:
    data = f.read()
    
newData = data.replace("donkey","######")

with open("donkey.txt" , "w") as f:
    content = f.write(newData)