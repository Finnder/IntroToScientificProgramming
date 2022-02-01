# Random Card
# By: Finnegan McGuire
# Status: Complete

import random

# Minimum and Maximum Range Of Random Int [Default: 0 - 51]
MIN = 0
MAX = 51

# Get Random Number For Random Card
randomCardNumber = random.randint(MIN, MAX)

# Gets the card type using a number
# Returns -> String
def GetCardType(number):

    # CLUBS
    if number >= 0 and number <= 12:
        return "Clubs"
    
    # DIAMONDS
    elif number >= 13 and number <= 25:
        return "Diamonds"

    # HEARTS
    elif number >= 26 and number <= 38:
        return "Hearts"

    # SPADES
    elif number >= 39 and number <= 51:
        return "Spades"

# Gets the card number words or special words depending on the number
# Returns -> String
def GetCardNumber(number):
    if number == 0:
        return "Ace"
    
    elif number == 1:
        return "Two"

    elif number == 2:
        return "Three"

    elif number == 3:
        return "Four"

    elif number == 4:
        return "Five"

    elif number == 5:
        return "Six"

    elif number == 6:
        return "Seven"

    elif number == 7:
        return "Eight"

    elif number == 8:
        return "Nine"

    elif number == 9:
        return "Ten"

    elif number == 10:
        return "Jack"
    
    elif number == 11:
        return "Queen"

    elif number == 12:
        return "King"

# Generate and Calculate Correct Output For User
# Returns -> String
def GenerateOutput():
   cardType = GetCardType(randomCardNumber)    
   cardNumber = None

   if cardType == "Clubs":
       cardNumber = GetCardNumber(randomCardNumber)

   elif cardType == "Diamonds":
       cardNumber = GetCardNumber(randomCardNumber - 13)
   
   elif cardType == "Hearts":
       cardNumber = GetCardNumber(randomCardNumber - 26)

   elif cardType == "Spades":
       cardNumber = GetCardNumber(randomCardNumber - 39)

   formatedString = f"This card is: {cardNumber} of {cardType}"
   return formatedString


# Display Output to user
print("Random Number: ", randomCardNumber)
print(GenerateOutput())


# Rules
"""
Types
0-12 -> Clubs
13-25 -> Diamonds
26-38 -> Hearts
39-51 -> Spades

Ranges Example
[0-12] -> 0=Ace 1=Two 2=Three... 9=Ten 10=Jack 11=Queen 12=King
Example: 11 = Queen Of Clubs
"""
