"""
Sample Output:

Enter input file name: small-average.txt
The average is 71.3
The percentage of people above average is 60.0
The student is above the average
"""

debugMode = False

if debugMode:
    fileName = "small-average.txt"
else:
    fileName = input('Enter input file name: ')

file = open(fileName, 'r').readlines()

# init variables
total = 0 
length = 0
aboveAvgPercent = 0

for items in file:
    total += int(items)
    length += 1

avg = total / length # calc avg

for g in file:
    if int(g) > avg:
        aboveAvgPercent += 1

aboveAvgPercent = (aboveAvgPercent / length) * 100 # calculate people above average percentage

print("The average is " + str(avg))
print("The percentage of people above average is " + str(aboveAvgPercent))

# Implement above average 
if avg >= aboveAvgPercent:
    print("The student is above average")
else:
    print("The student is not above average")
