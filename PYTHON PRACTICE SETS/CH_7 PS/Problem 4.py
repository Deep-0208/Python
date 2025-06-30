import math
n = int(input("Enter Number: "))

if n <= 1:
    print("Number is not prime")
else:
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            print("Number is not prime")
            break
    else:
        print("Number is prime")
