# Cycle Shift 
# By: Finnegan McGuire
# Status: Complete

# Shifts array over by a certain amount of times 
def ShiftArray(arr, shifts):

    newArr = [] # Define empty new array (will return)
    
    # Grab the last few indexes based on shifts and add them to new array
    i = shifts
    while i > 0:
        newArr.append(arr[-i])
        i -= 1
    
    # Add the rest of the numbers
    for i in range(len(arr) - shifts):
        newArr.append(arr[i])

    return newArr

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Define Array to reverse
array.sort() # Sort the given array
amountOfShift = 3 # Amount to shift the array by (right shift)

# Store return data from function
shiftedArray = ShiftArray(array, amountOfShift)

# OUTPUT
output = ""
for number in shiftedArray:
    output += str(number) # Add number to output
    output += " " # Space

print(output)

