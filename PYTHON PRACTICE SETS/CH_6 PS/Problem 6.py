marks = int(input("Enter your name :"))

if (marks >= 90):
    print("EX")
elif (marks >= 80 and marks <= 90):
    print("A")
elif (marks >= 70 and marks <= 80):
    print("B")
elif (marks >= 60 and marks <= 90):
    print("C")
elif (marks >= 50 and marks <= 90):
    print("D")
elif (marks < 50):
    print("F")
else:
    print("Your Enterd Incorrect Marks ! Please Enter Vaild Marks")
