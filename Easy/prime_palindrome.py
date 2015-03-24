import math
def ispalindrome(s):
    if len(s)<=1: return True
    else: return s[0]==s[-1] and ispalindrome(s[1:-1])


primes=[]
for j in range(1000):
    if all([j%factor>0 for factor in xrange(2,int(math.sqrt(j))+2)]):
        primes.append(j)
palins=[]
for i in map(str,primes):
    if ispalindrome(i): palins.append(i)
print max(map(int,palins))
