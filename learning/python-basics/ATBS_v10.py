# =============================================================
# Kam McIntire | Sports Analytics Journey
# VIDEO 10: .
# Source: Automate the Boring Stuff - Al Sweigart
# Date: 06/15/2026
# =============================================================

# CONCEPTS COVERED:
#   Global and Local Scopes

# -------------------------------------------------------------
# CONCEPT: Global and Local Scopes
# -------------------------------------------------------------

# Scopes are 'containers' of Variables (Global Variables & Local Variables)

# Global Scope:
name = Kam

# Local Scope:
import sys

def password():
    name = "Kam"
    this_file = "ATBS_v10.py"
    file_number = 10

    correct_password = name + "_" + this_file + "_" + str(file_number)

    attempts = 2

    while attempts > 0:
        guess = input("Password: ")

        if guess == correct_password:
            print("Access Granted\n")
            return                      # returns None Value - exits the whole function




        if name != name:
            input("Access Denied. Reason: You are not Kam. Try again\nHint: (your name)_(file name)_(file number)\nPassword: ")
            if name != name:
                input("Access Denied. Reason: You are not Kam. Goodbye!")
                sys.exit()
        if this_file != this_file:
            input("Access Denied. Reason: You've entered the wrong file name. Try again\nHint: (your name)_(file name)_(file number)\nPassword: ")
            if this_file != this_file:
                input("Access Denied. Reason: You've entered the wrong file name. Goodbye!")
                sys.exit()
        if file_number != file_number:
            input("Access Denied. Reason: You've entered the wrong file number. Try again\nHint: (your name)_(file name)_(file number)\nPassword: ")
            if file_number != file_number:
                input("Access Denied. Reason: You've entered the wrong file number. Goodbye!")
                sys.exit()
        if python = 
        else: print("Access Granted\n")



print("Enter this file's password below\nWARNING: YOU ONLY GET 2 GUESSES...\nPassword: ")

password()

print("The Password is Kam_ATBS_v10.py_10")

# QUESTION: 
# ANSWER: 