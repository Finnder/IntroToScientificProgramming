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

file = './lab06-materials/LOTR.txt'

knownWords = {}
knownChar = {}

with open(file, 'r') as file:
    for line in file:
        for word in line.split():
            if word in knownWords:
                knownWords[word] = knownWords[word] + 1
            else:
                knownWords[word] = 1
            
            print(word.split())

            for char in word:
                if char in knownChar:
                    knownChar[char] = knownChar[char] + 1
                else:
                    knownChar[char] = 1

for j in knownWords:
    print(j, knownWords[j])

for i in knownChar:
    print(i, knownChar[i])


