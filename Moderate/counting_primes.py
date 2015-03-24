"""

COUNTING PRIMES
CHALLENGE DESCRIPTION:


Given two integers N and M, count the number of prime numbers between N and M (both inclusive)

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Each line in this file contains two comma separated positive integers. E.g.


2,10
20,30

OUTPUT SAMPLE:

Print out the number of primes between N and M (both inclusive)

4
2

"""

import sys,math
test_cases=open(sys.argv[1],'r')
for i in test_cases.read().split('\n'):
    if i!='':
        a=int(i.split(',')[0])
        b=int(i.split(',')[1])
        e=0
        if a==2: e+=1
        for j in xrange(a,b+1):
            if all([j%x>0 for x in xrange(2,int(math.sqrt(j))+2)]):
		e+=1
	print e
        
        
		
