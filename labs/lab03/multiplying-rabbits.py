# Multiplying Rabbits
# By: Finnegan McGuire
# Status: Incomplete

"""
Sample Input and Output:
Enter total months: 10
There will be 89 pairs of rabbits.
"""

# Rabits to start with
startingRabbits = 2

# Gets user input for amount of months gone by
months = int(input('Enter total months: '))
    
# Generate pairs of rabits depending on months gone by
def rabbitmaker(number_of_months):
    rabbits = startingRabbits

    for x in range(number_of_months):
        rabbits += rabbits ** 2

    print(rabbits)

# Runs the function
rabbitmaker(months)
