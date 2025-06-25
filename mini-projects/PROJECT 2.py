'''
We are going to write a program that genrates a random number and asks the use to guess it.

if the player's guess is higher than the  actual number , the program display prints "Lower number please". Similarly , if the user's guess is too low , the program prits "Higher number please" When the user gusses the correct number , the program display the number of gusses the player to arrive at the number
'''

import random

n = random.randint(1, 101)
a = -1
count = 1
while(a != n):
    a = int(input("Guess the number :"))
    if (a > n):
        print("Lower Number Please")
        count += 1

    elif(a < n):
        print("Higher Number Please")
        count += 1

    else:
        print(f"You Guess Correct number in {count}th try")

