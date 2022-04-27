"""
Sample Output:

Enter input file name: small-average.txt
The average is 71.3
The percentage of people above average is 60.0
The student is above the average
"""

debugMode = True

if debugMode:
    fileName = "small-average.txt"
else:
    fileName = input('Enter input file name: ')

with open(fileName, 'r') as file:
    total = 0 
    i = 0
    aboveAvgPercent = 0
    
    for items in file:
        total += int(items)
        i += 1

    avg = total / i

    for items in file:
        if int(items) > avg:
            aboveAvgPercent += 1
    
print("The average is " + str(avg))
print("The percentage of people above average is " + str(aboveAvgPercent))
    

    
