"""

SIMPLE SORTING

CHALLENGE DESCRIPTION:

Write a program which sorts numbers.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Input example is the following

70.920 -38.797 14.354 99.323 90.374 7.581
-37.507 -3.263 40.079 27.999 65.213 -55.552

OUTPUT SAMPLE:

Print sorted numbers in the following way. Please note, that you need to print the numbers till the 3rd digit after the dot including trailing zeros.

-38.797 7.581 14.354 70.920 90.374 99.323
-55.552 -37.507 -3.263 27.999 40.079 65.213

"""

import sys
test_cases=open(sys.argv[1],'r')
for i in test_cases.read().split('\n'):
    if i!='':
        line=map(str,sorted(map(float,i.split(' '))))
        for x,y in enumerate(line):
            if len(y.split('.')[1])<3:
		line[x]+=(3-len(y.split('.')[1]))*'0'
        print ' '.join(line)
