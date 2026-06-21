# =============================================================
# Kam McIntire | Sports Analytics Journey
# VIDEO 11: try and except Statements & Input Validation
# Source: Automate the Boring Stuff - Al Sweigart
# Date: 06/20/2026
# =============================================================

# CONCEPTS COVERED:
#   try and except Statements
#   Input Validation

# -------------------------------------------------------------
# CONCEPT: try and except Statements
# -------------------------------------------------------------

# an input resulting in an 'Error' or 'Exception' output will crash the entire program
# UNLESS you use try and except Statements
#   allows the program to detect errors, handle them, and continue to run the program

# example of specifying an error:
#   (ZeroDivisionError)

def div15by(divby):
    try:
        return 15 / divby
    except ZeroDivisionError:
        print("Error: Python doesn't like dividing by 0...")

print(div15by(1))
print(div15by(2))
print(div15by(0))   # without the try and except Statement above ... output -> "ZeroDivisionError"
print("Program would crash and terminate here as py doesn't know how to handle x / 0")

# REMEMBER: if your function doesn't have a return Statement, the default return is None (value)
print()

print(div15by(3))
print(div15by(4))
print(div15by(5))
print("\n")

# -------------------------------------------------------------
# CONCEPT: Input Validation
# -------------------------------------------------------------

# 1. 'Catch All' errors with 'except:'   instead of 'except ___:'
# or
# 2. Include ways to validate inputs within your code to prevent crashes (and/or run additional lines of code)

guess = input("Anthony Edwards jersey number: ")
while guess:
    try:
        if int(guess) == 5:
            print("Correct. Ant has sported #5 since the 2024 season.\n")
        elif int(guess) < 0:
            print("NBA players don't have negative jersey numbers.\nThis if Statement is 'Input Validation' to catch an input of a negative number. Try again.\n")
        elif int(guess) == 1:
            print("Ant wore #1 his first 3 years in the league (2021-2023).\nThis if Statement is 'Input Validation' to catch an input of '1'. Try again.\n")
        elif int(guess) == 6:
            print("Fun Fact: In August 2022 after his passing, #6 has been permanently retired across all teams to honor Bill Russell.\nThis if Statement is 'Input Validation' to catch an input of '6'. Try again.\n")
        elif int(guess) >= 100:
            print("The NBA has always enforced strict rules to prevent any jersey number greater than or equal to 100.\nThis if Statement is 'Input Validation' to catch an input >=100. Try again.\n")
        elif int(guess) in range(0, 100):
            print("Incorrect.\nThis if Statement is 'Input Validation' to catch an input of 0-99 (but not including 1, 6, or the correct answer). Try again.\n")
    except:
        print("Please enter a number.\nThis if Statement is 'Input Validation' to catch an input that is not a number. Try again.\n")
    guess = input("Anthony Edwards jersey number: ")