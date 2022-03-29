# Chess
# By: Finnegan McGuire

from enum import Enum

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


def GetRow(rowSelection):
    return board[rowSelection][0:8]

def GetColumn(columnSelection):
    return board[0:8][columnSelection]

def CheckTheCheck():
    blackInCheck = False
    
    for row in board:
        for char in rows:
            if char == '.':
                pass

            if char == 'Q':
                pass





    return blackInCheck

print("ROW:", GetRow(0))
print("COLUMN:", GetColumn(0))

