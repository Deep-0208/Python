with open("log.txt") as f:
    data = f.read()
    if ("Python" in data):
        print("Yes python is present")
    else:
        print("No Python is not available")
