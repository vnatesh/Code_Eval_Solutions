
#------------------------- CREATED BY VIKAS NATESH

# This program is a greedy optimization for recreating a master string of characters from a list of overlapping substrings of the master string. 


import sys,string,itertools,difflib,time
start=time.time()

def side1(s):                                       # Find all substrings from one side (eg. s='ABCDE' and side1(s) = set(['BCDE', 'CDE', 'DE', 'ABCDE', 'E']) )
    return set([s[i:] for i in xrange(len(s))])

def side2(s):                                       # Find all substrings from the other side (eg. s='ABCDE' and side2(s) = set(['', 'A', 'AB', 'ABCD', 'ABC']) )
    return set([s[:i] for i in xrange(len(s))])     # The side functions are defined such that returned substrings are only those at the end (side1) or beginning (side2) of the input string


def overlap(a,b):
    if b in a: return b                     
    elif a in b: return a                    # In the trivial cases where b is in a or a is in b, return either b or a respectively
    q = side1(a) & side2(b)                   
    r = side1(b) & side2(a)                  # Create two sets of common overlaps from either side. This satisfies the condition that overlaps must occur at the start or end
    if q|r == set([]):                       # If the union of the two sets is empty, there are no overlaps so return ''
        return ''
    else: return max(q|r , key=len)           # If there are overlaps, return the longest one


def merge(a,b):    
    if overlap(a,b) == overlap(b,a) == '':  
            return ''
    elif a in b: return b
    elif b in a: return a                 

    q=len(overlap(a,b))
    if overlap(a,b) == a[:q] == b[-q:]: return b+a[q:]
    elif overlap(a,b) == a[-q:] == b[:q]: return a+b[q:] 



test_cases=open(sys.argv[1],'r')
for test in test_cases.read().split('\n'):
    line = [j for j in string.split(''.join(test),';')]
    q=line[0]
    while len(line)!=0:
        pairs=[(q,seq) for seq in line]
        matches=[overlap(y[0],y[1]) for y in pairs]
        best_match = max(matches,key=len)
        index = matches.index(best_match)
        x = pairs[index]
        q=merge(x[0],x[1])
        line=set(line)-set(x)
    print q



print time.time()-start

##            
        

###------------------------------BONUS------------------------------------
##
### If you have a list of strings ['atgc','gcat','attgc'], they can merge on the first
### operation as ['atgcat','attgc'], ['gcattgc','atgc' ] or ['gcatgc','attgc'] and can
### merge on the second operation as ['atgcattgc'] or ['attgcatgc'], yielding two different
### possible final reconstructions
##
##
