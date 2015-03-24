"""

WORD TO DIGIT

CHALLENGE DESCRIPTION:


Having a string representation of a set of numbers you need to print this numbers.

All numbers are separated by semicolon. There are up to 20 numbers in one line. The numbers are "zero" to "nine"

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Each line in this file is one test case. E.g.

zero;two;five;seven;eight;four
three;seven;eight;nine;two
OUTPUT SAMPLE:

Print numbers in the following way:

025784
37892

"""

import sys,string,math
test_cases=open(sys.argv[1],'r')
for i in test_cases.read().split('\n'):
    if i!='':
        q=''
        for j in i.split(';'):
            if j.lower()=='zero':
		q+='0'
            elif j.lower()=='one':
                q+='1'
            elif j.lower()=='two':
                q+='2'
            elif j.lower()=='three':
                q+='3'
            elif j.lower()=='four':
                q+='4'
            elif j.lower()=='five':
                q+='5'
            elif j.lower()=='six':
                q+='6'
            elif j.lower()=='seven':
                q+='7'
            elif j.lower()=='eight':
                q+='8'
            elif j.lower()=='nine':
                q+='9'
        print q

