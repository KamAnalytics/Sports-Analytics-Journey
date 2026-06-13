# =============================================================
# Kam McIntire | Sports Analytics Journey
# VIDEO 9: .
# Source: Automate the Boring Stuff - Al Sweigart
# Date: 06/12/2026
# =============================================================

# CONCEPTS COVERED:
#   Custom Functions
#   Return Statements
#   num Value
#   Key Word Arguments

# -------------------------------------------------------------
# CONCEPT: Custom Functions
# -------------------------------------------------------------

# Useful for grouping code that gets executed multiple times

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
#       Parameter: 
#           ex: def function(PARAMETER)
#       Argument: 
#           ex: function("ARGUMENT")
def function(parameter):
    print("function " + "or string " + "+ parameter")

function("argument")
print()

#   De-duplicating: getting rid of duplicated or copy/pasted code
#   Parameter: Within a def statement's parenthesis
#       def function(parameter)

# -------------------------------------------------------------
# CONCEPT: Return Statements
# -------------------------------------------------------------

player = "Steph Curry"
curry_3pm = {
    "2009-10": {"season": 1, "3pm": 166},
    "2010-11": {"season": 2, "3pm": 151},
    "2011-12": {"season": 3, "3pm": 55},
    "2012-13": {"season": 4, "3pm": 272},
    "2013-14": {"season": 5, "3pm": 261},
    "2014-15": {"season": 6, "3pm": 286},
    "2015-16": {"season": 7, "3pm": 402},
    "2016-17": {"season": 8, "3pm": 324},
    "2017-18": {"season": 9, "3pm": 212},
    "2018-19": {"season": 10, "3pm": 354},
    "2019-20": {"season": 11, "3pm": 12},
    "2020-21": {"season": 12, "3pm": 337},
    "2021-22": {"season": 13, "3pm": 285},
    "2022-23": {"season": 14, "3pm": 273},
    "2023-24": {"season": 15, "3pm": 357},
    "2024-25": {"season": 16, "3pm": 311},
    "2025-26": {"season": 17, "3pm": 190},
}

def curry_season_3pm():
    player = input("Player: ")
    season = int(input("Season: "))
    for year, data in curry_3pm.items()       # loop dict
        if data["season"] == season:          # find matching season
            return year, data["3pm"]          # return year and 3PM if found
    print(player + " did not play or record any 3PM in that season.") # if not found

result = curry_season_3pm()                   # call function, store returned values
