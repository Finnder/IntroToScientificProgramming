# ISBN Check
# By: Finnegan McGuire
# Status: Complete

# Request User Input for ISBN Number
ISBN_number = input('Enter an ISBN number: ')

# Calculate if number is a valid ISBN number. (Returns -> True/False)
def ISBN_Checker(x):

    # Initialize Variables
    total = 0
    multiplyBy = 10 # Reduces by one for each iteration (expects 10 digits)
    
    # Numbers split in array
    numbers = []

    # For seperating all the numbers inputed into single digits
    for number in x:
        numbers.append(number)

    # For all the char/numbers in the numbers array
    for number in numbers:        
       
        # Multiply i and number then append that number
        if number == 'X': # if number is X (10)
            total += (10 * multiplyBy)
        else:
            total += (int(number) * multiplyBy)

        # reduce multiply value
        multiplyBy -= 1

    # Find remainder, if not 0 (meaning no remainder) then False
    if (total % 11) != 0:
        return False
    
    else:
        return True

# Gather ISBN Checker Value (returns -> boolean) and store in 'ISBN Status'
ISBN_Status = ISBN_Checker(ISBN_number)

# If ISBN_number is not a valid ISBN Number
if(ISBN_Status == False):
    print('Invalid ISBN number.')

else:
    print('ISBN number accepted.')

"""
Sample Input and Output:

Enter an ISBN number: 8180520781
ISBN number accepted.

Enter an ISBN number: 8180220781
Invalid ISBN number.
"""
