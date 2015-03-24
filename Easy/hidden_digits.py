"""

HIDDEN DIGITS

CHALLENGE DESCRIPTION:

In this challenge you're given a random string containing hidden and visible digits. The digits are hidden behind lower case latin letters as follows: 0 is behind 'a', 1 is behind ' b ' etc., 9 is behind 'j'. Any other symbol in the string means nothing and has to be ignored. So the challenge is to find all visible and hidden digits in the string and print them out in order of their appearance.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Each line in this file contains a string. You may assume that there will be no white spaces inside the string. E.g.

abcdefghik
Xa,}A#5N}{xOBwYBHIlH,#W
(ABW>'yy^'M{X-K}q,
6240488

OUTPUT SAMPLE:

For each test case print out all visible and hidden digits in order of their appearance. Print out NONE in case there is no digits in the string. E.g.

012345678
05
NONE
6240488

"""

import sys,string
test_cases=open(sys.argv[1],'r')
for i in test_cases.read().split('\n'):
    if i!='':
        list1=[]
        for j in i:
            if j=='a': list1.append('0')
            elif j=='b': list1.append('1')
            elif j=='c': list1.append('2')
            elif j=='d': list1.append('3')
            elif j=='e': list1.append('4')
            elif j=='f': list1.append('5')
            elif j=='g': list1.append('6')
            elif j=='h': list1.append('7')
            elif j=='i': list1.append('8')
            elif j=='j': list1.append('9')
            elif j in string.digits: list1.append(j)
        if len(list1)==0: print 'NONE'
        else: print ''.join(list1)
        
