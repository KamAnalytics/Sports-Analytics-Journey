# =============================================================
# Kam McIntire | Sports Analytics Journey
# VIDEO 3: Using Functions to Write Programs
# Source: Automate the Boring Stuff - Al Sweigart
# Date: 06/05/2026 - Last updated 06/08/2026
# =============================================================

# CONCEPTS COVERED:
#   str(), int(), and float() Functions
#   Writing Programs

# -------------------------------------------------------------
# CONCEPT: str(), int(), and float() Functions
# -------------------------------------------------------------

# NOTE: In real sports data work, CSV files import all values as strings by default
## str(), int(), float() are used constantly to convert them before analysis

# These functions convert data types to work with player info
## NOTE: the 3 values are integers in the program below, age and weight are defined as strings for this example only

## int to str for concatenation
player_number = 14
print("Sam Darnold's player number: #" + str(player_number))
## str to int for math
player_age = "29"
print("Sam Darnold's next birthday age: " + str(int(player_age) + 1))
## str to float for conversion
player_weight = "225"
print("Sam Darnold's weight in kg: " + str(float(player_weight) * 0.453592))
print()

# QUESTION: Why might it be useful to define a number as a str rather than an int?
# ANSWER: Values that are RARELY used with math don't need to be integers at all, this would save time on constantly converting back/forth
            # Example: Jersey numbers - you'd never do math on a jersey number

# QUESTION: How would you clean data that was imported as incorrect value types, or you just want to change them (imported as a str but you want to convert to an int)
# ANSWER: pandas is smart enough to guess, but sometimes gets it wrong. Here's how to fix it:
#            df["age"] = df["age"].astype(int)
#            df["weight"] = df["weight"].astype(float)
            # This is pandas converting entire columns of data at once

# -------------------------------------------------------------
# CONCEPT: Writing Programs
# -------------------------------------------------------------

# This is an example of a program where I define player information data as a key that acts as a 'mini database' of sorts
## NOTE: Very beginner-level, still learning...
## Demonstrates:
### input() capturing user data
### Dictionaries and nested dictionary access
#### Membership operator `in`
#### .lower() for input normalization
#### if/elif/else flow control
#### f-strings for clean output

print("Welcome to Kam's NFL Player Info Lookup")
print("Week 1 2026: New England Patriots vs Seattle Seahawks")
print()

players = {
    "Sam Darnold": {
        "team": "Seattle Seahawks",
        "position": "QB",
        "number": 14,
        "age": 29,
        "college": "USC",
        "height": "6'3\"",
        "weight": "225 lbs"
    },
    "Jaxon Smith-Njigba": {
        "team": "Seattle Seahawks",
        "position": "WR",
        "number": 11,
        "age": 24,
        "college": "Ohio State",
        "height": "6'0\"",
        "weight": "197 lbs"
    }
}

player_input = input("Enter a player name: ")
print()

if player_input in players:
    print(f"Here's what I have on {player_input}. What would you like to know?")
    print("Options: team, position, number, age, college, height, weight")
    print()
    stat_input = input("Enter your choice: ").lower()
    print()

    if stat_input in players[player_input]:
        print(f"{player_input}'s {stat_input}: {players[player_input][stat_input]}")
    else:
        print(f"'{stat_input}' isn't a valid option. Try: team, position, number, age, college, height, or weight")
else:
    print(f"'{player_input}' wasn't found. Try: Sam Darnold or Jaxon Smith-Njigba")