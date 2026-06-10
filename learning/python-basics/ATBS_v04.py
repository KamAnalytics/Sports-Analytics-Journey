# =============================================================
# Kam McIntire | Sports Analytics Journey
# VIDEO 4: Flow Control Statements
# Source: Automate the Boring Stuff - Al Sweigart
# Date: 06/09/2026
# =============================================================

# CONCEPTS COVERED:
#   Flow Charts
#   Flow Control Statements

# -------------------------------------------------------------
# CONCEPT: Flow Charts
# -------------------------------------------------------------

# Diagram that shows the execution process of a program

# -------------------------------------------------------------
# CONCEPT: Flow Control Statements
# -------------------------------------------------------------

# Boolean Values
#   True or False
#   Can be used in variables
New_England_Patriots = True
Kansas_City_Chiefs = False

# Comparison Operators
#   ==  Equal to
#   !=  Not equal to
#   <   Less than
#   >   Greater than
#   <=  Less than or equal to
#   >=  Greater than or equal to
# Expressions with Comparison Operators evaluate to a Boolean Value
print(10 == 10)
print("10 == 10 is " + str(10 == 10))
print()

print(10 == "10")
print("10 == \"10\" is " + str(10 == "10"))
print()

print(10 == 10.0)
print("10 == 10.0 is " + str(10 == 10.0))
print()

if 10 < 100: print("10 < 100")
if 10 > 100: print("10 > 100")
print()

myName = "Kam"
print(myName == "Kam")
print("myName == Kam is " + str(myName == "Kam"))
print()

print(myName == 100)
print("myName == 100 is " + str(myName == 100))
print()

year = 2007
player = {
    "Tom Brady": {
        "team": "New England Patriots",
        "position": "QB",
        "number": 12,
        "age": 30,
        "college": "Michigan",
        "height": "6'4\"",
        "weight": "225"
    }
}
player_input = input("In 2007, what team was Tom Brady on?\n")
print()

if player_input.lower() == player["Tom Brady"]["team"].lower():
    print("Correct!")
else:
    print("Nope, guess again...")

# Boolean Operators
#   and
#   or
#   not

# The and Operator's Truth Table
print(True and True) # everything must be True to output True
print(True and False)
print(False and True)
print(False and False)
print()
myName = "Kam"
myAge = 25
myEyes = "Hazel"
print("Kam is 25 with hazel-colored eyes" if myName == "Kam" and myAge == 25 and myEyes == "Hazel" else "Kam is not 25 with hazel-colored eyes")
print()

# The or Operator's Truth Table
print(True or True)
print(True or False)
print(False or True)
print(False or False) # there must be at least one True, else False
print()

# The not Operator's Truth Table
print(not True)
print(not False)