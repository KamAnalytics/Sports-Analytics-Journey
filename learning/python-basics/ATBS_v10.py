# =============================================================
# Kam McIntire | Sports Analytics Journey
# VIDEO 10: Global & Local Scopes
# Source: Automate the Boring Stuff - Al Sweigart
# Date: 06/15/2026 - Last updated 06/20/2026
# =============================================================

# CONCEPTS COVERED:
#   Global and Local Scopes

# -------------------------------------------------------------
# CONCEPT: Global and Local Scopes
# -------------------------------------------------------------

# Scopes are 'containers' of Variables (Global Variables, Local Variables)


# Global and Local Variables can have the same name and different values simultaneously
# examples of the different scopes:

# Global: `name = "Kam"`
# Local: `name = `"Kameron"`

# Global Scope:
#   accessible everywhere
name = "Kam"                            #*GLOBAL*#
print("Global scope is " + name)

# Local Scope:
#   only exists inside a function
import sys

def password():
    name = "Kameron"                        #*LOCAL*#
    this_file = "ATBS_v10.py"
    file_number = 10
    correct_password = name + "_" + this_file + "_" + str(file_number)

    attempts = 2
    while attempts > 0:
        guess = input("Password: ")
        if guess == correct_password:
            print("Access Granted\n")
            return
        else:
            attempts = attempts - 1
            reasons = ""
            if "Kameron" not in guess:
                reasons = reasons + "name, "
            if "ATBS_v10.py" not in guess:
                reasons = reasons + "file name, "
            if str(file_number) not in guess:
                reasons = reasons + "file number, "
            
            if attempts > 0:
                print("Access Denied. Reason: " + reasons + "try again.\n")
            else:
                print("Access Denied. Reason: " + reasons + "goodbye!\n")
                sys.exit()

password()
# Kameron_ATBS_v10.py_10

print("Global scope is still " + name)
print("\n\n")

# QUESTION: if a variable is within a function, is it 1. a Global Variable or 2. a Local Variable being read from the Global Scope?
# ANSWER: Depends on whethere there is an Assignment Statement defining the variable anywhere in the function
#   Assignment Statement = Local Variable
#   NO Assignment Statement = Global Variable
#       example:

team = "Patriots"

# LOCAL

def pats():                         # pats() is the Function
    team_location = "New England"   # team_location is the Assignment Statement
    print(team_location)                # making team_location a LOCAL VARIABLE residing in the pats() Function

team_location = "Foxborough, MA"    # (this gets ignored because when calling the pats() Function, team_location within it is defined as "New England")

pats()
print()


# GLOBAL

def patriots():                         # pats() is the Function
                                    # there is NO Assignment Statement
    print(team_location)                # making team_location a GLOBAL VARIABLE residing in the pats() Function
                                        # as it must be defined somewhere globally
team_location = "Foxborough, MA"        # (as it is here)

patriots()
print()


# QUESTION: Can you assign a new value to a Global Variable within the Local Scope?
# ANSWER: YES - Global Statements:

# `global ___`

team_location = "Foxborough, MA"        # (this gets ignored because "New England" is the new Global Variable for team_location...

def pats():
    global team_location
    team_location = "New England"       # (as it is here)
    print(team_location)

print("Calling pats() AND print(team_location) both output ")
pats()
print("and " + team_location)

print("because \"New England\" is most recently defined as the value for that Global Variable")


# QUESTION: Why use both Global/Local Scopes? Wouldn't it be easier to make everything a Global Variable?
# ANSWER: Not necessarily...

# Benefits of Local Scopes:
#   Lets you separate code of a Function from the rest of the program
#   Lets you treat Functions as blocks in a way
#   Makes it easier to find errors/bugs within the respective Scope