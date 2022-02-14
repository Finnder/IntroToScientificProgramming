# Multiplying Rabbits
# By: Finnegan McGuire
# Status: Incomplete

"""
Sample Input and Output:
Enter total months: 10
There will be 89 pairs of rabbits.
"""

while True:

    try:
        # Gets user input for amount of months gone by
        months = int(input('Enter total months: '))
        break

    except ValueError:
        print("Please enter a valid number") 
    
# Generate pairs of rabits depending on months gone by
def pairsOfRabbits(number_of_months):

    # Initialize Variables
    childPairs = 1
    maturePairs = 0 
    previousChildCount = childPairs

    # If user entered 2 or less months. No rabbits are created untill month 3
    if number_of_months <= 2:
        return 1

    # Adding +1 to account for months past
    for months in range(number_of_months):
        
        previousChildCount = childPairs 
        
        # The month that the first pair becomes mature (start generating rabbits)
        if months == 1:
            maturePairs = 1

        childPairs = maturePairs 
        maturePairs += previousChildCount

    totalPairs = maturePairs + childPairs

    return totalPairs

# Run the function -> outputs rabbits after x amount of months
amountOfPairs = pairsOfRabbits(months)

print("There will be " + str(amountOfPairs) + " pairs of rabbits.")

















