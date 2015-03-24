"""
DELTA TIME
CHALLENGE DESCRIPTION:

You are given the pairs of time values. The values are in the HH:MM:SS format with leading zeros. Your task is to find out the time difference between the pairs.

INPUT SAMPLE:

The first argument is a file that contains lines with the time pairs.

For example:

14:01:57 12:47:11
13:09:42 22:16:15
08:08:06 08:38:28
23:35:07 02:49:59
14:31:45 14:46:56

OUTPUT SAMPLE:

Print to stdout the time difference for each pair, one per line. You must format the time values in HH:MM:SS with leading zeros.

For example:

01:14:46
09:06:33
00:30:22
20:45:08
00:15:11

"""


import sys,datetime
test_cases=open(sys.argv[1],'r')
for i in test_cases.read().split('\n'):
    if i!='':
        a=map(int,i.split(' ')[0].split(':'))
        b=map(int,i.split(' ')[1].split(':'))
        c=(datetime.timedelta(seconds=a[2],minutes=a[1],hours=a[0])-datetime.timedelta(seconds=b[2],minutes=b[1],hours=b[0])).__str__()
        if '-' in c:
            c=(datetime.timedelta(seconds=b[2],minutes=b[1],hours=b[0])-datetime.timedelta(seconds=a[2],minutes=a[1],hours=a[0])).__str__()
            if len(c)<8: c='0'+c
        elif len(c)<8:
            c='0'+c
        print c
