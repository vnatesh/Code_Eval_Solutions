"""

LOWERCASE
CHALLENGE DESCRIPTION:


Given a string write a program to convert it into lowercase.

INPUT SAMPLE:

The first argument will be a path to a filename containing sentences, one per line. You can assume all characters are from the english language. E.g.

HELLO CODEEVAL
This is some text

OUTPUT SAMPLE:

Print to stdout, the lowercase version of the sentence, each on a new line. E.g.

hello codeeval
this is some text

"""

#Convert Strings to Lower Case
import sys,string

test_cases=open(sys.argv[1],'r')
for i in test_cases.read().split('\n'):
    if i!='':
        print i.lower()

test_cases.close()
