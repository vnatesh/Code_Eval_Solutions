"""

FOLLOWING INTEGER
CHALLENGE DESCRIPTION:

Credits: This challenge has appeared in a past google competition 

You are writing out a list of numbers.Your list contains all numbers with exactly Di digits in its decimal representation which are equal to i, for each i between 1 and 9, inclusive. You are writing them out in ascending order. For example, you might be writing every number with two '1's and one '5'. Your list would begin 115, 151, 511, 1015, 1051. Given N, the last number you wrote, compute what the next number in the list will be. The number of 1s, 2s, ..., 9s is fixed but the number of 0s is arbitrary.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Each line in this file is one test case. Each test case will contain an integer n < 10^6. E.g.

115
842
8000

OUTPUT SAMPLE:

For each line of input, generate a line of output which is the next integer in the list. E.g.

151
2048
80000

"""

import sys,string, itertools
test_cases=open(sys.argv[1],'r')
for test in test_cases.read().split('\n'):
    if test!='':
        ans=map(int,sorted(set(map(''.join,itertools.permutations(test,len(test))))))
        if max(ans)==int(test):
            blar=test+'0'
            ans=map(int,sorted(set(map(''.join,itertools.permutations(blar,len(blar))))))
            for i in ans:
                if i>int(test):
                    print str(i)
                    break
        else:
            print ans[ans.index(int(test))+1]


