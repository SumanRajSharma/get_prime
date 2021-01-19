'''
Seive of Eratosthenes
'''
import math
import sys

def getPrimes(limit):
    primes = [True] * (limit + 1)

    # ignore 0, 1 as prime number; loop starts with 2 and ends at sqrt(limit)
    for i in range(2, int(math.sqrt(limit))+1):
        if(primes[i] == True):
            # finds multiples of prime i and marks false as multiple of prime i is not a prime number; 
            # loop start from i*i, ends at <= limit and increments j+i
            for j in range(i**2, limit+1, +i):
                primes[j] = False

    return [i for i, number in enumerate(primes) if (number and i >= 2)]

if __name__ == '__main__': 
    try:
        result = getPrimes(int(sys.argv[1]))
        print('Total prime numbers between 2 and {}: {}'.format(sys.argv[1], len(result)))   
        print(result)
    except ValueError:
        print('Please input a valid integer')
    