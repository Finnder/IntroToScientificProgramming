import random

# yahtzee.py 
attempts = 0
rolls = 0

def rollDice():
    return random.randint(1, 6)

def experiment():
    firstRoll = []
    for i in range(6):
       firstRoll.append(rollDice())

experiment()

print(f'In expectation, it takes {attempts} attemps to roll {rolls} sixes')
