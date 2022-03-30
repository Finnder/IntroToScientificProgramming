# Chess
# By: Finnegan McGuire

# NOTE: Sample is Incorrect? -> Chess board has 8 vertical & horizontal rows (sample has only 7)
"""
Sample Input:
Q..kb.r 
p..n.ppp
....q...
....p.B.
........
PPP..PPP
..KR....

Output: 
Black is in check
"""

board = []

# Open file
with open("./lab05-materials/chess.txt","r") as file:
    lines = file.readlines() # Store lines

# Append board array with board
for line in lines:
    board += [[char for char in line.strip()]]

def kingAttack(y, x):
    for i in range(3):
        for j in range(3):
            try:
                if board[y + i - 1][x + j - 1] == 'k' and y + i - 1 >= 0 and x + j - 1 >= 0:
                    return True
            except IndexError:
                pass

def knightAttack(y, x):

    for l in [2, -2]: # Check Y
        for s in [1, -1]: # Check Left and Right
            try:
                if y + l >= 0 and x + s >= 0:
                    if board[y+l][x+s] == 'k':
                        return True
            except IndexError:
                pass

            try:
                if y + s >= 0 and x + l >= 0:
                    if board[y+s][x+l] == 'k':
                        return True
            except IndexError:
                pass

def queenAttack(y, x):
    if rookAttack(y, x) or bishopAttack(y, x):
        return True

def rookAttack(y, x):
    
    # CHECK RIGHT
    for i in range(y + 1, 8):
        if board[i][x] == '.':
            continue
        if board[i][x] == 'k':
            return True
        else:
            break
    
    # CHECK LEFT
    for i in range(y - 1, -1, -1):
        if board[i][x] == '.':
            continue
        if board[i][x] == 'k':
            return True
        else:
            break

    # CHECK UP
    for i in range(x + 1, 8):
        if board[y][i] == '.':
            continue
        if board[y][i] == 'k':
            return True
        else:
            break

    # CHECK DOWN
    for i in range(x - 1, -1, -1):
        if board[y][i] == '.':
            continue
        if board[y][i] == 'k':
            return True
        else:
            break

def bishopAttack(y, x):
    
    # Check up right diagonal
    try:
        for i in range(1, 8):
            if board[y + i][x + i] == '.':
                continue
            if board[y + i][x + i] == 'k':
                return True
            else:
                break
    except IndexError:
        pass

    # Check up left diagonal
    try:
        for i in range(1, 8):
            if x - i >= 0:
                if board[y + i][x - i] == '.':
                    continue
                if board[y + i][x - i] == 'k':
                    return True
                else:
                    break
    except IndexError:
        pass

    # Check down right diagonal
    try:
        for i in range(1, 8):

            if y - i >= 0:
                if board[y - i][x + i] == '.':
                    continue
                if board[y - i][x + i] == 'k':
                    return True
                else:
                    break
    except IndexError:
        pass

    # Check down left diagonal
    try:
        for i in range(1, 8):
            if y - i >= 0 and x - i >= 0:
                if board[y - i][x - i] == '.':
                    continue
                if board[y - i][x - i] == 'k':
                    return True
                else:
                    break
    except IndexError:
        pass

def pawnAttack(y, x):
    try:
        sqR = board[y - 1][x + 1]
    except IndexError:
        sqR = 10

    try:
        if x - 1 >= 0:
            sqL = board[y - 1][x - 1] 
        else:
            sqL = 10
    except IndexError:
        sqL = 10

    if sqL == 'k' or sqR == 'k':
        return True

def CheckTheCheck():
    blackInCheck = False
 
    for y, row in enumerate(board):
        for x, val in enumerate(row):

            if val == "R": # Rook
                blackInCheck = rookAttack(y, x)   
            if val == "Q": # Queen
                blackInCheck = queenAttack(y, x)
            if val == "B": # Bishop
                blackInCheck = bishopAttack(y, x)
            if val == "P": # Pawn
                blackInCheck = pawnAttack(y, x)
            if val == "K": # King
                blackInCheck = kingAttack(y, x)
            if val == "N": # Knight
                blackInCheck = knightAttack(y, x)

            if blackInCheck:
                return True
    
    return blackInCheck

if CheckTheCheck():
    print("Black king is in check.")
else:
    print("Black king is not in check.")
