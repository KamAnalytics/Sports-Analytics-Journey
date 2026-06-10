# =============================================================
# Kam McIntire | Sports Analytics Journey
# VIDEO 5: Flow Control Statements, "Truthy" & "Falsey" Values, & bool Functions
# Source: Automate the Boring Stuff - Al Sweigart
# Date: 06/09/2026 - Last updated 06/10/2026
# =============================================================

# CONCEPTS COVERED:
#   Flow Control Statements (continued)
#   "Truthy" & "Falsey" Values
#   bool Functions
#   Misc Terms

# -------------------------------------------------------------
# CONCEPT: Flow Control Statements (continued)
# -------------------------------------------------------------

# if & else Statements
#   if Statements conditionally execute code
#   else Statements execute when all previous conditions are False

password = "Kam"
input("This program is for Kam and Kam only. Who is this?\n")
print()
if password == "Kam":
    print("Welcome, Kam!")
else:
    print("Access Denied")

# More complicated use-case for if & else Statements
#   many if and else Statements could've been used here but it would've been bad code, a While Loop is best here

nfl_coaches_wins_alltime = {
    "Arizona Cardinals": {"coach": "Ken Whisenhunt", "wins": 49},
    "Atlanta Falcons": {"coach": "Dan Reeves", "wins": 54},
    "Baltimore Ravens": {"coach": "John Harbaugh", "wins": 180},
    "Buffalo Bills": {"coach": "Marv Levy", "wins": 123},
    "Carolina Panthers": {"coach": "John Fox", "wins": 78},
    "Chicago Bears": {"coach": "George Halas", "wins": 324},
    "Cincinnati Bengals": {"coach": "Marv Lewis", "wins": 131},
    "Cleveland Browns": {"coach": "Paul Brown", "wins": 222},
    "Dallas Cowboys": {"coach": "Tom Landry", "wins": 270},
    "Denver Broncos": {"coach": "Mike Shanahan", "wins": 146},
    "Detroit Lions": {"coach": "Wayne Fontes", "wins": 67},
    "Green Bay Packers": {"coach": "Curly Lambeau", "wins": 229},
    "Houston Texans": {"coach": "Gary Kubiak", "wins": 63},
    "Indianapolis Colts": {"coach": "Tony Dungy", "wins": 92},
    "Jacksonville Jaguars": {"coach": "Jack Del Rio", "wins": 69},
    "Kansas City Chiefs": {"coach": "Andy Reid", "wins": 280},
    "Las Vegas Raiders": {"coach": "John Madden", "wins": 112},
    "Los Angeles Chargers": {"coach": "Don Coryell", "wins": 72},
    "Los Angeles Rams": {"coach": "John Robinson", "wins": 79},
    "Miami Dolphins": {"coach": "Don Shula", "wins": 347},
    "Minnesota Vikings": {"coach": "Bud Grant", "wins": 168},
    "New England Patriots": {"coach": "Bill Belichick", "wins": 333},
    "New Orleans Saints": {"coach": "Sean Payton", "wins": 161},
    "New York Giants": {"coach": "Steve Owen", "wins": 155},
    "New York Jets": {"coach": "Weeb Ewbank", "wins": 73},
    "Philadelphia Eagles": {"coach": "Andy Reid", "wins": 140},
    "Pittsburgh Steelers": {"coach": "Chuck Noll", "wins": 209},
    "San Francisco 49ers": {"coach": "George Seifert", "wins": 113},
    "Seattle Seahawks": {"coach": "Pete Carroll", "wins": 147},
    "Tampa Bay Buccaneers": {"coach": "Tony Dungy", "wins": 56},
    "Tennessee Titans": {"coach": "Jeff Fisher", "wins": 146},
    "Washington Commanders": {"coach": "Joe Gibbs", "wins": 171},
}
q1_guess = input("Who do you believe holds the record for \"Most All-Time Wins\" by an NFL Head Coach?\n").title()

while q1_guess.lower() != "don shula":
    for team, data in nfl_coaches_wins_alltime.items():
        if data["coach"].lower() == q1_guess.lower():
            print(f"No, {q1_guess} is not the record holder. {q1_guess} has {data['wins']} wins with the {team}. Guess again.")
            break
    q1_guess = input("Guess again: ").title()
print()
print("Correct! Don Shula holds the record, tallying 347 wins with the Miami Dolphins.")
print()

# elif Statements
#   the first elif Statement with a True condition is executed, following elif Statements are ignored
#   ORDER MATTERS!
#   can have as many elif Statements as needed
#       only if needed, include an else Statement at the end in case all conditions are False
print("General NBA Positional Height Ranges")
print("Enter a height (in inches) to see what position best suits that height.")
print()
height = float(input("Height: "))
if height < 75:
    print("A height of " + str(height) + " inches would likely fit the position of a PG")
elif height < 78:
    print("A height of " + str(height) + " inches would likely fit the position of a SG")
elif height < 81:
    print("A height of " + str(height) + " inches would likely fit the position of a SF")
elif height < 83:
    print("A height of " + str(height) + " inches would likely fit the position of a PF")
elif height > 83:
    print("A height of " + str(height) + " inches would likely fit the position of a C")
print()

# -------------------------------------------------------------
# CONCEPT: "Truthy" & "Falsey" Values
# -------------------------------------------------------------

# "Truthy" & "Falsey" String Values
understanding = input("Do you understand how this program is working? If so, press Enter. Otherwise, explain why not. ")
# Input returns a String Value, not a Boolean (True/False) Value

if understanding:
# Truthy - any input that isn't blank
#   be more explicit with - if understanding != "":
    print("You should review your code and run this program again...")
# Falsey - blank Strings
else:
    print("Great!")
print()

# "Truthy" & "Falsey" Integer Values
#   0 is Falsey, else Truthy

# "Truthy" & "Falsey" Floating Point Values
#   0.0 is Falsey, else Truthy

# -------------------------------------------------------------
# CONCEPT: bool Functions
# -------------------------------------------------------------

# returns the input's equivalent Boolean Value

#   bool Functions w/ Strings
print("bool(\"Kam\") = " + str(bool("Kam")))
print("bool(\"\") = " + str(bool("")))
print()
#   bool Functions w/ Integers
print("bool(10) = " + str(bool(10)))
print("bool(10.0) = " + str(bool(10.0)))
print("bool(0) = " + str(bool(0)))
print("bool(0.0) = " + str(bool(0.0)))

# -------------------------------------------------------------
# CONCEPT: Misc Terms
# -------------------------------------------------------------

# BLOCKS
#   aka Clauses, lines of code indented at the same level to tell Python what's in if Statements (ex.) and what isn't
#       Begin when indentation increases, statements that end with :
#       End when indentation returns to previous level
##     *Blank lines are ignored*
# CONDITION
#   aka Expression, the expression in a Flow Control Statement