# Radio Active
# By: Finnegan McGuire
# Status: Complete
import math

# Gathering User Input
initialAmount = input('Enter the initial amount of Carbon-14 in the artifact (in grams): ')
currentAmount = input('Enter the current amount of Carbon-14 in the artifact (in grams): ')

# Turning user input from strings to int
initialAmount = int(initialAmount)
currentAmount = int(currentAmount)

# Initializing Variables
ageOfArtifact = 0
e = 2.7183
k = 3.9 * (10 ** -12) # Or (3.9e-12)
oneYearInSec = 31536000	

# Calculating Age Of The Artifact
sec_ageOfArtifact = (math.log(initialAmount/currentAmount)) / (k)
year_ageOfArtifact = round(sec_ageOfArtifact / oneYearInSec, 2)


# Displaying Age of the artifact
print(year_ageOfArtifact)
