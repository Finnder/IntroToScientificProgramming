inpf = open("lab04-materials/book.txt", "r", encoding="utf8", errors="ignore")
outf = open("lab04-materials/utput.txt", "w", encoding="utf8", errors="ignore")

lower_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] 

outf.truncate(0) # Erase previous file contents

# 'avocado' -> is also 'dyrfdgr'
# 3 spaces forward for each character
# EX:
# a -> d (a, b, c, d)


# Returns -> String / Char
def IncrementCharacter(char):

    newChar = char
    amountToDecrease = 3
    check = False

    lowerCase = False
    upperCase = False
    # TODO: For some reason these if statements are always resulting to false, even when it should be true
    
    # Is character lowercase?
    for chars in lower_alphabet:
        if char == chars:
            lowerCase = True

    # Is character uppercase?
    for chars in upper_alphabet:
        if char == chars:
            upperCase = True

    if lowerCase == True:
        newCharIndex = lower_alphabet.index(char) - amountToDecrease
        newChar = lower_alphabet[newCharIndex]    
        check = True

    if upperCase == True:
        newCharIndex = upper_alphabet.index(char) - amountToDecrease
        newChar = upper_alphabet[newCharIndex]
        check = True
    
    return newChar

def ChangeCharacter(char):
    x = ord(char)
    y = chr(x)
    return y

# For every character in inpf file
for c in inpf.read():

    # Coverts unknown characters into normal characters
    z = ChangeCharacter(c) 

    # Increments letter by 3 and adds to output file
    output = IncrementCharacter(z)

    outf.write(output)

# Close files
outf.close()
inpf.close()
