with open("log.txt") as f:
    content = f.read()
    
with open("log_1.txt", "w") as f :
    f.write(content)
    