"""
STRING PERMUTATIONS

CHALLENGE DESCRIPTION:

Write a program which prints all the permutations of a string in alphabetical order. We consider that digits < upper case letters < lower case letters. The sorting should be performed in ascending order.

INPUT SAMPLE:

Your program should accept a file as its first argument. The file contains input strings, one per line.

For example:

hat
abc
Zu6

OUTPUT SAMPLE:

Print to stdout the permutations of the string separated by comma, in alphabetical order.

For example:

aht,ath,hat,hta,tah,tha
abc,acb,bac,bca,cab,cba
6Zu,6uZ,Z6u,Zu6,u6Z,uZ6

"""

# Print all permutations of a string (do this for many strings where each string is a line)
import sys, itertools
test_cases=open(sys.argv[1],'r')
for i in test_cases.read().split('\n'):
    a=map(''.join,sorted(list(itertools.permutations(i))))
    print ','.join(a)
