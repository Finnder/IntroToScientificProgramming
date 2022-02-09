# Tax Calculation
# By: Finnegan McGuire
# Status: Complete

# Gather user input
print('This program computes taxes for the year 2020 for singles.')
userIncome = int(input("Enter Taxable Income: "))

# Determine income bracket rate
# Returns -> Float
def IncomeBracketRate(income):
    if income >= 0 and income <= 9700: # Make it more simple by just using 'income <= 9700'
        return 0.10

    elif income >= 9701 and income <= 39475:
        return 0.12

    elif income >= 39476 and income <= 84200:
        return 0.22

    elif income >= 84201 and income <= 160725:
        return 0.24

    elif income >= 160726 and income <= 204100:
        return 0.32

    elif income >= 204101 and income <= 510300:
        return 0.35

    elif income > 510300:
        return 0.37

# Gather User Rate
userRate = IncomeBracketRate(userIncome)

# Gather Tax Owed
userTaxOwed = round(userIncome * userRate)

# Display Info To User
print(f'Total tax owed is {userTaxOwed}')

# Rates to Income Bracket Data 
"""
Rate & Income Bracket
--- ------------------
10% $0 to $9,700
12% $9,701 to $39,475
22% $39,476 to $84,200
24% $84,201 to $160,725
32% $160,726 to $204,100
35% $204,101 to $510,300
37% $510,300+
"""
