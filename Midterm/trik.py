# Trik
# By: Finnegan McGuire
# Status: Complete

move = input("Enter the move string: ")

coinLocation = []

currentCup = 2

# Add user data to array
for i in move:
    coinLocation.append(i)

def SwapCups(locations):
    global currentCup
    for location in locations:
        if location.upper() == 'A':
            if currentCup == 1:
                currentCup += 1

            elif currentCup == 2:
                currentCup -= 1

        elif location.upper() == 'B':
            if currentCup == 2:
                currentCup += 1 

            elif currentCup == 3:
                currentCup -= 1
        
        elif location.upper() == 'C':
            if currentCup == 1:
                currentCup += 2

            elif currentCup == 3:
                currentCup -= 2

def Output() :
    output = ""

    if currentCup == 1:
        output = "Coin in first cup"
    elif currentCup == 2:
        output = "Coin in second cup"
    elif currentCup == 3:
        output = "Coin in third cup"

    print(output)

SwapCups(coinLocation)
Output()

"""
Sample inputs and outputs:
    Enter the move string: ABC
    Coin in third cup.
    Enter the move string: ACBC
    Coin in second cup.
"""
