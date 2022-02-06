# Prime Factors 
# By: Finnegan McGuire
# Status: Incomplete
import math

# Get user input
user_number = int(input('Enter a Number: '))

# Calcualte the prime factors of the number given
def find_prime_factors(number):

    prime_factorizations = []

    # Add the number to to the prime factorization array
    while number % 2 == 0:
        print(2)
        prime_factorizations.append(2)
        number = number / 2
    
    # 
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        
        while number % i == 0:
            print(i)
            number = number / i
    
    if number > 2:
        print(number)


find_prime_factors(user_number)

"""
Sample Input and Output:
Enter a number: 24
The set of prime factors are
2
2
2
3
"""
