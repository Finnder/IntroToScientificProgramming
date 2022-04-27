"""
Sample Input and Output:
Enter a binary string: 10101001101011
The hex value of the string is 2a6b
"""

binString = input('Enter a binary string: ')

lenOfString = len(binString)
pairs = lenOfString / 4

for i in range(pairs):
    currentBin = binString[0:4]
    print(currentBin + " -> " + ConvertToHex(currentBin))

    
