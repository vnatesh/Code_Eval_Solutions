"""

AGE DISTRIBUTION
CHALLENGE DESCRIPTION:

You're responsible for providing a demographic report for your local school district based on age. To do this, you're going determine which 'category' each person fits into based on their age.
The person's age will determine which category they should be in:

If they're from 0 to 2 the child should be with parents print : 'Still in Mama's arms' 
If they're 3 or 4 and should be in preschool print : 'Preschool Maniac' 
If they're from 5 to 11 and should be in elementary school print : 'Elementary school' 
From 12 to 14: 'Middle school' 
From 15 to 18: 'High school' 
From 19 to 22: 'College'
From 23 to 65: 'Working for the man' 
From 66 to 100: 'The Golden Years' 
If the age of the person less than 0 or more than 100 - it might be an alien - print: "This program is for humans"

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Each line of input contains one integer - age of the person:

OUTPUT SAMPLE:

For each line of input print out where the person is:

Still in Mama's arms
College

"""


import sys,itertools
test_cases=open(sys.argv[1],'r')
for i in test_cases.read().split('\n'):
    if i!='':
        a=int(i)
        if a in xrange(0,3):
            print "Still in Mama's arms"
        elif a in xrange(3,5):
            print 'Preschool Maniac'
        elif a in xrange(5,12):
            print 'Elementary School'
        elif a in xrange(12,15):
            print 'Middle school'
        elif a in xrange(15,19):
            print 'High school'
        elif a in xrange(19,23):
            print 'College'
        elif a in xrange(23,66):
            print 'Working for the man'
        elif a in xrange(66,101):
            print 'The Golden Years'
        else: print 'This program is for humans'
