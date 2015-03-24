"""
MINIMUM COINS
CHALLENGE DESCRIPTION:


You are given 3 coins of value 1, 3 and 5. You are also given a total which you have to arrive at. Find the minimum number of coins to arrive at it.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Each line in this file contains a positive integer number which represents the total you have to arrive at. E.g.

11
20

OUTPUT SAMPLE:

Print out the minimum number of coins required to arrive at the total. E.g.

3
4

"""

import sys,math
test_cases=open(sys.argv[1],'r')
for i in test_cases.read().split('\n'):
    if i!='':
        list1=[]
        coins=[5,3,1]
        i=float(i)

        j=0
        while j<len(coins):
            if i/coins[j]==int(i)/coins[j]:
                list1.append(int(i)/coins[j])
                break
            elif i/coins[j]>int(i)/coins[j]>=1:
                list1.append(int(i)/coins[j])
                i=i%coins[j]
                j+=1
            elif i/coins[j]>int(i)/coins[j]==0:
                list1.append(0)
                i=i%coins[j]
                j+=1
        print sum(list1)
        
        
        
