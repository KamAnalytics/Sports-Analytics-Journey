import datetime

name = "Kam"

# datetime = module imported above
# .date = specific class in the module that deals with calendar dates (not times)
# .today() = grabs today's date from the system clock
today = datetime.date.today()

goal = "Sports Performance & Decision Analyst - NFL/NBA Front Office"

# f-strings
## f = tells python: "this string contains variables, swap them in"
## {} = contents that get replaced with their values
print(f"Name: {name}")
print(f"Day 1 Date: {today}")
print(f"Goal: {goal}")
print("Setup complete. No more excuses.")