# write a program to find a greatest of four numbers enterd by the user

n1 = int(input("Enter Num 1 :"))
n2 = int(input("Enter Num 2 :"))
n3 = int(input("Enter Num 3 :"))
n4 = int(input("Enter Num 4 :"))

if (n1 > n2 and n1 > n3 and n1 > n4):
        print(f"{n1} is greates")

elif (n2 > n3 and n2 > n4):
    print(f"{n2} is greates")

elif (n3 > n4):
    print(f"{n3} is greates")

else:
    print(f"{n4} is greates")
