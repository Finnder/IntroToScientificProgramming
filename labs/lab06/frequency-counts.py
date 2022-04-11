# Word and Letter Counts By: Finnegan McGuire


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
knownChar = []

def AppendDictString(word):
   
    dictionary = {
        "word": word,
        "count": 1
    }

    if len(word) == 1:
        knownChar.append(dictionary)
    else:
        knownWords.append(dictionary)


def GetAllWords():
    file = './lab06-materials/LOTR.txt'

    with open(file, 'r') as file:
        for line in file:
            for word in line.split():
                AppendDictString(word)
                for char in word.split():
                    AppendDictString(char)

GetAllWords()

for j in knownWords:
    print(j)
