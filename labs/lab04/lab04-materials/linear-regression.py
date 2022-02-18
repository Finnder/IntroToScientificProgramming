f = open("weather-data.txt", "r")

# TODO: Find the slope m and the y-intercept of the regression line.


def FindSlope(data):
    x = []
    
    for i in data:
        print(i)

def FindYIntercept():
    pass




print ("The slope is " + str(m))
print ("The y-intercept is " + str(c))

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
