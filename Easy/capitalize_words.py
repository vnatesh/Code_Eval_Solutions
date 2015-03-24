"""

CAPITALIZE WORDS

CHALLENGE DESCRIPTION:


Write a program which capitalizes the first letter of each word in a sentence.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Input example is the following

Hello world
javaScript language
a letter
1st thing

OUTPUT SAMPLE:

Print capitalized words in the following way.

Hello World
JavaScript Language
A Letter
1st Thing

"""

import sys,string
test_cases=open(sys.argv[1],'r')
for i in test_cases.read().split('\n'):
    if i!='':
        list1=[]
        line=i.split(' ')
        for j in line:
            if j[0] not in string.uppercase:
                list1.append(j[0].upper()+j[1:])
            else: list1.append(j)
        print ' '.join(list1)
