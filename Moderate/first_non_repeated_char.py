"""
FIRST NON-REPEATED CHARACTER
CHALLENGE DESCRIPTION:


Write a program which finds the first non-repeated character in a string.

INPUT SAMPLE:

The first argument is a path to a file. The file contains strings.

For example:

yellow
tooth

OUTPUT SAMPLE:

Print to stdout the first non-repeated character, one per line.

For example:

y
h

"""

import sys,re
test_cases=open(sys.argv[1],'r')
for i in test_cases.read().split('\n'):
    if i!='':
        list1=[]
        for j in i:
            if i.count(j)<2:
		list1.append(j)
        print str(list1[0])

        
    
        
