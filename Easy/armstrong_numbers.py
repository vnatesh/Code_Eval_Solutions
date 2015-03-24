"""

ARMSTRONG NUMBERS

CHALLENGE DESCRIPTION:


An Armstrong number is an n-digit number that is equal to the sum of the n'th powers of its digits. Determine if the input numbers are Armstrong numbers.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Each line in this file has a positive integer. E.g.

6
153
351

OUTPUT SAMPLE:

Print out True/False if the number is an Armstrong number or not. E.g.

True
True
False

"""

import sys
test_cases=open(sys.argv[1],'r')
for i in test_cases:
    q=[]
    if len(i)!=0:
        q.append(''.join(i.split('\n')))
    for i in q:
	w=[]
	for j in i:
		w.append(int(j)**len(i))
	if sum(w)==int(i): print True
	else: print False


