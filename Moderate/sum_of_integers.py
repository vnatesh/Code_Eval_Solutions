"""
SUM OF INTEGERS
CHALLENGE DESCRIPTION:

Write a program to determine the largest sum of contiguous integers in a list.

INPUT SAMPLE:

The first argument is a path to a filename containing a comma-separated list of integers, one per line.

For example:

-10,2,3,-2,0,5,-15
2,3,-2,-1,10

OUTPUT SAMPLE:

Print to stdout the largest sum. In other words, of all the possible contiguous subarrays for a given array, find the one with the largest sum, and print that sum.

For example:

8
12

"""

import sys,math,itertools
test_cases=open(sys.argv[1],'r')
for i in test_cases.read().split('\n'):
    if i!='':
        a=map(int,i.split(','))
        line=[]
        for i in range(len(a)):
            for j in range(len(a)+1):
		if j>i:
                    line.append(sum(a[i:j]))
        print max(line)
