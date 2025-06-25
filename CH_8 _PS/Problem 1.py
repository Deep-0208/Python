def max(n1, n2, n3):
    if (n1 > n2 and n1 > n3):
        print(f"Greatest of three is {n1}")
    elif (n2 > n3):
        print(f"Greatest of three is {n2}")
    else:
        print(f"Greatest of three is {n3}")


n1 = int(input("Enter Number 1 : "))
n2 = int(input("Enter Number 2 : "))
n3 = int(input("Enter Number 3 : "))

max(n1,n2,n3)