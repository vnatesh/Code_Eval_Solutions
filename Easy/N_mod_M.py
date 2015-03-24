"""

N MOD M
CHALLENGE DESCRIPTION:


Given two integers N and M, calculate N Mod M (without using any inbuilt modulus operator).

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Each line in this file contains two comma separated positive integers. E.g

20,6
2,3

You may assume M will never be zero.

OUTPUT SAMPLE:

Print out the value of N Mod M

"""

import sys,string,math
test_cases=open(sys.argv[1],'r')
for i in test_cases.read().split('\n'):
    if i!='':
        line=map(int,i.split(','))
        print str(line[0]-line[1]*(line[0]/line[1]))




