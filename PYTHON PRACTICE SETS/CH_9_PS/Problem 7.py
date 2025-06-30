with open("log.txt") as f:
    lines = f.readlines()

    lineNo = 1
    for line in lines:
        if ("Python" in line):
            print(f"Yes Python is present in line num {lineNo}")
            break
        lineNo += 1

    else:
        print("Python is not available")
