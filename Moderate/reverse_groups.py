"""

REVERSE GROUPS

CHALLENGE DESCRIPTION:


Given a list of numbers and a positive integer k, reverse the elements of the list, k items at a time. If the number of elements is not a multiple of k, then the remaining items in the end should be left as is.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Each line in this file contains a list of numbers and the number k, separated by a semicolon. The list of numbers are comma delimited. E.g.

1,2,3,4,5;2
1,2,3,4,5;3

OUTPUT SAMPLE:

Print out the new comma separated list of numbers obtained after reversing. E.g.

2,1,4,3,5
3,2,1,4,5

"""

import sys,math
test_cases=open(sys.argv[1],'r')
for i in test_cases.read().split('\n'):
    if i!='':
        a=int(i.split(';')[1])
        b=i.split(';')[0].split(',')
        x=0
        s=[]
        while x<len(b):
            if len(list(reversed(b[x:x+a])))==a:
                s.append(','.join(reversed(b[x:x+a])))
            else: s.append(','.join(b[x:x+a]))
            x+=a
        print ','.join(s)




