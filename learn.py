import math

def f0(x, A):
    return x**2 - A

def f1(x):
    return x * 2
    

A = float(input('A:'))
x = 1

for i in range(100):
    x = x - f0(x, A)/f1(x)

print('guess', x)
print('sqrt', math.sqrt(A))
