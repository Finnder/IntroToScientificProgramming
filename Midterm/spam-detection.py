# Spam Detection
# By: Finnegan McGuire
# Status: Complete

"""
Sample Input and Output:
Enter text: Welcome CS2435 Coders!!
Whitespace ratio = 0.08695652
Lowercase ratio = 0.47826087
Uppercase ratio = 0.17391304
Symbols ratio = 0.26086957
"""

# Get user input to compute later
userInput = input("Enter text: ")

# Ratios for each character
whitespaceRatio = 0
lowercaseRatio = 0
uppercaseRatio = 0
symbolsRatio = 0

# Calculated the word
def CalculateWord(word):
   
    # Referencing Globals
    global whitespaceRatio
    global lowercaseRatio
    global uppercaseRatio
    global symbolsRatio

    # Initializing Variables
    whitespaceChars = 0
    lowercaseChars = 0
    uppercaseChars = 0 
    symbolChars = 0
    
    # Calculate characters in word
    for i in word:
        if i.islower():
            lowercaseChars += 1
        elif i.isupper():
            uppercaseChars += 1
        elif i == ' ' or i == '\n' or i == '\t':
            whitespaceChars += 1
        else: 
            symbolChars += 1
    
    # Calculate ratios of each character
    whitespaceRatio = whitespaceChars / len(word)
    uppercaseRatio = uppercaseChars / len(word)
    lowercaseRatio = lowercaseChars / len(word)
    symbolsRatio = symbolChars / len(word) 

CalculateWord(userInput)

# Output
print(f"""
Whitespace ratio = {whitespaceRatio}
Lowercase ratio = {lowercaseRatio}
Uppercase ratio = {uppercaseRatio}
Symbols ratio = {symbolsRatio}
""")
