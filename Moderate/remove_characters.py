"""
REMOVE CHARACTERS
CHALLENGE DESCRIPTION:


Write a program which removes specific characters from a string.

INPUT SAMPLE:

The first argument is a path to a file. The file contains the source strings and the characters that need to be scrubbed. Each source string and characters you need to scrub are delimited by comma.

For example:

how are you, abc
hello world, def

OUTPUT SAMPLE:

Print to stdout the scrubbed strings, one per line. Ensure that there are no trailing empty spaces on each line you print.

For example:

how re you
hllo worl

"""

# Remove all characters in one string, from another string

import sys
test_cases=open(sys.argv[1],'r')
for i in test_cases.read().split('\n'):
    if i!='':
        w=i.split(',')
        a=w[0].strip()
        b=w[1].strip()
        a=list(a)
        b=list(b)
        for j in b:
            while j in a:
                a.remove(j)
        print ''.join(a)


