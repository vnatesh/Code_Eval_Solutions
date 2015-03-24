"""
LETTERCASE PERCENTAGE RATIO


Your task is to write a program which determines (calculates) the percentage ratio of lowercase and uppercase letters.

INPUT SAMPLE:

Your program should accept a file as its first argument. Each line of input contains a string with uppercase and lowercase letters.

For example:

thisTHIS
AAbbCCDDEE
N
UkJ

OUTPUT SAMPLE:

For each line of input, print the percentage ratio of uppercase and lowercase letters rounded to the second digit after the point.

For example:


lowercase: 50.00 uppercase: 50.00
lowercase: 20.00 uppercase: 80.00
lowercase: 0.00 uppercase: 100.00
lowercase: 33.33 uppercase: 66.67

"""

import sys,string
test_cases=open(sys.argv[1],'r')
for i in test_cases.read().split('\n'):
    if i!='':
        upper=[]
        lower=[]
        for j in i:
            if j in string.lowercase:
                lower.append(j)
            elif j in string.uppercase:
                upper.append(j)
        percent_upper=round(100*len(upper)/float(len(upper)+len(lower)),2)
        percent_lower=round(100*len(lower)/float(len(upper)+len(lower)),2)
        a=str(percent_upper).split('.')
        if len(a[1])<2:
            x= a[0]+'.'+a[1]+('0'*(2-len(a[1])))
        else: x=a[0]+'.'+a[1]
        b=str(percent_lower).split('.')
        if len(b[1])<2:
            y= b[0]+'.'+b[1]+('0'*(2-len(b[1])))
        else: y=b[0]+'.'+b[1]
        print 'lowercase: '+y+' uppercase: '+x 
