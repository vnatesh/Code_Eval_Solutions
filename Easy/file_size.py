"""

FILE SIZE

CHALLENGE DESCRIPTION:


Print the size of a file in bytes.

INPUT:

The first argument to your program has the path to the file you need to check the size of.

OUTPUT SAMPLE:

Print the size of the file in bytes. E.g.

55

"""

import os,sys,argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename',help='Enter in the name of the file containing the test cases' )
args = parser.parse_args()


file_info=os.stat(args.filename)
print(file_info.st_size)
