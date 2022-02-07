# Prime Factors 
# By: Finnegan McGuire
# Status: Incomplete

import math

# Calcualte the prime factors of the number given
def find_prime_factors(number):
    
    # Empty array to store all factorizations of 'number'
    prime_factorizations = []

    # Add the number to to the prime factorization array
    while number % 2 == 0:
        prime_factorizations.append(2)
        number = number / 2
    
    # Figure out the next prime factorizations
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        while number % i == 0:
            prime_factorizations.append(i)
            number = number / i
    
    if number > 2:
        prime_factorizations.append(number)

    return prime_factorizations

# Displays all info related to the prime number
def DisplayPrimeNumberInfo(number):

    # Call function to find the prime factors of 'user_number' 
    primeFactorizations = find_prime_factors(user_number)

    print("The set of prime factors are")
    
    # Display all factorizations of 'user_number'
    for factorizations in primeFactorizations:
        print(round(factorizations))

while True:
    # Get user input
    try:
        user_number = int(input('Enter a Number: '))
        break

    except ValueError:
        print('Please enter a number')



DisplayPrimeNumberInfo(round(user_number))

"""
Sample Input and Output:
Enter a number: 24
The set of prime factors are
2
2
2
3
"""
