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

    pairs = 1

    # TODO: Figure out formula to figure out pairs of rabbits
    if number_of_months <= 2:
        pairs = 1

    else:
        pass

    return pairs

# Run the function -> outputs rabbits after x amount of months
amountOfPairs = pairsOfRabbits(months)

print("There will be " + str(amountOfPairs) + " pairs of rabbits.")

















