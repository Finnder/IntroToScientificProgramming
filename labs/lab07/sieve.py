n = input()

numbers = []

primesTxt = open('./primes.txt', 'w')
primesTxt.truncate()

p = 2

for i in range(0, int(n) + 1):
    numbers += [i]

    if i == 0 or i == 1:
        numbers[i] = '_'

while True:
    for j in range(p * 2, len(numbers), p):
        numbers[j] = '_'

    for h in range(p + 1, len(numbers)):
        if h != '_':
            p = h
            break
    else:
        break

for g in numbers:
    if g != '_':
        primesTxt.write(str(g) + '\n')

primesTxt.close()
