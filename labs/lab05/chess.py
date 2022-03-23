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

# Classify What is on board (enums are ways to declare new data types)
class Piece(Enum):
    WHITE_PAWN = "P"
    WHITE_KNIGHT = "N"
    WHITE_BISHOP = "B"
    WHITE_ROOK = "R"
    WHITE_QUEEN = "Q"
    WHITE_KING = "K"

    BLACK_PAWN = "p"
    BLACK_KNIGHT = "n"
    BLACK_BISHOP = "b"
    BLACK_ROOK = "r"
    BLACK_QUEEN = "q"
    BLACK_KING = "k"

file = open("./lab05-materials/chess.txt","r")
file = file.read()

rows = [[], [], [], [], [], [], [], []] # Chess board array, 8 horizontal & vertical rows/columns

def DefineRows():
    currentRow = 0
    while currentRow < 8:

        # Add to row
        rows[currentRow].append(file[(0 + (currentRow * 9)):(8 + (currentRow * 9))])
        currentRow += 1 # Change row number

def Check(board):
    blackInCheck = False

    for i in range(len(rows)): # For every row in rows
        for x in range(len(rows[i])): # For every char in rows[i] (current row)
            currentSpot = rows[i][x]

            if currentSpot == Piece.WHITE_PAWN or Piece.BLACK_PAWN:
                # Check the row above and see if king is in range
                try:
                    if rows[i - 1][2] == Piece.BLACK_KING and currentSpot == Piece.WHITE_PAWN:
                        blackInCheck = True

                    if rows[i - 1][4] == Piece.BLACK_KING and currentSpot == Piece.WHITE_PAWN:
                        blackInCheck = True

                except IndexError:
                    # If no row above / below do nothing
                    pass

            if currentSpot == Piece.WHITE_KNIGHT or currentSpot == Piece.BLACK_KNIGHT:
                # Check 1/2 rows above and 1/2 rows below 

                try:
                    # Check row 1 above and 2 above
                    if rows[i - 1][1] == Piece.BLACK_KING and currentSpot == Piece.WHITE_KNIGHT:
                        blackInCheck = True

                    if rows[i - 1][5] == Piece.BLACK_KING and currentSpot == Piece.WHITE_KNIGHT:
                        blackInCheck = True

                    if rows[i - 2][2] == Piece.BLACK_KING and currentSpot == Piece.WHITE_KNIGHT:
                        blackInCheck = True

                    if rows[i - 2][4] == Piece.BLACK_KING and currentSpot == Piece.WHITE_KNIGHT:
                        blackInCheck = True
                except IndexError:
                    # If no row above / below do nothing
                    pass                   

                try:
                    # Check row 1 below and 2 below
                    if rows[i + 1][1] == Piece.BLACK_KING and currentSpot == Piece.WHITE_KNIGHT:
                        blackInCheck = True

                    if rows[i + 1][5] == Piece.BLACK_KING and currentSpot == Piece.WHITE_KNIGHT:
                        blackInCheck = True

                    if rows[i + 2][2] == Piece.BLACK_KING and currentSpot == Piece.WHITE_KNIGHT:
                        blackInCheck = True

                    if rows[i + 2][4] == Piece.BLACK_KING and currentSpot == Piece.WHITE_KNIGHT:
                        blackInCheck = True
                except IndexError:
                    # If no row above / below do nothing
                    pass
                
            if currentSpot == Piece.BLACK_BISHOP or currentSpot == Piece.BLACK_BISHOP:
                # Check all rows in a diagonal way
                pass

            if currentSpot == Piece.WHITE_ROOK or currentSpot == Piece.BLACK_ROOK:
                # Check all rows strait up and left and right
                pass

            if currentSpot == Piece.WHITE_QUEEN or currentSpot == Piece.BLACK_QUEEN:
                # Check all rows diagonal up, down, left, right, diagonal
                if rows[i-1]
                pass

            if currentSpot == Piece.WHITE_KING or currentSpot == Piece.BLACK_KING:
                # Check all squares around 
                pass

    return blackInCheck

DefineRows() # Defines the rows
print(file)

isCheck = Check(rows) # check if king is in check

if isCheck:
    print("Black King is in check.")
else: 
    print("Black King is not in check.")
