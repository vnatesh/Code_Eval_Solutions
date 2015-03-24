"""

MORSE CODE

CHALLENGE DESCRIPTION:

You have received a text encoded with Morse code and want to decode it.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Input example is the following:

.- ...- ..--- .-- .... .. . -.-. -..-  ....- .....
-... .... ...--
Each letter is separated by space char, each word is separated by 2 space chars.

OUTPUT SAMPLE:

Print out decoded words. E.g.

AV2WHIECX 45
BH3
You program has to support letters and digits only.

"""

master={'..--.-': '_', '...--': '3', '--..--': ',', '....-': '4', '.....': '5', '-...': 'B', '-..-': 'X', '.-.': 'R', '--.-': 'Q', '--..': 'Z', '.': 'E', '.----.': "'", ' ': ' ', '..---': '2', '.--': 'W', '.-': 'A', '..': 'I', '-.-.': 'C', '---...': ':', '---': 'O', '-.--': 'Y', '-': 'T', '-..-.': '/', '.-..': 'L', '--.': 'G', '...': 'S', '-.--.-': ')', '..--..': '?', '.----': '1', '-----': '0', '-.-': 'K', '-..': 'D', '----.': '9', '-....': '6', '.---': 'J', '.--.': 'P', '.-.-.-': '.', '--': 'M', '-.': 'N', '....': 'H', '---..': '8', '...-': 'V', '--...': '7', '-.-.-.': ';', '..-': 'U', '..-.': 'F', '-....-': '-'}

import sys,string,itertools,re
test_cases=open(sys.argv[1],'r')
for i in test_cases.read().split('\n'):
    if i!='':
        i=i.split('  ')
        line=''
        for r in i:
            r=r.split(' ')
            for x in r:
		line+=(master[x])
            line+=' '
        print line
        
