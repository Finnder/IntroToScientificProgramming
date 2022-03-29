# Counting Avocados
# By: Finnegan McGuire
# Status: Complete

fruitsFile = open('./lab04-materials/fruits.txt', 'r')

fruitToFind = 'avocado' + '\n' # adding the \n because they are hidden after every word
numberOfFruit = 0
fruits = []

for x in fruitsFile:
    fruits.append(x)

for fruit in fruits:
    if fruit == fruitToFind:
        numberOfFruit += 1

fruitsFile.close()

print('The number of avocados is ', numberOfFruit)
