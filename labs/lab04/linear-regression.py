# Linear Regression
# By: Finnegan McGuire
# Status: Incomplete

import matplotlib.pyplot as plt

f = open("./lab04-materials/weather-data.txt", "r")

n = 71 # Points in data

# TODO:
# - Compute the slope
# - Compute the y intercept 
# - Then store in m and c
# - Print data

def CalculateSlope(X, Y, X_AVG, Y_AVG):
    numerator = 0
    denominator = 0

    for i in range(n):
        numerator += (X[i] - X_AVG) * (Y[i] - Y_AVG)
        denominator += (X[i] - X_AVG) ** 2

    slope = (numerator / denominator)
    return slope

def GetAverage(List):
    return sum(List) / len(List)

# Code to plot the graph
x = list()
y = list()

labels = list()
xbase = None

# Getting Data from file
for line in f:
    a,b = line.split()
    if xbase is None:
        xbase = float(a)
    x.append(float(a)-xbase)
    y.append(float(b))
    labels.append(int(a))

# Get Averages
xAvg = GetAverage(x)
yAvg = GetAverage(y)

f.close() # Close file

# Calculate 
m = CalculateSlope(x, y, xAvg, yAvg)
c = yAvg - (m * xAvg)

# Display Slope and Y intercept
print('The slope is ', m)
print('The y-intercept is ', c)

# Plot the data using plt
plt.plot(x, y, 'bo')

line = [m * x[i] + c for i in range(len(x))]
plt.plot(x, line, 'r')

# Add labels to dot chart
plt.xlabel("Year")
plt.ylabel("Temperature")

# Show data to user
plt.show()
