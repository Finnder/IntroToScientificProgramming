# Weight Tolerance
# By: Finnegan McGuire
# Status: Complete


# Gather user input
desiredWeight = input('Enter desired weight: ')
tolerance = input('Enter tolerance (as percentage): ')

# Convert input variables into strings
desiredWeight = int(desiredWeight)
tolerance = int(tolerance)

# Calculate 
rangePositive = ((desiredWeight * (tolerance/100)) + desiredWeight)
rangeNegative = (desiredWeight - (desiredWeight * (tolerance/100)))

print(f'The range of accepted wight for the part is from {rangeNegative} to {rangePositive}')

