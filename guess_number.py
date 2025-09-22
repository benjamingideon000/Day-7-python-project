# guess_number.py

import random

number_to_guess = random.randint(1, 50)
attempts = 0

print("Hey there! Let's play a game. I'm thinking of a number between 1 and 50.")

while True:
    guess = int(input("What's your guess? "))
    attempts += 1

    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print(f"Yay! You got it in {attempts} attempts. Well done!")
        break
