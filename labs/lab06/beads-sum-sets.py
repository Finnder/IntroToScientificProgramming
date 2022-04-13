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
debug =  False

if debug:
    inputFile = 'small-beads.in'
else:
    inputFile = input("Enter input file: ")

beadsum = int(input("Enter bead sum k: "))

file = f'./lab06-materials/{inputFile}'

numbers = set()

with open(file, 'r') as file:
    for number in file:
        numbers.add(int(number))

    for i in numbers:
        bead = beadsum - i

        if bead in numbers:
            if i < bead:
                pass
            else:
                print(bead, i)
