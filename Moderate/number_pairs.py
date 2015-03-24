"""

NUMBER PAIRS
CHALLENGE DESCRIPTION:


You are given a sorted array of positive integers and a number 'X'. Print out all pairs of numbers whose sum is equal to X. Print out only unique pairs and the pairs should be in ascending order

INPUT SAMPLE:

Your program should accept as its first argument a filename. This file will contain a comma separated list of sorted numbers and then the sum 'X', separated by semicolon. Ignore all empty lines. If no pair exists, print the string NULL e.g.

1,2,3,4,6;5
2,4,5,6,9,11,15;20
1,2,3,4;50

OUTPUT SAMPLE:

Print out the pairs of numbers that equal to the sum X. The pairs should themselves be printed in sorted order i.e the first number of each pair should be in ascending order. E.g.

1,4;2,3
5,15;9,11
NULL

"""

import sys,itertools
test_cases=open(sys.argv[1],'r')
for i in test_cases.read().split('\n'):
    if i!='':
        a=i.split(';')
        pairs=list(itertools.combinations(map(int,list(a[0].split(','))),2))
        prints=[]
        for j in pairs:
            if sum(j)==int(a[1]):
                prints.append([j[0],j[1]])
        if len(prints)==0: print('NULL')
        else: print(";".join(",".join(map(str,i)) for i in prints))
