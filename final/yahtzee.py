import random

# yahtzee.py 
total = 0
avgAttempts = 0

def rollDice():
    return random.randint(1, 6)

def experiment():
    attempts = 0

    currentRoll = [0, 0, 0, 0, 0]
    while currentRoll != [6, 6, 6, 6, 6]:

        currentRoll = [rollDice(), rollDice(), rollDice(), rollDice(), rollDice()]

        attempts += 1

    return attempts

    
for i in range(1000):
    total += experiment()

avgAttempts = total / 1000

print(f'In expectation, it takes {avgAttempts} attemps to roll 5 sixes')
