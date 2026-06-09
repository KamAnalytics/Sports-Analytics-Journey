# =============================================================
# Kam McIntire | Sports Analytics Journey
# VIDEO 2: Expressions, Data Types, & Variables
# Source: Automate the Boring Stuff - Al Sweigart
# Date: 06/04/2026
# =============================================================

# CONCEPTS COVERED:
#   Expressions
#   Data Types
#   Variables

# -------------------------------------------------------------
# CONCEPT: Expressions
# -------------------------------------------------------------

# Most basic program instruction
# Expressions = Values + Operators
# Always reduce to a single value

print(2 + 2)
print(5 * 3)

# -------------------------------------------------------------
# CONCEPT: Data Types
# -------------------------------------------------------------

# Integers
print(100)
# Floats
print(3.1415)
print(10.0)
# Strings
    ## Concatenation
print('USD ' + 'Coyotes')
    ## Replication
print('Go Yotes' + '!' * 3)

# -------------------------------------------------------------
# CONCEPT: Variables
# -------------------------------------------------------------

# Assignment statements
player_1 = 'A.J. Brown'
p1_team = 'New England Patriots'
p1_position = 'WR'
p1_jersey = '1'
print(player_1 + ' is now on the ' + p1_team + '. He plays ' + p1_position + ' wearing #' + p1_jersey)

# QUESTION: How can I store multiple NFL players' data such as jersey #, position, age, etc.?
# ANSWER: Use...
## (1/4) Unique variable names
### simple
p1 = 'Drake Maye'
p1_team = 'New England Patriots'
p1_position = 'QB'
p1_jersey = 10

p1_bio = '{} is the {} for the {} wearing #{}'.format(p1, p1_position, p1_team, p1_jersey)
print(p1_bio)

p2 = 'Rhamondre Stevenson'
p2_team = 'New England Patriots'
p2_position = 'RB'
p2_jersey = 38

p2_bio = '{} is the {} for the {} wearing #{}'.format(p2, p2_position, p2_team, p2_jersey)
print(p2_bio)

## (2/4) Dictionaries
### cleaner

# From here forward...
## I'm using " " instead of ' ' for strings

p3 = {
    "name": "TreVeyon Henderson",
    "team": "New England Patriots",
    "position": "RB",
    "jersey": 32
}

print(p3["name"] + " is the " + p3["position"] + " for the " + p3["team"] + " wearing #" + str(p3["jersey"]))

p4 = {
    "name": "Romeo Doubs",
    "team": "New England Patriots",
    "position": "WR",
    "jersey": 87
}

print(p4["name"] + " is the " + p4["position"] + " for the " + p4["team"] + " wearing #" + str(p4["jersey"]))

### Note: f-strings make the above print functions cleaner and easier to read

## (3/4) Class
### better than unique variable names and dictionaries
### NOTE: Don't rely on this pattern yet... Revisit this properly after learning functions and OOP (Object-Oriented Programming)

class NFLPlayer:
    def __init__(self, name, team, position, jersey):
        self.name = name
        self.team = team
        self.position = position
        self.jersey = jersey

    def bio(self):
        return "{} is the {} for the {} wearing #{}".format(
            self.name, self.position, self.team, self.jersey)

p5 = NFLPlayer("Kayshon Boutte", "New England Patriots", "WR", 9)
print(p5.bio())

## (4/4) pandas DataFrame (df)
### BEST PRACTICE within a single file
### NOTE: This requires pandas library (pip install pandas), revisit later
### BEST PRACTICE for real sports data projects

import pandas as pd

players = [
    {"name": "Drake Maye", "team": "Patriots", "position": "QB", "jersey": 10},
    {"name": "Kayshon Boutte", "team": "Patriots", "position": "WR", "jersey": 9},
    {"name": "TreVeyon Henderson", "team": "Patriots", "position": "RB", "jersey": 32},
]

df = pd.DataFrame(players)
print(df)

print(df[df["position"] == "WR"])  # All WRs instantly