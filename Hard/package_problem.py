"""
PACKAGE PROBLEM

CHALLENGE DESCRIPTION:


You want to send your friend a package with different things.
Each thing you put inside the package has such parameters as index number, weight and cost.
The package has a weight limit.
Your goal is to determine which things to put into the package so that the total weight is less than or equal to the package limit and the total cost is as large as possible.

You would prefer to send a package which weights less in case there is more than one package with the same price.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. The input file contains several lines. Each line is one test case.

Each line contains the weight that the package can take (before the colon) and the list of things you need to choose. Each thing is enclosed in parentheses where the 1st number is a thing's index number, the 2nd is its weight and the 3rd is its cost. E.g.

81 : (1,53.38,$45) (2,88.62,$98) (3,78.48,$3) (4,72.30,$76) (5,30
.18,$9) (6,46.34,$48)
8 : (1,15.3,$34)
75 : (1,85.31,$29) (2,14.55,$74) (3,3.98,$16) (4,26.24,$55) (5,63
.69,$52) (6,76.25,$75) (7,60.02,$74) (8,93.18,$35) (9,89.95,$78)
56 : (1,90.72,$13) (2,33.80,$40) (3,43.15,$10) (4,37.97,$16) (5,46
.81,$36) (6,48.77,$79) (7,81.80,$45) (8,19.36,$79) (9,6.76,$64)

OUTPUT SAMPLE:

For each set of things that you put into the package provide a list (items’ index numbers are separated by comma). E.g.

4
-
2,7
8,9

CONSTRAINTS:

Max weight that a package can take is ≤ 100
There might be up to 15 items you need to choose from
Max weight and cost of an item is ≤ 100

"""

def SumValue(x):
    list1=[]
    for i in x:
        list1.append(items[i][0])
    return sum(list1)


def SumWeight(x):
    list2=[]
    for i in x:
        list2.append(items[i][1])
    return sum(list2)


def MaxValue(w,v,i,aW,m):
    try: return m[(i,aW)]
    except KeyError:
        if i==0:
            if w[i]<=aW:
                m[(i,aW)]=[s[i]]
                return [s[i]]
            else:
                m[(i,aW)]=[]
                return []
        without_i=MaxValue(w,v,i-1,aW,m)
        if w[i]>aW:
            m[(i,aW)]=without_i
            return without_i
        else:
            with_i=[s[i]] + MaxValue(w,v,i-1,aW-w[i],m)
        if SumValue(with_i) > SumValue(without_i):
            ans=with_i
        elif SumValue(with_i) < SumValue(without_i): ans=without_i
        else:
            if SumWeight(with_i)<SumWeight(without_i): ans=with_i
            else: ans=without_i
        m[(i,aW)]=ans
        return sorted(ans)


import sys,string,itertools
test_cases=open(sys.argv[1],'r')
for test in test_cases.read().split('\n'):
    if test!='':
        memo={}
        aW=int(test.split(' : ')[0])
        a=test.split(' : ')[1].split(' ')
        
        weights=[]
        for x in a:
            weights.append(float(x[1:-1].split(',')[1]))

        values=[]
        for y in a:
            values.append(float(y[1:-1].split(',')[-1][1:]))

        index=len(weights)-1
        items={}
        for j in range(1,len(values)+1):
            items[j]=zip(values,weights)[j-1]
        s=items.keys()        

        
        output=MaxValue(weights,values,index,aW,memo)

        if output!=[]:
            print ','.join(map(str,output))
        else: print '-'

        



