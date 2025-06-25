a = int(input("Enter number :"))
b = int(input("Enter number :"))

try :
    print(f"a/b is {a/b}")
except ZeroDivisionError:
    if (b == 0):
        print(f"a/b is ∞")
    