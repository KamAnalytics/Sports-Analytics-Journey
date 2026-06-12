# =============================================================
# Kam McIntire | Sports Analytics Journey
# VIDEO 6: while Loops
# Source: Automate the Boring Stuff - Al Sweigart
# Date: 06/10/2026
# =============================================================

# CONCEPTS COVERED:
#   while Loops
#       break & continue Statements

# -------------------------------------------------------------
# CONCEPT: while Loops
# -------------------------------------------------------------

# execution returns to the start of the while Loop until a condition is False
#   GREAT for "Input Validation" as it loops to ensure a valid input for the program
#   unlike an if Statement which ends after all conditions are executed
# Iteration: 1 execution through a Loop

intro = 0
while intro < 3:
    print("Welcome!")
    intro = intro + 1
# "this while Loop iterates 3 times"
print()

name = ""
# (while Statements need to evaluate at least something immediately)

while name != "your name":
    print("In order to continue, please type your name:" )
    name = input()
print("Thank you!")
print()

#   break Statements
#       jumps execution out of the Loop

# !Infinite Loop!
while True:     # this can never be False
    print("In order to continue, please type your name:" )

    name = input()
    if name == "your name":
        break
print("Thank you!")
print()

#   continue Statements
pass_play = 0
while pass_play < 4:
    pass_play = pass_play + 1
    if pass_play == 2:
        continue
    if pass_play == 4:
        continue
    print("Drive #1: Passing Play on " + str(pass_play) + " down.")
print()

drive1_plays = ["kickoff", "pass", "run", "pass", "penalty", "run", "run", "sack", "punt"]
pass_count = 0
for play in drive1_plays:
    if play != "pass":
        continue
    pass_count = pass_count + 1
#       or pass_count += 1
    print("Drive #1: Passing play #" + str(pass_count) + " recorded.")