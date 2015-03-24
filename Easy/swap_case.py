"""
SWAP CASE

CHALLENGE DESCRIPTION:


Write a program which swaps letters' case in a sentence. All non-letter characters should remain the same.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Input example is the following

Hello world!
JavaScript language 1.8
A letter

OUTPUT SAMPLE:

Print results in the following way.

hELLO WORLD!
jAVAsCRIPT LANGUAGE 1.8
a LETTER

"""

import sys,string,math
test_cases=open(sys.argv[1],'r')
for i in test_cases.read().split('\n'):
    if i!='':
        q=[]
        for j in i:
            if j in string.uppercase:
                    q.append(j.lower())
            elif j in string.lowercase:
                    q.append(j.upper())
            else: q.append(j)
        print ''.join(q)
