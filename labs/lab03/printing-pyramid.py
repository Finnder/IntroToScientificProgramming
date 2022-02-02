# Printing Pyramid
# By: Finnegan McGuire
# Status: Incomplete

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
    
    i = 0
    incrementRate = 1
    
    treeChar = '*'

    while i <= number:
        
        # TODO: Works until we reach 10 then it needs more spaces before to backspace correctly

        # Display Tree Line
        print(('\t') + ('\b'*i) + ((treeChar * i) + treeChar + (treeChar * i)))

        # Increment
        i = i + incrementRate

createTree(rows)
