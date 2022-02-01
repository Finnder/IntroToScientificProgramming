# Rock, Paper, Scissors
# By: Finnegan McGuire
# Status: Complete

import random

choices = ('rock', 'paper', 'scissors')

# Is the game running?
running = True

# Returns -> String
def BotChoice():
    x = random.randint(0, 2)
    return choices[x]

# Game Loop
while running:
    print('Lets play a game of Rock, Paper and Scissors')
    
    botChoice = BotChoice() # Gets random choice for bot

    userChoice = input('I have selected mine, what do you select [type rock, paper or scissors]?')
    
    if userChoice.lower() == 'rock':
        if botChoice == 'rock':
            print("I chose rock. You chose rock. It's a tie")
        
        elif botChoice == 'paper':
            print("I chose paper. You chose rock. I win.")
        
        elif botChoice == 'scissors':
            print("I chose scissors. You chose rock. You win.")
            
    
    elif userChoice.lower() == 'paper':
        if botChoice == 'rock':
            print("I chose rock. You chose paper. You win.")
            
        elif botChoice == 'paper':
            print("I chose paper. You chose paper. It's a tie.")
            
        elif botChoice == 'scissors':
            print("I chose scissors. You chose paper. I win.")
            

    elif userChoice.lower() == 'scissors':
        if botChoice == 'rock':
            print("I chose rock. You chose scissors. I win.")
            
        elif botChoice == 'paper':
            print("I chose paper. You chose scissors. You win")
            
        elif botChoice == 'scissors':
            print("I chose scissors. You chose scissors. It's a tie")

    else:
        print('Thanks for playing!')
        running = False # Stops while loop

    print(" ") # Spacer

