# ISBN Check
# By: Finnegan McGuire
# Status: Complete


# Checks to see if user entered only usable ISBN characters
def CheckInputOfUser(userInput):

    # Accepted ISBN characters
    validInputs = ['0', '1', '2', '3', '4', '5', '6', '7', '8' , '9', 'X']
    
    inputValid = False
    
    # Checks if users input has any invalid characters for the algorithm
    # using the any() function to check if any characters are invalid (another option would be to use a for loop)
    if any(x not in validInputs for x in userInput):
        inputValid = False
    else:
        inputValid = True
    
    # Returns if the input is valid or not (True or False)
    return inputValid

# Request User Input for ISBN Number
ISBN_number = input('Enter an ISBN number: ')

# Calculate if number is a valid ISBN number. (Returns -> True/False)
def ISBN_Checker(x):
     
    is_ISBN = False
   
    # Check input of the user, return false if user input contains any invalid characters
    if CheckInputOfUser(x) == False:
        return is_ISBN
    
    # If user input LENGTH is not 10 then number is not an ISBN number
    if len(x) != 10:
        return is_ISBN

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
        if number == 'X': # if number is X then make it -> (10)
            total += (10 * multiplyBy)
        else:
            total += (int(number) * multiplyBy)

        # reduce multiply value
        multiplyBy -= 1

    # Find remainder, if not 0 (0 -> meaning no remainder) then False
    if (total % 11) != 0:
        is_ISBN = False
    else:
        is_ISBN = True

    return is_ISBN


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
