"""

BEAUTIFUL STRINGS

CHALLENGE DESCRIPTION:


Credits: This problem appeared in the Facebook Hacker Cup 2013 Hackathon. 

When John was a little kid he didn't have much to do. There was no internet, no Facebook, and no programs to hack on. So he did the only thing he could... he evaluated the beauty of strings in a quest to discover the most beautiful string in the world. 

Given a string s, little Johnny defined the beauty of the string as the sum of the beauty of the letters in it. The beauty of each letter is an integer between 1 and 26, inclusive, and no two letters have the same beauty. Johnny doesn't care about whether letters are uppercase or lowercase, so that doesn't affect the beauty of a letter. (Uppercase 'F' is exactly as beautiful as lowercase 'f', for example.) 

You're a student writing a report on the youth of this famous hacker. You found the string that Johnny considered most beautiful. What is the maximum possible beauty of this string?

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Each line in this file has a sentence. E.g.

ABbCcc
Good luck in the Facebook Hacker Cup this year!
Ignore punctuation, please :)
Sometimes test cases are hard to make up.
So I just go consult Professor Dalves

OUTPUT SAMPLE:

Print out the maximum beauty for the string. E.g.

152
754
491
729
646

"""

import sys,string
test_cases=open(sys.argv[1],'r')
for i in test_cases.read().split('\n'):
    if i!='':
        m={}
        line=list(''.join(i.lower().split(' ')))
        q=[]
        for x in line:
            if x in string.ascii_letters:
		q.append(x)
        for j in set(q):
            m[j]=q.count(j)
        k=26
        a=0
        for y in list(reversed(sorted(m.values()))):
            a+=y*k
            k-=1
        print a
