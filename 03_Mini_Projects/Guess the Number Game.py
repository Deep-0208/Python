# Random number, user tries to guess it in limited attempts

import random

# Computer Choice
computer_choice = random.randint(1, 21)

attempt = 1
allowed_attempt = 10

while (attempt < allowed_attempt) :
        user_choice = int(input("Guess Number From 1-20 :"))
        
        if (user_choice > computer_choice):
            print("Guess Lower Number")
            attempt += 1
            print(f"You have only {10 - attempt} to guess correct number ")

        elif (user_choice < computer_choice):
            print("Guess Higher Number")
            attempt += 1
            print(f"You have only {10 - attempt} to guess correct number ")
        
        else:
            print(f"You Guessed Correct Number in {attempt}")
            break