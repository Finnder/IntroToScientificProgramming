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

inputFile = input("Enter input file: ")
beadsum = input("Enter bead sum k: ")

file = open(f'./lab06-materials/{inputFile}')

