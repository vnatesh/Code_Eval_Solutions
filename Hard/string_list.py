"""
STRING LIST
CHALLENGE DESCRIPTION:

Credits: Challenge contributed by Max Demian. 

You are given a number N and a string S. Print all of the possible ways to write a string of length N from the characters in string S, comma delimited in alphabetical order.

INPUT SAMPLE:

The first argument will be the path to the input filename containing the test data. Each line in this file is a separate test case. Each line is in the format: N,S i.e. a positive integer, followed by a string (comma separated). E.g.

1,aa
2,ab
3,pop

OUTPUT SAMPLE:

Print all of the possible ways to write a string of length N from the characters in string S comma delimited in alphabetical order, with no duplicates. E.g.

a
aa,ab,ba,bb
ooo,oop,opo,opp,poo,pop,ppo,ppp

"""

import sys,string,itertools
test_cases=open(sys.argv[1],'r')
for i in test_cases.read().split('\n'):
    if i!='':
        a=i.split(',')[0]
        b=i.split(',')[1]
        print ','.join(map(''.join,itertools.product(''.join(sorted(set(b))),repeat=int(a))))
        

