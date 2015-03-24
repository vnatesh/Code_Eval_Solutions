"""

PASCALS TRIANGLE
CHALLENGE DESCRIPTION:


A Pascals triangle row is constructed by looking at the previous row and adding the numbers to its left and right to arrive at the new value. If either the number to its left/right is not present, substitute a zero in it's place. More details can be found here: Pascal's triangle. E.g. a Pascal's triangle upto a depth of 6 can be shown as:

            1
          1   1
        1   2   1
       1  3   3   1
     1  4   6   4   1
    1  5  10  10  5   1
INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Each line in this file contains a positive integer which indicates the depth of the triangle (1 based). E.g.

6

OUTPUT SAMPLE:

Print out the resulting pascal triangle upto the requested depth in row major form. E.g.

1 1 1 1 2 1 1 3 3 1 1 4 6 4 1 1 5 10 10 5 1

"""

import math

def combs(n, k):
    return int((math.factorial(n)) / ((math.factorial(k)) * math.factorial(n - k)))

def func(i):
    list1=[]
    for j in xrange(i):
        list2=[]
        for x in xrange(j+1):
            list2.append(combs(j,x))
        list1.append(list2)
    return list1
        

import sys,itertools
test_cases=open(sys.argv[1],'r')
for i in test_cases.read().split('\n'):
    if i!='':
        print ' '.join(map(str,sum(func(int(i)),[])))


        
