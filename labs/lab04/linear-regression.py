f = open("./lab04-materials/weather-data.txt", "r")

# TODO:
# - Compute the slope
# - Compute the y intercept 
# - Then store in m and c
# - Print data

def ComputeSlope(x1, y1, x2, y2):
    slope = (y2 - y1) / (x2 - x1)
    return slope

def ComputeYIntercept():
    pass

def GetAverage(List):
    return sum(List) / len(List)

# Code to plot the graph
x = list()
y = list()

x_average = GetAverage(x)
y_average = GetAverage(y)

# Gather Slope and Y intercept data
m = ComputeSlope()
c = ComputeYIntercept()

labels = list()

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
#line = [m * x[i] + c for i in range(len(x))]
#plt.plot(x, line, 'r')

plt.xlabel("Year")
plt.ylabel("Temperature")
plt.show()

print(x, y)
