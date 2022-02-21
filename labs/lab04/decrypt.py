inpf = open("lab04-materials/book.txt", "r", encoding="utf8", errors="ignore")
outf = open("lab04-materials/utput.txt", "w", encoding="utf8", errors="ignore")


lower_alphabet = string.ascii_lowercase # Gives all lowercase letters of the alphabet
upper_alphabet = string.ascii_uppercase # Gives all uppercase letters of the alphabet


# TODO: Decrypt the book
for c in inpf:
    output = []
    if c == any(lower_alphabet) or c == any(upper_alphabet):
        x = ord(c)
        y = chr(x)
        output.append(y)

print(output)

outf.close()
inpf.close()
