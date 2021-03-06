"""
SHORTEST REPETITION

CHALLENGE DESCRIPTION:


Write a program to determine the shortest repetition in a string. 
A string is said to have period p if it can be formed by concatenating one or more repetitions of another string of length p. For example, the string "xyzxyzxyzxyz" has period 3, since it is formed by 4 repetitions of the string "xyz". It also has periods 6 (two repetitions of "xyzxyz") and 12 (one repetition of "xyzxyzxyzxyz").

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Each line will contain a string of up to 80 non-blank characters. E.g.

abcabcabcabc
bcbcbcbcbcbcbcbcbcbcbcbcbcbc
dddddddddddddddddddd
adcdefg

OUTPUT SAMPLE:

Print out the smallest period of the input string. E.g.

3
2
1
7

"""

import sys
test_cases=open(sys.argv[1],'r')
for i in test_cases.read().split('\n'):
    if i!='':
        x=1
        solutionfound=False
        while not solutionfound:
            if set(i.split(i[:x]))==set(['']):
                    print len(i[:x])
                    solutionfound=True
            else: x+=1
        

            
            
