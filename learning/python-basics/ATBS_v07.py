# =============================================================
# Kam McIntire | Sports Analytics Journey
# VIDEO 7: for Loops & range() Function
# Source: Automate the Boring Stuff - Al Sweigart
# Date: 06/11/2026
# =============================================================

# CONCEPTS COVERED:
#   for Loops
#       

# -------------------------------------------------------------
# CONCEPT: for Loops
# -------------------------------------------------------------

# Iterates a Loop a specific # of itmes

#Total sum of numbers 1-100, excluding 50
total = 0
# range() Function
for x in range(1, 101, 1):
#                      ^ "Step Argument"
    if x == 50:
        continue
    total = total + x
print(str(total))

# while Loop equivalent of a for Loop
y = 0                   # change
total2 = 0
while y < 100:
    y = y + 1           # change
    if y == 50:
        continue
    total2 = total2 + y
print(str(total2))

# -------------------------------------------------------------
# CONCEPT: range() Function
# -------------------------------------------------------------

# Format of a range() Function:
#   format(Min, Max (but not including), Step Argument)
z = 0
for z in range(0, 10, 2):
    print(str(z))