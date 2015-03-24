"""
PREFIX EXPRESSIONS
CHALLENGE DESCRIPTION:

You are given a prefix expression. Write a program which evaluates it.

INPUT SAMPLE:

Your program should accept a file as its first argument. The file contains one prefix expression per line.

For example:

* + 2 3 4
Your program should read this file and insert it into any data structure you like. Traverse this data structure and evaluate the prefix expression. Each token is delimited by a whitespace. You may assume that sum ‘+’, multiplication ‘*’ and division ‘/’ are the only valid operators appearing in the test data.

OUTPUT SAMPLE:

Print to stdout the output of the prefix expression, one per line.

For example:

20

CONSTRAINTS:

The evaluation result will always be an integer ≥ 0.
The number of the test cases is ≤ 40.

"""

import sys,math,itertools,re
test_cases=open(sys.argv[1],'r')
for test in test_cases.read().split('\n'):
    if test!='':
        a=''.join(test.split(' '))
        x=map(int,re.findall(r'\d+',test))
        y=list(reversed(list(''.join(re.findall(r'\D+',a)))))
        for i in y:
            if i=='-':
                y.remove(i)
        if y[0]=='+': ans=float(x[0])+x[1]
        elif y[0]=='*': ans=float(x[0])*x[1]
        elif y[0]=='/': ans=float(x[0])/x[1]
        x.remove(x[0])
        x.remove(x[0])
        y.remove(y[0])
        i=0        
        while i<len(y):
            if y[i]=='+': ans+=float(x[i])
            elif y[i]=='*': ans*=float(x[i])
            elif y[i]=='/': ans=ans/float(x[i])
            i+=1
        print int(ans)





