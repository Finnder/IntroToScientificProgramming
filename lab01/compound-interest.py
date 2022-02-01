# Compound Interest
# By: Finnegan McGuire
# Status: Complete

debugMode = False # Allows for a quick way to test a set of numbers (what I used to debug my program)

# Gather user input
if not debugMode:
    P = input('Enter the principal amount: ')
    r = input('Enter the rate of interest: ')
    n = input('Enter the number of times interest is compounded in a year: ')
    t = input('Enter the total number of years borrowed: ')
else:
    # Variables are string to simulate user input (input values are initially strings)
    P = '5000'
    r = '5'
    n = '12'
    t = '10'

# Convert user input into integers
P = int(P)

r = int(r)
r = r / 100 # Change into a percentage (Ex: 5 -> 0.05 OR 5%)

n = int(n)
t = int(t)

# Calculate compound interest
A = P * (1 + (r/n)) ** (n*t)

# Round number to 2 decimal places
A = round(A, 2)

# Display the compounded interst of P to the user
print('The total amount paid is ', A)
