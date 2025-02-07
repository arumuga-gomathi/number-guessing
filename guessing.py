# Simple Guessing Game

import random

# Pick a random number between 1 and 10
secret_number = random.randint(1, 10)

# Give player 3 chances to guess
print("🎲 Guess the Number Game 🎲")
print("I'm thinking of a number between 1 and 10!")

# Player gets 3 attempts
for attempt in range(3):
    # Ask for guess
    guess = int(input("Your guess (1-10): "))
    
    # Check if guess is correct
    if guess == secret_number:
        print("🎉 Bro! YOU WON! Great guess!")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

# If no guess was correct
if guess != secret_number:
    print(f"Game over! The number was {secret_number}")