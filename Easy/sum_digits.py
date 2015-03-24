"""

SUM OF DIGITS
CHALLENGE DESCRIPTION:


Given a positive integer, find the sum of its constituent digits.

INPUT SAMPLE:

The first argument will be a path to a filename containing positive integers, one per line. E.g.

23
496

OUTPUT SAMPLE:

Print to stdout, the sum of the numbers that make up the integer, one per line. E.g.

5
19

"""

import sys,string
test_cases=open(sys.argv[1],'r')
for i in test_cases.read().split('\n'):
    if i!='':
        r=0
        for j in i:
            r+=int(j)
        print r

