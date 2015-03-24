"""

MATRIX ROTATION
CHALLENGE DESCRIPTION:

You are given a 2D N×N matrix. Each element of the matrix is a letter: from ‘a’ to ‘z’. Your task is to rotate the matrix 90° clockwise:

a b c        g d a
d e f  =>    h e b
g h i        i f c

INPUT SAMPLE:

The first argument is a file that contains 2D N×N matrices, presented in a serialized form (starting from the upper-left element), one matrix per line. The elements of a matrix are separated by spaces.
For example:

a b c d
a b c d e f g h i j k l m n o p
a b c d e f g h i

OUTPUT SAMPLE:

Print to stdout matrices rotated 90° clockwise in a serialized form (same as in the input sample).

For example:

c a d b
m i e a n j f b o k g c p l h d
g d a h e b i f c

CONSTRAINTS:

The N size of the matrix can be from 1 to 10
The number of test cases is 100

"""

import sys,math,itertools
test_cases=open(sys.argv[1],'r')
for i in test_cases.read().split('\n'):
    if i!='':
        a=i.split(' ')
        q=int(math.sqrt(len(a)))
        w=[x*q for x in range(1,q+1)]
        d=[x*q for x in range(0,q)]
        list1=[]
        for g in range(q):
            list1.append(a[d[g]:w[g]])
        list1=list(reversed(list1))
        print ' '.join(list(itertools.chain(*zip(*list1))))
