# Calculating Pi
# By: Finnegan McGuire
# Status: Complete

import math

n = 100 # Iterations

# Calculate pi
def ContinuedFractions(iterations):
    numerator = 4
    numberToAdd = iterations * 2 - 1
    denominator = 1
    
    for i in range(iterations):
       denominator = numberToAdd + (((iterations - i)**2) / denominator)
       numberToAdd -= 2

    return 4 / denominator

continuedFractionsPi = ContinuedFractions(n)

# Output
print("Pi computed using continued fractions is", continuedFractionsPi)
print("Pi computed using math.pi is", math.pi);


"""
Pi computed using continued fractions is 3.141592653589793
Pi computed using math.pi is 3.141592653589793
"""
