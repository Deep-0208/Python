with open("poems1.txt") as f:
    data = (f.read())
    if("twinkle" in data):
        print("Twinkle is available")
    else:
        print("Twinkle is not available")
        