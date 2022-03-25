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

file = open("./lab05-materials/chess.txt","r")
file = file.read()

DefineRows() # Defines the rows
print(file)

isCheck = Check(rows) # check if king is in check

if isCheck:
    print("Black King is in check.")
else: 
    print("Black King is not in check.")
