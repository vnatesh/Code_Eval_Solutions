"""

DECIMAL TO BINARY
CHALLENGE DESCRIPTION:

You are given a decimal (base 10) number, print its binary representation.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename containing decimal numbers greater or equal to 0, one per line.

Ignore all empty lines.

For example:

2
10
67

OUTPUT SAMPLE:

Print the binary representation, one per line.

For example:

10
1010
1000011

"""

import sys,string
test_cases=open(sys.argv[1],'r')
for i in test_cases.read().split('\n'):
    if i!='':
        if len(i.split('.'))>1:
            a=bin(int(i.split('.')[0]))[2:]
            b=bin(int(i.split('.')[1]))[2:]
            print a+'.'+b
        else: print bin(int(i.split('.')[0]))[2:]
