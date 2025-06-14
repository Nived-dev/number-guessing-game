"""
Number Guessing Game.

This is a simple number guessing game where the user has 3 attempts
to guess a number betwen 1 and 10. After each guess, feedback is
given whether the guess was too high or too low.
"""

import random
number_to_guess = random.randint(1,10) #generates a random number between 1 to 10.
print("Welcome to the number guessing game!")
print("I'm thinking a number between 1 to 10.\nYou will get 3 attempts.")

guess = None
attempts = 0
max_attempts = 3

while guess != number_to_guess and attempts < max_attempts: #below code will work if this two conditions follows.
    guess = int(input("Take a guess on the number"))
    attempts += 1 #attempts = attempts + 1
    if guess > number_to_guess:
        print("Too high! Try again.")
    elif guess < number_to_guess:
        print("Too low! Try again.")
    elif guess == number_to_guess:
        print("Congratulations! You guessed right.\n YOU WIN")
        break #stops the loop if guessed right.
else:
    print(f"Sorry, you're out of chances. The number was {number_to_guess}")