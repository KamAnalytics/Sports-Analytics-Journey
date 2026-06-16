# =============================================================
# Kam McIntire | Sports Analytics Journey
# VIDEO 9: Custom Functions, return Statements, None Values, & Keyword Arguments
# Source: Automate the Boring Stuff - Al Sweigart
# Date: 06/12/2026 - Last updated 06/15/2026
# =============================================================

# CONCEPTS COVERED:
#   Custom Functions
#   return Statements
#   None Value
#       (which is essentially the default return Statement - as in print())
#       no return Value means None is the return Value
#   Keyword Arguments

# -------------------------------------------------------------
# CONCEPT: Custom Functions
# -------------------------------------------------------------

# Useful for getting rid of duplicate code & grouping code that gets executed multiple times

def wemby():
    print("Name: Victor Wembanyama")
    print("Team: San Antonio Spurs")
    print("Position: C")
    print("Jersey: #1")
    print("Height: 7'4\"")
    print("Weight: 210 lbs")
    print("Age: 21")
    print("College: N/A (French League)")
    print("Draft: 2023, Pick #1 Overall")
wemby()
print()

# Terms:
#   Parameter vs. Argument
#   BOTH: Within the Parenthesis

#   Parameter: IN def STATEMENT ONLY
#       ex: def function(PARAMETER)
#   Argument: INPUT to functions, assigned to Parameters
#       ex: function("ARGUMENT")

#       Return: OUTPUT of functions

# Parameter
def kams_function(parameter):
    print(parameter)

# Argument
kams_function("argument")
print("")

#   De-duplicating: getting rid of duplicated or copy/pasted code
#   Parameter: Within a def statement's parenthesis
#       def function(parameter)

# -------------------------------------------------------------
# CONCEPT: Return Statements
# -------------------------------------------------------------

# Allows you to specify the return Value
# Sends a value back to whoever called the function
def season_year(season_num):
    seasons = {1: "2009-10", 2: "2010-11", 3: "2011-12"}
    return seasons[season_num]
print(season_year(3))
# 2011-12

# if your function doesn't have a return Statement, the default return is None (value)
# such as:
print("\n")

# another return Statement use case
#   also includes some entries having an additional key
player = "Steph Curry"
curry_3pm = {
    "2009-10": {"season": 1, "3pm": 166},
    "2010-11": {"season": 2, "3pm": 151},
    "2011-12": {"season": 3, "3pm": 55, "fun_fact": player + " played only 26 games this season due to recurring right ankle injuries and surgery."},
    "2012-13": {"season": 4, "3pm": 272},
    "2013-14": {"season": 5, "3pm": 261},
    "2014-15": {"season": 6, "3pm": 286},
    "2015-16": {"season": 7, "3pm": 402, "fun_fact": player + " held the NBA single-season 3PM record at the time. He was also named the unanimous MVP."},
    "2016-17": {"season": 8, "3pm": 324},
    "2017-18": {"season": 9, "3pm": 212},
    "2018-19": {"season": 10, "3pm": 354},
    "2019-20": {"season": 11, "3pm": 12, "fun_fact": player + " played just 5 games this season due to a broken hand suffered in October 2019."},
    "2020-21": {"season": 12, "3pm": 337},
    "2021-22": {"season": 13, "3pm": 285},
    "2022-23": {"season": 14, "3pm": 273},
    "2023-24": {"season": 15, "3pm": 357},
    "2024-25": {"season": 16, "3pm": 311},
    "2025-26": {"season": 17, "3pm": 190},
}
print("Provide Steph Curry's season number (1-17) to look up 3PM totals for that season.")
def curry_season_3pm():
    player = input("Player (Enter \"Steph Curry\"): ")
    while player.title() != "Steph Curry":
        print("This program only supports Steph Curry.")
        player = input("Player (Enter \"Steph Curry\"): ")
    season = int(input("Season #: "))
    for year, data in curry_3pm.items():                                   # loop dict
        if data["season"] == season:                                       # find matching season
            fun_fact = data["fun_fact"] if "fun_fact" in data else ""
            return year, data["3pm"], fun_fact                             ### return year, 3PM if found as year=[0] and 3PM=[1]
    print(player + " did not play or record any 3PM in that season.")      # if not found
print()

result = curry_season_3pm()                                                # call function, store returned values
print(player + " recorded " + str(result[1]) + " 3PM in the " + str(result[0]) + " season.")
if result[2]:
    print(result[2])
print()

# -------------------------------------------------------------
# CONCEPT: None Value
# -------------------------------------------------------------

# Think of the print() Function as returning the str as a side effect
#   Displays the text representation of what's inside the parenthesis
#   Similar to the True and False Boolean Values
# Only value of the None Data Type

print(None)
# return Value: None (string)

nothing = print()
# nothing = None
print(str(nothing == None))
# return Value: None (value/integer) or blank
print("\n")

# This shows that EVERY Function Call has a 'return' Value
#   no return Value means None is the return Value

# -------------------------------------------------------------
# CONCEPT: Keyword Arguments
# -------------------------------------------------------------

# Optional Arguments to pass to a Function Call

# sep=""
print("ATBS", "v09.py", sep="_")

# end=""
print("Made ", end="")
print("by ", end="")
print("Kam ", end="")
print("McIntire", end="")

# use , for string concatenation
print("Trust", "The", "Process", ":)")