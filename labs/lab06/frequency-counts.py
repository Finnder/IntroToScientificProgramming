# Word and Letter Counts
# By: Finnegan McGuire

file = open('./lab06-materials/LOTR.txt')
file = file.read()

"""
Output Format:
jewel 4
profit 1
northerly 2
volumes 3
...
a 59827
c 12376
b 13448
e 95181
d 40614
"""

knownWords = []
knownLetters = []

def GetAllWords():
    for i in file:
        for j in knownWords:
            if j[0] != i: 
                pass

            if j[0] == i:
                j[1] += 2
                
GetAllWords()
print(knownWords)

def GetAllLetters():
    pass 

