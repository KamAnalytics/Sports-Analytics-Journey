# =============================================================
# Kam McIntire | Sports Analytics Journey
# VIDEO 14: for w/ Lists, Multiple & Augmented Assignments
# Source: Automate the Boring Stuff - Al Sweigart
# Date: 06/28/2026
# =============================================================

# CONCEPTS COVERED:
#   for Loops with Lists
#       -  (Step Argument refresher)
#       1. "Sequences" vs. Lists
#       2. for i in range(len(listNAME))
#   Multiple Assignment
#       1. When to use a List or Dictionary
#       2. Swapping Variables
#   Augmented Assignment Operators
#       1. +=  -=  *=  /=
#       2. %=  Modulus (remainder) Operator

# -------------------------------------------------------------
# CONCEPT: for Loops with Lists
# -------------------------------------------------------------

# range object in range(4) = [0, 1, 2, 3]
for week in range(4):
    print(week)
print()
# this is technically called a Sequence, or 'List-like'

print(list(range(4)))
# THIS will return a list - use list() Function
print()

by5 = list(range(0, 100, 5))
print(by5)
print()


# for i in range(len(listNAME))
#   useful for getting both the #'d order and value of items in a List
#       (in other words)
#   use i to refer to the (integer) index AND the list value assigned to that index

print("MLB Home Run Leaders (2025 Season):")
mlb_HR_leaders_2025 = ["Cal Raleigh", "Kyle Schwarber", "Shohei Ohtani", "Aaron Judge", "Eugenio Suarez"]

for i in range(len(mlb_HR_leaders_2025)):
    print("#" + str(i + 1) + ": " + mlb_HR_leaders_2025[i])
# in this example, i refers to the player's placement in the Top 5 AND their name
print()

# -------------------------------------------------------------
# CONCEPT: Multiple Assignment
# -------------------------------------------------------------

print("2026 NBA Finals Stats:")
# Instead of...
wemby_finals_stats = [38, 19, 14, 2, 0, 5, -3, 2, 3, "7-19", "1-6", "4-5"]
MIN = wemby_finals_stats[0]
PTS = wemby_finals_stats[1]
REB = wemby_finals_stats[2]
AST = wemby_finals_stats[3]
STL = wemby_finals_stats[4]
BLK = wemby_finals_stats[5]
PLUS_MINUS = wemby_finals_stats[6]
TO = wemby_finals_stats[7]
PF = wemby_finals_stats[8]
FG = wemby_finals_stats[9]
THREE_PT = wemby_finals_stats[10]
FT = wemby_finals_stats[11]
# print("Victor Wembanyama | " + str(MIN) + " MIN | " + str(PTS) + " PTS | " + str(REB) + " REB | " + str(AST) + " AST | " + str(STL) + " STL | " + str(BLK) + " BLK | " + str(PLUS_MINUS) + " +/- | " + FG + " FG | " + THREE_PT + " 3PT | " + FT + " FT")

# Use...
PLAYER, MIN, PTS, REB, AST, STL, BLK, PLUS_MINUS, TO, PF, FG, THREE_PT, FT = ["Victor Wembanyama", 38, 19, 14, 2, 0, 5, -3, 2, 3, "7-19", "1-6", "4-5"]
print(PLAYER + " | " + str(MIN) + " MIN | " + str(PTS) + " PTS | " + str(REB) + " REB | " + str(AST) + " AST | " + str(STL) + " STL | " + str(BLK) + " BLK | " + str(PLUS_MINUS) + " +/- | " + FG + " FG | " + THREE_PT + " 3PT | " + FT + " FT")
print()

# NOTE:
# use dictionaries with multiple players
#   wemby_finals_stats = {"MIN": 38, "PTS": 19}
#   brunson_finals_stats = {"MIN": 41, "PTS": 45}

# Another example:

# Kam:
age, hair_color, eye_color = [25, "brown", "hazel"]

# QUESTION: What if I wanted to be able to name and call/reference the List, its Variables, AND Values?
# ANSWER:
age, hair_color, eye_color = kam = [25, "brown", "hazel"]

# QUESTION: What if I wanted to do this for multiple people?
# ANSWER: again, use dictionaries with multiple people
# DO NOT ALSO USE:
age, hair_color, eye_color = fakeKam = [26, "blue", "green"]
# This is because calling print(age) (in any applicable context) will overlap with both data sets (and only output the recent assignment)



# Swapping Variables

# Point Leaders of a Game:
wemby_pts, ant_pts = 25, 20

rank1, rank2 = "Victor Wembanyama", "Anthony Edwards"
print("#1: " + rank1 + " | " + str(wemby_pts) + " PTS")
print("#2: " + rank2 + " | " + str(ant_pts) + " PTS")
print()


wemby_pts, ant_pts = 25, 28

if ant_pts > wemby_pts:
    rank1, rank2 = rank2, rank1
    wemby_pts, ant_pts = ant_pts, wemby_pts
print("#1: " + rank1 + " | " + str(wemby_pts) + " PTS")
print("#2: " + rank2 + " | " + str(ant_pts) + " PTS")
print()

# -------------------------------------------------------------
# CONCEPT: Augmented Assignment Operators
# -------------------------------------------------------------

#   +=  -=  *=  /=  %=  ...and more

date = "06/28/2026"
my_age = 25

print("Today, " + date + ", I am " + str(my_age) + " years old.")


date = "03/15/2027"

if date == "03/15/2027":
    my_age += 1
    print("On " + date + ", I will be " + str(my_age) + " years old.")
print()



#   %=
num = 10
print(num)

num %= 4
print(num)