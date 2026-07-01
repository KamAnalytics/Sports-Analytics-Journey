# =============================================================
# Kam McIntire | Sports Analytics Journey
# VIDEO 15: Methods
# Source: Automate the Boring Stuff - Al Sweigart
# Date: 06/29/2026 - Last updated 06/30/2026
# =============================================================

# CONCEPTS COVERED:
#   Methods
#       List Methods:
#           1. index()
#           2. append()
#           3. insert()
#           4. remove()
#           5. sort()
#               - "ASCII-betical" Order NOT Alphabetical Order

# -------------------------------------------------------------
# CONCEPT: Methods
# -------------------------------------------------------------

# Methods: same as a function, but it's called on a value
#   list.METHOD()


# index()
def nhl_goal_leaders_2526():
    leaders_2526 = ["Nathan MacKinnon", "Cole Caufield", "Connor McDavid", "Macklin Celebrini", "Jason Robertson"]
    
    players = "Cole Caufield", "Wayne Gretzky", "Macklin Celebrini"
    for player in players:
        try:
            print(player + " is at Index " + str(leaders_2526.index(player)))
        except ValueError:
            print(player + "is not in this list")
nhl_goal_leaders_2526()
print()

# QUESTION: If a List has duplicated items, does the index() Method return both?
# ANSWER: No, only the first one

myName_letters_1 = list("Kameron McIntire")
print(myName_letters_1.index("n"))

print(list("Kameron McIntire").index("e"))
print()


# LIST METHODS:
# append(), insert(), remove(), & sort()

# append()
#   adds new items to the END of a List
myName_letters_2 = ["K", "a", "m"]
myName_letters_2.append("e")
myName_letters_2.append("r")
myName_letters_2.append("o")
myName_letters_2.append("n")
print(myName_letters_2)
print()

# insert()
#   adds new items to a SPECIFIC INDEX of a list
#   listName.insert(POSITION, ITEM)
myName_letters_3 = ["K", "m", "r", "n"]
myName_letters_3.insert(1, "a")
myName_letters_3.insert(3, "e")
myName_letters_3.insert(5, "o")
print(myName_letters_3)
print()

# remove()
#   removes an item from a List
ant_teammates = ["Lamelo Ball", "Naz Reid", "Jaden McDaniels", "Karl-Anthony Towns", "Nickeil Alexander-Walker"]
ant_teammates.remove("Naz Reid")
ant_teammates.remove("Karl-Anthony Towns")
print("Anthony Edwards' Teammates (2026-27 Season): " + ", ".join(ant_teammates))
print()

# QUESTION: What's the difference between 'del list[index]' and 'list.remove(item)'?
# ANSWER: del removes by INDEX #, .remove() removes by VALUE

# QUESTION: Does del and/or remove() delete multiple/duplicated items in a List?
# ANSWER: No, BOTH only delete the first instance. To remove all, use a Loop or call del/remove() multiple times

# sort() & sorted()
#   Lists with int or str can be sorted
#       sort() is a METHOD
#       sorted() is a FUNCTION (standalone: "sorted()")



print("2026 NFL Combine Top 10 40-yard Dashes:\n")

# Original paired data (name, time) - keeps them together
combine = [
    ("Bryce Lance", 4.34),
    ("Mike Washington Jr.", 4.33),
    ("Treydan Stukes", 4.33),
    ("Robert Spears-Jennings", 4.32),
    ("Toriano Pride Jr.", 4.32),
    ("Jeff Caldwell", 4.31),
    ("Deion Burks", 4.30),
    ("Zavion Thomas", 4.28),
    ("Lorenzo Styles Jr.", 4.27),
    ("Brenen Thompson", 4.26)
]

# Times (numerically)
times = sorted([x[1] for x in combine])
print("Times (fastest -> slowest): " + str(times) + "\n")


# Names (alphabetically)
names = sorted([x[0] for x in combine])
print("Players (alphabetically): " + ", ".join(names) + "\n")


# Paired (fastest -> slowest)
combine.sort(key=lambda x: x[1])            # lambda sorts tuples by a specific element (without Pandas)
print("Fastest -> Slowest:")
for i, (name, time) in enumerate(combine):  # enumerate(list) loops through a List and outputs the INDEX AND VALUE at the same time 
    print("#" + str(i + 1) + " " + name + ": " + str(time))
print("\n")



# sort() uses "ASCII-betical" Order, not Alphabetical Order
#   uppercase characters come before lowercase characters

ascii_betical = ["aaa", "BBB", "ZZZ", "ccc"]
ascii_betical.sort()
print("\"ASCII\"-betical: " + str(ascii_betical))
print()


# for true Alphabetical Order, pass: key=str.lower
alphabetical = ["aaa", "BBB", "ZZZ", "ccc"]
alphabetical.sort(key=str.lower)
print("Alphabetical: " + str(alphabetical))