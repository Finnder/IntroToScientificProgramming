fruitsFile = open('lab04-materials/fruits.txt', 'r')

fruitToFind = 'avocado'
numberOfFruit = 0

for lines in fruitsFile:
    print(lines)
    if(lines == fruitToFind):
        numberOfFruit += 1


    
print('The number of avocados is ', numberOfFruit)

