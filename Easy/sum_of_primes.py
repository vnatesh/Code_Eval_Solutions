"""
SUM OF PRIMES
CHALLENGE DESCRIPTION:

Write a program which determines the sum of the first 1000 prime numbers.

INPUT SAMPLE:

There is no input for this program.

OUTPUT SAMPLE:

Print to stdout the sum of the first 1000 prime numbers.

3682913

"""

import sys,math

def nth_prime(x):
    primes=[]
    n=1
    while len(primes)<=x:
        if all([n%j>0 for j in xrange(2,int(math.sqrt(n))+1)]):
            primes.append(n)
        n=n+1
    return primes


print sum(nth_prime(1000))-1

