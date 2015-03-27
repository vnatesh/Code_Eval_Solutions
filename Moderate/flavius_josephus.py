"""
Flavius Josephus was a famous Jewish historian of the first century, at the time of the destruction of the Second Temple. According to legend, during the Jewish-Roman war he was trapped in a cave with a group of soldiers surrounded by Romans. Preferring death to capture, the Jews decided to form a circle and, proceeding around it, to kill every j'th person remaining until no one was left. Josephus found the safe spot in the circle and thus stayed alive. 
Write a program that returns a list of n people, numbered from 0 to n-1, in the order in which they are executed.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Each line in this file contains two comma separated positive integers n and m, where n is the number of people and every m'th person will be executed. E.g.

10,3
5,2

OUTPUT SAMPLE:

Print out the list of n people (space delimited) in the order in which they will be executed. E.g.

2 5 8 1 6 0 7 4 9 3
1 3 0 4 2

"""

import sys,itertools,math
test_cases=open(sys.argv[1],'r')
for i in test_cases.read().split('\n'):
    if i!='':
        a=map(int,i.split(','))[0]
        b=map(int,i.split(','))[1]
        q=range(a)
        j=-1
        list1=[]
        while len(list1)!=a:
            while j<len(q):
                try:
                        list1.append(q[j+b])
                        j+=b
                except IndexError: break
            s=[x for x in range(a) if x not in list1]
            q=q+s
        print ' '.join(map(str,list1))


