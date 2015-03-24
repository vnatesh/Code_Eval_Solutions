"""
SUDOKU
CHALLENGE DESCRIPTION:


Sudoku is a number-based logic puzzle. It typically comprises of a 9*9 grid with digits so that each column, each row and each of the nine 3*3 sub-grids that compose the grid contains all the digits from 1 to 9. For this challenge, you will be given an N*N grid populated with numbers from 1 through N and you have to determine if it is a valid sudoku solution. You may assume that N will be either 4 or 9. The grid can be divided into square regions of equal size, where the size of a region is equal to the square root of a side of the entire grid. Thus for a 9*9 grid there would be 9 regions of size 3*3 each.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Each line in this file contains the value of N, a semicolon and the sqaure matrix of integers in row major form, comma delimited. E.g.

4;1,4,2,3,2,3,1,4,4,2,3,1,3,1,4,2
4;2,1,3,2,3,2,1,4,1,4,2,3,2,3,4,1

OUTPUT SAMPLE:

Print out True/False if the grid is a valid sudoku layout. E.g.

True
False

"""

import sys
test_cases=open(sys.argv[1],'r')
for i in test_cases.read().split('\n'):
    if i!='':
        a=int(i.split(';')[0])
        b=i.split(';')[1].split(',')
        if a==4:
            b1=b[:len(b)/2]
            b2=b[len(b)/2:]
            list1=[b1,b2]
            row=set(map(str,xrange(1,a+1)))
            if all([set(j[0:2]+j[4:6])==set(j[2:4]+j[6:8])==row for j in list1]):
                print 'True'
            else: print 'False'
        elif a==9:
            b1=b[:len(b)/3]
            b2=b[len(b)/3:2*(len(b)/3)]
            b3=b[2*(len(b)/3):]
            list1=[b1,b2,b3]
            row=set(map(str,xrange(1,a+1)))                
            if all([set(j[0:3]+j[9:12]+j[18:21])==set(j[3:6]+j[12:15]+j[21:24])==set(j[6:9]+j[15:18]+j[24:])==row for j in list1]):
                print 'True'
            else: print 'False'
            
            

            
    
