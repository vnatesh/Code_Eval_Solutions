"""

MULTIPLICATION TABLES

CHALLENGE DESCRIPTION:


Print out the grade school multiplication table upto 12*12.

INPUT SAMPLE:

There is no input for this program.

OUTPUT SAMPLE:

Print out the table in a matrix like fashion, each number formatted to a width of 4 (The numbers are right-aligned and strip out leading/trailing spaces on each line). The first 3 line will look like:

1   2   3   4   5   6   7   8   9  10  11  12
2   4   6   8  10  12  14  16  18  20  22  24
3   6   9  12  15  18  21  24  27  30  33  36

"""

list1=map(str,[i*j for i in range(1,13) for j in range(1,13)])
x=0
list2=[]
while x<len(list1):
    list2.append(list1[x:x+12])
    x+=12


for i in list2:
    i=[str(j).rjust(4) for j in i]
    print ''.join(i)                
