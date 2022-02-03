# Printing Pyramid
# By: Finnegan McGuire
# Status: Complete

"""
Sample Input and Output:
How many rows to print: 10
                *
               ***
              *****
             *******
            *********
           ***********
          *************
         ***************
        *****************
       *******************
"""


rows = int(input('How many rows to print: '))

# Creates and Displays Tree
def createTree(number):
    
    i = 0 # Current Iteration
    incrementRate = 1 # How many char are added to each side of center each iteration
    treeChar = '*' # What char prints on the tree

    while i <= number:
        
        # Steps:
        # 1. Add a space based on the amount of tree lines to create
        # 2. Backspace depending on i (increases by one each iteration)
        # 3. Add tree chars depedning on i to each side of tree center
        print((' '*number) + ('\b'*i) + ((treeChar * i) + treeChar + (treeChar * i)))

        # Increment
        i = i + incrementRate

# Call Function to create tree
createTree(rows)
