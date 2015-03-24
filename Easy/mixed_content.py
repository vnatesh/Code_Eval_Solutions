"""
MIXED CONTENT

You have a string of words and digits divided by comma. Write a program which separates words with digits. You shouldn't change the order elements.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Input example is the following

8,33,21,0,16,50,37,0,melon,7,apricot,peach,pineapple,17,21
24,13,14,43,41

OUTPUT SAMPLE:

melon,apricot,peach,pineapple|8,33,21,0,16,50,37,0,7,17,21
24,13,14,43,41

As you cas see you need to output the same input string if it has words only or digits only.

"""

import sys,string
test_cases=open(sys.argv[1],'r')
for i in test_cases.read().split('\n'):
    if i!='':
        j=0
        list1=[]
        list2=[]
        line=i.split(',')
        while j<len(line):
            try: list1.append(int(line[j]))
            except ValueError:
                list2.append(line[j])
            j+=1
        if len(list1)>0 and len(list2)>0:
            print ','.join(list2)+'|'+','.join(map(str,list1))
        elif len(list1)==0 and len(list2)>0:
            print ','.join(list2)
        elif len(list1)>0 and len(list2)==0:
            print ','.join(map(str,list1))

