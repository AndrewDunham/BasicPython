startingPounds = int(input("What is your starting lifting weight? (in lbs)"))
addWeight = input("Would you like to add more weight? (yes or no)")
if (addWeight == "yes"):
  pounds = int(input("Which plate did you add to one side of the bar? (in lbs)")
  totalPounds = startingPounds + (pounds * 2) + 45
addWeight = input("Would you like to add more weight? (yes or no)")

if (addWeight == "yes"):
  morePounds = int(input("Which plate did you add to one side of the bar? (in lbs)")
  totalPounds += (morePounds * 2)
  addWeight = input("Would you like to add more weight? (yes or no)")
else:
  print("your total weight was:" totalPounds)
