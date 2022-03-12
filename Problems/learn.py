import math

def f0(x, A):
    return x**2 - A

def f1(x):
    return x * 2
    

A = float(input('A:'))
x = 1
i = 0

while True:
    print(i, x)
    i += 1
    p = x
    x = x - (x**2 - A)/(2 * x)
    if abs(p - x) < 0.00001:
        break

print('guess', x)
print('sqrt', math.sqrt(A))
