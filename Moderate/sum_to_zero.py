"""
SUM TO ZERO
CHALLENGE DESCRIPTION:


You are given an array of integers. Count the numbers of ways in which the sum of 4 elements in this array results in zero.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Each line in this file consist of comma separated positive and negative integers. E.g.

2,3,1,0,-4,-1
0,-1,3,-2

OUTPUT SAMPLE:

Print out the count of the different number of ways that 4 elements sum to zero. E.g.

2
1

"""

import sys,itertools
test_cases=open(sys.argv[1],'r')
for i in test_cases.read().split('\n'):
    if i!='':
        a=map(sum,list(itertools.combinations(map(int,i.split(',')),4)))
        print a.count(0)
        


    

