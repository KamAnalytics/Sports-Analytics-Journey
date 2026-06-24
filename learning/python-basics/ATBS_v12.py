# =============================================================
# Kam McIntire | Sports Analytics Journey
# VIDEO 12: Writing Programs
# Source: Automate the Boring Stuff - Al Sweigart
# Date: 06/23/2026
# =============================================================

# CONCEPTS COVERED:
#   Writing Programs

# -------------------------------------------------------------
# CONCEPT: Writing Programs
# -------------------------------------------------------------

import random

secretNumber = random.randint(1, 20)
print("I'm thinking of a number 1-20. You have 5 guesses. What's your guess?")

# Debug line
print("The secret number is " + str(secretNumber))

for guessesTaken in range(1, 6):
    guess = int(input())
    if guess < secretNumber:
        print(str(guess) + " is too low. You have " + str(5 - guessesTaken) + " guesses remaining.")
    elif guess > secretNumber:
        print(str(guess) + " is too high. You have " + str(5 - guessesTaken) + " guesses remaining.")
    else:
        break

if guess == secretNumber and guessesTaken == 1:
    print("Correct! You guessed the secret number in just a single guess!")
elif guess == secretNumber:
    print("Correct! You guessed the secret number in " + str(guessesTaken) + " guesses!")
else:
    print("You did not guess the secret number in 5 guesses. The secret number was " + str(secretNumber))

# NOTES:
#   ensure proper order and placements for lines of code
#   ensure proper format for Loops and if/elif/else Statements
#   always remember when you need to convert to/from Strings & Integers