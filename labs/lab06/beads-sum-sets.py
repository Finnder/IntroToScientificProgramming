# A Beady Problem
# By: Finnegan McGuire

"""
Sample Input (File small-beads.in):
3
4
1
2
5
6
9
10
8
7
"""
"""
Sample Input and Output:
1
Enter input file: small-beads.in
Enter bead sum k: 5
2 3
1 4
"""
debug = False

if debug:
    inputFile = 'small-beads.in'
else:
    inputFile = input("Enter input file: ")

beadsum = int(input("Enter bead sum k: "))

file = open(f'./lab06-materials/{inputFile}').read()

numbers = []
def BeadyProblem():
    for i in file:
        for j in file:
            if i != '\n' and j != '\n':
                if int(i) + int(j) == beadsum:
                    if int(i) != 0 and int(j) != 0:
                        numbers.append([int(i), int(j)])

    numbers.sort() # Sorts array
    
    # Remove Dups
    for z in numbers:
        for x in numbers:
            if z == x or z == x.reverse():
                numbers.remove(x)
    
    # Sort all arrays
    for h in range(len(numbers)):
        numbers[h].sort()
    
BeadyProblem()

for k in numbers:
    print(k[0], k[1])
