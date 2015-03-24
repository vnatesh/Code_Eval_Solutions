"""
NUMBER OF ONES
CHALLENGE DESCRIPTION:

Write a program which determines the number of 1 bits in the internal representation of a given integer.

INPUT SAMPLE:

The first argument is a path to a file. The file contains integers, one per line.

For example:

10
22
56

OUTPUT SAMPLE:

Print to stdout the number of ones in the binary form of each number.

For example:

2
3
3

"""

import sys,string
test_cases=open(sys.argv[1],'r')
for i in test_cases.read().split('\n'):
    if i!='':
        print sum(map(int,bin(int(i))[2:]))





