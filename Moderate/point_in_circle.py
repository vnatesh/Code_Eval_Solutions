"""
POINT IN CIRCLE
CHALLENGE DESCRIPTION:

Having coordinates of the center of a circle, it's radius and coordinates of a point you need to define whether this point is located inside of this circle.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Input example is the following

Center: (2.12, -3.48); Radius: 17.22; Point: (16.21, -5)
Center: (5.05, -11); Radius: 21.2; Point: (-31, -45)
Center: (-9.86, 1.95); Radius: 47.28; Point: (6.03, -6.42)
All numbers in input are between -100 and 100

OUTPUT SAMPLE:

Print results in the following way.

true
false
true

"""

import sys,math

def distance(x1,y1,x2,y2):
    return math.sqrt(((x2-x1)**2)+((y2-y1)**2))

def insideCircle(x1,y1,x2,y2,r):
    if distance(x1,y1,x2,y2)<r:
        return True
    else: return False

test_cases=open(sys.argv[1],'r')
for i in test_cases.read().split('\n'):
    if i!='':
        a=i.split(';')[0].strip()[9:-1]
        b=i.split(';')[1].strip()[8:]
        c=i.split(';')[2].strip()[8:-1]
        x1=float(a.split(',')[0].strip())
        y1=float(a.split(',')[1].strip())
        x2=float(c.split(',')[0].strip())
        y2=float(c.split(',')[1].strip())
        r=float(b.strip())
        if insideCircle(x1,y1,x2,y2,r)==True:
                 print 'true'
        else: print 'false'
