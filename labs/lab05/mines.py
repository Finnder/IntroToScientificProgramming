# Mines
# By: Finnegan McGuire

"""
........**...... ....1233**211.11
.....***...*...* ...12***322*212*
....*........*.. ...1*4421.112*21
.....*.......... ...12*1.....1121
...............* .122211..111112*
..**......*..*.. 12**2....1*22*21
.*.*.......*.... 1*4*2....12*211.
................ 22211.....123221
*...........**.* *211.......1**2*
..*............. 13*3111111113331
..**..*..*...*.. .2**12*32*211*1.
......**..*..... 123212**33*1111.
.*......*....... 1*111335*3111221
....*.*.*....**. 1111*2*3*2..1**2
...............* ...1121211..234*
.............*.. ............1*21

GRID: 16x16
"""
board = []
newBoard = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] #16x16 array
with open("./lab05-materials/mines.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    board += [[char for char in line.strip()]]

# Checks point 3x3 area
def CheckForBombs(row, column):
    numOfBombs = 0
    
    if board[row][column] == '*':
        return '*'

    try:
        if board[row][column - 1] == '*' and column - 1 >= 0:
            numOfBombs += 1

    except IndexError:
        pass

    try:
        if board[row][column + 1] == '*':
            numOfBombs += 1

    except IndexError:
        pass

    try:
        if board[row - 1][column - 1] == '*' and column >= 0:
            numOfBombs += 1

    except IndexError:
        pass
    try:
        if board[row - 1][column + 1] == '*':
            numOfBombs += 1

    except IndexError:
        pass

    try:
        if board[row - 1][column] == '*':
            numOfBombs += 1
    except IndexError:
        pass

    try:
        if board[row + 1][column] == '*':
            numOfBombs += 1
    except IndexError:
        pass
    try:
        if board[row + 1][column + 1] == '*':
            numOfBombs += 1
    except IndexError:
        pass
    try:
        if board[row + 1][column - 1] == '*' and column - 1 >= 0:
            numOfBombs += 1
    except IndexError:
        pass

    if numOfBombs == 0:
        return '.'

    return str(numOfBombs)

# CHECK BOMBS
for x in range(0, 16):
    for i in range(0, 16):
        newBoard[x].append(CheckForBombs(x, i))

# DISPLAY OUTPUT
for i in newBoard:
    line = ''.join(i)
    print(line)
