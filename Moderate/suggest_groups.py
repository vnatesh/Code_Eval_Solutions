"""
SUGGEST GROUPS
CHALLENGE DESCRIPTION:

You may have noticed that a new feature was added to our web site – user groups. So, this challenge is about joining groups.

You are given a list of users of a social network, friends of each user, and groups the user participates in.

To help users find the most interesting groups, we suggest them joining the groups where ≥50% of their friends participate.

Your task is to write a program which finds a list of suggested groups for each user.

INPUT SAMPLE:

The first argument is a file that contains the information about each user, one user per line. The line is delimited by colon ‘:’ into three parts: user name, list of friends, and list of groups. The items in each part are delimited by comma ‘,’.

For example:

Amira:Isaura,Lizzie,Madalyn,Margarito,Shakira,Un:Driving,Mineral 
collecting
Elliot:Isaura,Madalyn,Margarito,Shakira:Juggling,Mineral 
collecting
Isaura:Amira,Elliot,Lizzie,Margarito,Verla,Wilford:Juggling
Lizzie:Amira,Isaura,Verla:Driving,Mineral collecting,Rugby
Madalyn:Amira,Elliot,Margarito,Verla:Driving,Mineral collecting
,Rugby
Margarito:Amira,Elliot,Isaura,Madalyn,Un,Verla:Mineral collecting
Shakira:Amira,Elliot,Verla,Wilford:Mineral collecting
Un:Amira,Margarito,Wilford:
Verla:Isaura,Lizzie,Madalyn,Margarito,Shakira:Driving,Juggling
,Mineral collecting
Wilford:Isaura,Shakira,Un:Driving


OUTPUT SAMPLE:

Print to stdout the list of suggested groups for each user. The list of users and the list of groups for each user must be sorted alphabetically.

For example:

Isaura:Driving,Mineral collecting
Lizzie:Juggling
Madalyn:Juggling
Margarito:Driving,Juggling
Shakira:Driving,Juggling
Un:Driving,Mineral collecting

CONSTRAINTS:

Number of users in input data is 200.
Number of different groups in input data is 15.
There can be users that do not participate in any group.
Friendship is mutual (if user A is a friend with user B, then user B is a friend with user A).

"""

import sys,string,re
test_cases=open(sys.argv[1],'r')
friends={}
groups={}
for i in test_cases.read().split('\n'):
    if i!='':
        a=i.split(':')[0]
        b=i.split(':')[1].split(',')
        c=i.split(':')[2].split(',')
        friends[a]=b
        groups[a]=c
        
for j in sorted(friends.keys()):
    list1=[groups[friends[j][i]] for i in xrange(len(friends[j]))]
    hobbies=[x for y in list1 for x in y]
    list3=[]
    for e in set(hobbies):
        if hobbies.count(e)>=len(friends[j])/2.0:
            list3.append(e)
    list4=[]
    for f in list3:
        if f not in groups[j]:
            list4.append(f)
    if list4!=[]:
        print j+':'+','.join(sorted(list4))
            

