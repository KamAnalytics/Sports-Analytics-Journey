# =============================================================
# Kam McIntire | Sports Analytics Journey
# VIDEO 13: Lists, Indexes, & Slices
# Source: Automate the Boring Stuff - Al Sweigart
# Date: 06/26/2026
# =============================================================

# CONCEPTS COVERED:
#   Lists
#       1. Lists
#       2. Lists of Lists
#       3. Changing a List's Items
#           - Using an Index
#           - Using a Slice
#       4. String & List Similarities
#           - len Function
#           - List Concatenation
#           - List Replication
#           - list() Function
#           - in and not in Operators
#   Indexes
#       1. Indexing Lists
#       2. Indexing Lists of Lists
#       3. Negative Indexes
#   Slices
#       1. Slice Shortcuts

# -------------------------------------------------------------
# -------------------------------------------------------------
# -------------------------------------------------------------
#                          FIRST...
#          I USE LIST SYNTAX EXCLUSIVELY IN THIS FILE
#       Lists begin with []   Dictionaries begin with {}
# -------------------------------------------------------------
# -------------------------------------------------------------
# -------------------------------------------------------------

this_is_a_list = ["Item A", "Item B", "Item C"]
# Index =   0         1        2

this_is_a_dictionary = {
    "key_1": "Value A",
    "key_2": "Value B",
    "key_3": "Value C"
}

# -------------------------------------------------------------
# CONCEPT: Lists
# -------------------------------------------------------------

# BEGINNING WITH 0

# 1. LISTS
#   Items in an ordered sequence
exampleList = [1, 2, 3, 4, 5]
print(exampleList[0])
print(exampleList[4])
print()

team = "New England Patriots"
# New England Patriots 2026-27 Opponents (by Week #)
pats_opponents = [
    "Seattle Seahawks",
    "Pittsburgh Steelers",
    "Jacksonville Jaguars",
    "Buffalo Bills",
    "Las Vegas Raiders",
    "New York Jets",
    "Chicago Bears",
    "Miami Dolphins",
    "Green Bay Packers",
    "Detroit Lions",
    "BYE WEEK",
    "Los Angeles Chargers",
    "Buffalo Bills",
    "Minnesota Vikings",
    "Kansas City Chiefs",
    "New York Jets",
    "Denver Broncos",
    "Miami Dolphins",
]



# 2. LISTS of LISTS
#   Accessed using multiple indexes
exampleList = [1, 10, 100], [2, 20, 200], [3, 30, 300], [4, 40, 400], [5, 50, 500]
print(exampleList[0])
print(exampleList[2][1])
print(exampleList[4][2])
print()

# New England Patriots 2026-27 Regular Season Schedule
#   [week, date, time, location, opponent]
#       [... (items within these items of the list) ...]
# THIS IS A LIST OF DICTIONARIES
pats_schedule = [
    {
        "week": 1,
        "date": "Wednesday, Sept. 9, 2026",
        "time": "7:20 PM CST",
        "location": "Lumen Field (Seattle, WA)",
        "opponent": "Seattle Seahawks"
    },
    {
        "week": 2,
        "date": "Sunday, Sept. 20, 2026",
        "time": "12:00 PM CST",
        "location": "Gillette Stadium (Foxborough, MA)",
        "opponent": "Pittsburgh Steelers"
    },
    {
        "week": 3,
        "date": "Sunday, Sept. 27, 2026",
        "time": "12:00 PM CST",
        "location": "EverBank Stadium (Jacksonville, FL)",
        "opponent": "Jacksonville Jaguars"
    },
    {
        "week": 4,
        "date": "Sunday, Oct. 4, 2026",
        "time": "12:00 PM CST",
        "location": "Highmark Stadium (Orchard Park, NY)",
        "opponent": "Buffalo Bills"
    },
    {
        "week": 5,
        "date": "Sunday, Oct. 11, 2026",
        "time": "12:00 PM CST",
        "location": "Gillette Stadium (Foxborough, MA)",
        "opponent": "Las Vegas Raiders"
    },
    {
        "week": 6,
        "date": "Sunday, Oct. 18, 2026",
        "time": "12:00 PM CST",
        "location": "Gillette Stadium (Foxborough, MA)",
        "opponent": "New York Jets"
    },
    {
        "week": 7,
        "date": "Thursday, Oct. 22, 2026",
        "time": "7:15 PM CST",
        "location": "Soldier Field (Chicago, IL)",
        "opponent": "Chicago Bears"
    },
    {
        "week": 8,
        "date": "Sunday, Nov. 1, 2026",
        "time": "3:25 PM CST",
        "location": "Hard Rock Stadium (Miami Gardens, FL)",
        "opponent": "Miami Dolphins"
    },
    {
        "week": 9,
        "date": "Sunday, Nov. 8, 2026",
        "time": "3:25 PM CST",
        "location": "Gillette Stadium (Foxborough, MA)",
        "opponent": "Green Bay Packers"
    },
    {
        "week": 10,
        "date": "Sunday, Nov. 15, 2026",
        "time": "8:30 AM CST",
        "location": "Allianz Arena (Munich, Germany)",
        "opponent": "Detroit Lions"
    },
    {
        "week": 11,
        "date": "BYE WEEK",
        "time": "BYE, N/A",
        "location": "N/A",
        "opponent": "N/A"
    },
    {
        "week": 12,
        "date": "Sunday, Nov. 29, 2026",
        "time": "7:20 PM CST",
        "location": "SoFi Stadium (Inglewood, CA)",
        "opponent": "Los Angeles Chargers"
    },
    {
        "week": 13,
        "date": "Sunday, Dec. 6, 2026",
        "time": "3:25 PM CST",
        "location": "Gillette Stadium (Foxborough, MA)",
        "opponent": "Buffalo Bills"
    },
    {
        "week": 14,
        "date": "Thursday, Dec. 10, 2026",
        "time": "7:15 PM CST",
        "location": "Gillette Stadium (Foxborough, MA)",
        "opponent": "Minnesota Vikings"
    },
    {
        "week": 15,
        "date": "Monday, Dec. 21, 2026",
        "time": "7:15 PM CST",
        "location": "GEHA Field at Arrowhead Stadium (Kansas City, MO)",
        "opponent": "Kansas City Chiefs"
    },
    {
        "week": 16,
        "date": "Sunday, Dec. 27, 2026",
        "time": "12:00 PM CST",
        "location": "MetLife Stadium (East Rutherford, NJ)",
        "opponent": "New York Jets"
    },
    {
        "week": 17,
        "date": "TBD (Jan. 2/3, 2027)",
        "time": "TBD - Flex Game",
        "location": "Gillette Stadium (Foxborough, MA)",
        "opponent": "Denver Broncos"
    },
    {
        "week": 18,
        "date": "TBD (Jan. 9/10, 2027)",
        "time": "TBD - Flex Game",
        "location": "Gillette Stadium (Foxborough, MA)",
        "opponent": "Miami Dolphins"
    }
]



## Changing a List's Items

ajbrown_altnames = ["A.J. Brown", "Arthur Juan Brown", "A.O."]
print(ajbrown_altnames[1])

#   1. Using an Index:
#       assigning a new value to an item in the list
ajbrown_altnames[1] = "Swole Batman"
print(ajbrown_altnames[1])


#   2. Using a Slice:
#       assigning a new value to multiple items in the list
ajbrown_altnames[0:2] = ["A.J. Man-Down", "Downtown Brown", "Touchdown Brown"]
print(ajbrown_altnames)

## Deleting a List's Items
del ajbrown_altnames[0]
print(ajbrown_altnames)



## String & List Similarities

aj_1k = ["1k", "Always", "Open", "A.O"]

# 1. len Function
print(str(len(aj_1k)))

# 2. List Concatenation
exampleList_2 = [1, 2, 3, 4, 5]
print(str(aj_1k[0]) + " " + str(aj_1k[1]) + " " + str(aj_1k[2]))

# 2. List Replication
print(str(aj_1k[0]) * 3)

# 3. list() Function
#       similar to str() & int(), converts values passed to it into a list
print(list("Kam"))

# 4. in & not in Operators
if "K" in list("Kam"):
    print("K is in Kam")
else:
    print("K is NOT in Kam")

if "L" not in list("Kam"):
    print("L is NOT in Kam")
else:
    print("L is in Kam")

print()

# -------------------------------------------------------------
# CONCEPT: Indexes
# -------------------------------------------------------------

# SINGLE Item
# BEGINNING WITH 0

# 1. Indexing Lists
# Accessing a single item (assigned a value) in a list using an Integer Index for the item's position in the list
print(pats_opponents[0])
print(pats_opponents[10])
print(pats_opponents[17])
print()

# 2. Indexing Lists of Lists
print("Week " + str(pats_schedule[0]["week"]) + ": The " + team + " play the " + pats_schedule[0]["opponent"] + " on " + pats_schedule[0]["date"] + " at " + pats_schedule[0]["time"] + " @ " + pats_schedule[0]["location"] + ".")
print(pats_schedule[10]["date"])
print(pats_schedule[17]["opponent"])
print()



# Negative Indexes
#   [-1] is the LAST item in the list

print("The " + team + " have their " + pats_schedule[-8]["date"] + " in Week " + str(pats_schedule[-8]["week"]))
print()

# -------------------------------------------------------------
# CONCEPT: Slices
# -------------------------------------------------------------

# MULTIPLE Items/Values, aka a new List
# Evaluates to a new List Value
# BEGINNING WITH 0

# Accessing multiple values from a list
#   [0:10] = 1st item -> 10th item
#       0 = Index 0 = 1st item in List
#       10 = Index 10 = 11th item in List (is NOT INCLUDED)
#       MEANING it goes up to, but NOT including, the 11th item


# printing each week's info as slices but EXCLUDING TBD/Flex Games (last 2 weeks)
# also defining game (refresher on how to create an Iteration Variable)
#   Iteration Variable: aka Loop Variable, temporary variable that gets reassigned to each item in the list on every iteration of the loop
#       only exists inside the loop (below) where it's defined/used and has no meaning outside of it
for game in pats_schedule[0:16]:
    print("Game " + str(game["week"]) + ": " + team + " vs " + game["opponent"] + " on " + game["date"] + " at " + game["time"] + " @ " + game["location"])
print("\n")



# Slice Shortcuts

nfl_positions = ["QB", "RB", "FB", "WR", "TE", "C", "LG", "RG", "LT", "RT", "DE", "DT", "NT", "EDGE", "ILB", "OLB", "MLB", "CB", "FS", "SS", "K", "P", "LS", "H", "KR", "PR"]
print("All NFL Positions:")

print("Offense: " + str(nfl_positions[:10]))     # start of list to x

print("Defense: " + str(nfl_positions[10:20]))

print("Offense: " + str(nfl_positions[20:]))     # x to end of list