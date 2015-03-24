"""
LONGEST WORD

CHALLENGE DESCRIPTION:

In this challenge you need to find the longest word in a sentence. If the sentence has more than one word of the same length you should pick the first one.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Input example is the following

some line with text
another line
Each line has one or more words. Each word is separated by space char.

OUTPUT SAMPLE:

Print the longest word in the following way.

some
another

"""

import sys,string,math
test_cases=open(sys.argv[1],'r')
for i in test_cases.read().split('\n'):
    if i!='':
        q=max(map(len,i.split(' ')))
        for j in i.split(' '):
            if len(j)==q:
                print j
                break
