f = open("./lab04-materials/weather-data.txt", "r")

# TODO: Find the slope m and the y-intercept of the regression line.


def ReformatPoint(x, y):
    # Covert to int and float to use math on it 
    x = int(x)
    y = float(y)
    new_x = x - 1929
    point = [new_x, y]
    return point 

for points in f:
    x = points.split()[0]
    y = points.split()[1]

    print(ReformatPoint(x, y))


"""
# Code to plot the graph
f = open("weather-data.txt", "r")
x = list()
y = list()
xlabels = list()

xbase = None
for line in f:
    a,b = line.split()
    if xbase is None:
        xbase = float(a)
    x.append(float(a)-xbase)
    y.append(float(b))
    xlabels.append(int(a))
f.close()

import matplotlib.pyplot as plt
plt.plot(x, y, 'bo')
line = [m * x[i] + c for i in range(len(x))]
plt.plot(x, line, 'r')

plt.xlabel("Year")
plt.ylabel("Temperature")
plt.show()
"""
