"""

BIT POSITIONS
CHALLENGE DESCRIPTION:


Given a number n and two integers p1,p2 determine if the bits in position p1 and p2 are the same or not. Positions p1 and p2 are 1 based.

INPUT SAMPLE:

The first argument will be a path to a filename containing a comma separated list of 3 integers, one list per line. E.g.

86,2,3
125,1,2

OUTPUT SAMPLE:

Print to stdout, 'true'(lowercase) if the bits are the same, else 'false'(lowercase). E.g.

true
false

"""

import sys,string,re
test_cases=open(sys.argv[1],'r')
for i in test_cases.read().split('\n'):
    if i!='':
        a=map(int,i.split(','))
        if bin(a[0])[-a[1]]==bin(a[0])[-a[2]]:
            print 'true'
        else: print 'false'
        
        
