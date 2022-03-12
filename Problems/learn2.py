import math

x = math.pi / 4
term = x
t = term 

for i in range(100000):
    term *= -1 * x * x
    term /= (2*i + 2) * (2*i + 3)
    t += term
    print(i, t)

print('My Guess', t)
print('math.sin ', math.sin(x))
