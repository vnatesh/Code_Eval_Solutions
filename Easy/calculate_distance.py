"""
CALCULATE DISTANCE

CHALLENGE DESCRIPTION:


You have coordinates of 2 points and need to find the distance between them.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Input example is the following

(25, 4) (1, -6)
(47, 43) (-25, -11)
All numbers in input are integers between -100 and 100.

OUTPUT SAMPLE:

Print results in the following way.

26
90

You don't need to round the results you receive. They must be integer numbers.

"""

import sys,re,string,math
test_cases=open(sys.argv[1],'r')
for i in test_cases.read().split('\n'):
    if i!='':
        a=map(int,[j.translate(None,'(),') for j in re.findall(r'\(\-*\d+\,\s\-*\d+\)',''.join(i))][0].split(' '))
        b=map(int,[j.translate(None,'(),') for j in re.findall(r'\(\-*\d+\,\s\-*\d+\)',''.join(i))][1].split(' '))
        print int(math.sqrt(((a[0]-b[0])**2)+((a[1]-b[1])**2)))
        

