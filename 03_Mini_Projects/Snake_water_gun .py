import random

# Mapping for choices
symbol_to_number = {"s": 1, "w": -1, "g": 0}
number_to_symbol = {1: "Snake", -1: "Water", 0: "Gun"}

# Computer's choice
computer = random.choice([0, 1, -1])

# User input
user_input = input(
    "Enter your choice (s for Snake, w for Water, g for Gun): ").lower()

# Input validation
if user_input not in symbol_to_number:
    print("Invalid input! Please enter 's', 'w', or 'g'.")
    exit()

you = symbol_to_number[user_input]

print(f"Computer chose: {number_to_symbol[computer]}")
print(f"You chose: {number_to_symbol[you]}")

# Game logic
if computer == you:
    print("Match Draw!")
elif (computer == 1 and you == -1) or (computer == -1 and you == 0) or (computer == 0 and you == 1):
    print("You win!")
else:
    print("You lose!")
