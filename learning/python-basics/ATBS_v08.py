# =============================================================
# Kam McIntire | Sports Analytics Journey
# VIDEO 8: Built-In Library & pip to Install Third-Party Modules
# Source: Automate the Boring Stuff - Al Sweigart
# Date: 06/12/2026
# =============================================================

# CONCEPTS COVERED:
#   Built-in Functions
#   Standard Library
#   import Statements
#   pip to Install Third-Party Modules

# -------------------------------------------------------------
# CONCEPT: Built-in Functions
# -------------------------------------------------------------

# py's basic set of functions
print("print(), input(), len()")

# -------------------------------------------------------------
# CONCEPT: Standard Library
# -------------------------------------------------------------

# py's set of modules
#   math
#   random
#   sys
#   os
#   pip

# -------------------------------------------------------------
# CONCEPT: import Statements
# -------------------------------------------------------------

# Random
import random

# To use imported Statemens within imported Modules, tell py: thisModule.thisStatement
# 'randint' Function within Random Module -> random.randint
print(random.randint(1, 100))
# code w/ random.randint()
while True:
    x = random.randint(1, 3)
    if x == 2:
        continue
    print(x)
    break

# ! NOT BEST PRACTICE !
from random import *
# from the random module, import *(all) functions
print(randint(10, 15))

import sys
# code w/ sys.exit()
hit_enter = input("Roll a dice\nIf you roll a 1, this file's program execution stops here\nType \"roll\" to roll the dice. Good luck!\n\n")
if hit_enter != "roll".lower():
    print("Please type \"roll\" to roll the dice")
else: 
    while True:
        x = randint(1, 6)
        if x == 1:
            print("You rolled a 1. Goodbye!")
            sys.exit()
        break
print("Whew, you rolled a " + str(x) + ".")

# -------------------------------------------------------------
# CONCEPT: pip to Install Third-Party Modules
# -------------------------------------------------------------

# pip is a Standard Library as of 3.4
# https://automatetheboringstuff.com/3e/appendixa.html

# pyperclip must be installed via pip through the terminal
import pyperclip

response = input("Check this out, \"Kam\" will be copied to your clipboard if you type: \"pip install pyperclip\"\n\n")
while True:
    if response != "pip install pyperclip":
        print("Please type \"pip install pyperclip\" to proceed.")
    else:
        break

pyperclip.copy("Kam")
Kam = input("Hit Ctrl + V and Enter\n\n")

if Kam != "Kam":
    print("Looks like that didn't work...")
else:
    print("It worked!")