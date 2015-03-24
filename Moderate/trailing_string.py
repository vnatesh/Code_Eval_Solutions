"""

TRAILING STRING
CHALLENGE DESCRIPTION:


There are two strings: A and B. Print 1 if string B occurs at the end of string A. Otherwise, print 0.

INPUT SAMPLE:

The first argument is a path to the input filename containing two comma-delimited strings, one per line. Ignore all empty lines in the input file.

For example:

Hello World,World
Hello CodeEval,CodeEval
San Francisco,San Jose

OUTPUT SAMPLE:

Print 1 if the second string occurs at the end of the first string. Otherwise, print 0.

For example:

1
1
0

"""

import sys,string
test_cases=open(sys.argv[1],'r')
for i in test_cases.read().split('\n'):
    if i!='':
        a=i.split(',')
        if a[1] in a[0]:
            if a[1]==a[0][-len(a[1]):]:
                print 1
            else: print 0
        else: print 0
