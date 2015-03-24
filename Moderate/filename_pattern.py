"""
FILENAME PATTERN
CHALLENGE DESCRIPTION:

You are given a filename pattern and a list of filenames. Find out which filenames from the list are matching the given pattern. The pattern can contain characters and the following wildcards:

? — matches any single character.
* — matches everything (any multiple characters, any single character, or empty string).
[abc] — matches any character inside brackets (in this example: a, b, or c).
Matching is case-sensitive.

INPUT SAMPLE:

The first argument is a file that contains space-separated filename pattern and filenames.

For example:

*7* johab.py gen_probe.ko palmtx.h macpath.py tzp dm-dirty-log.h 
bh1770.h pktloc faillog.8.gz zconf.gperf
*[0123456789]*[auoei]* IBM1008_420.so zfgrep limits.conf.5.gz tc.h 
ilogb.3.gz limits.conf CyrAsia-TerminusBold28x14.psf.gz nf_conntra
ck_sip.ko DistUpgradeViewNonInteractive.pyc NFKDQC
*.??? max_user_watches arptables.h net_namespace Kannada.pl 
menu_no_no.utf-8.vim shtags.1 unistd_32_ia32.h gettext-tools.mo 
ntpdate.md5sums linkat.2.gz
*.pdf OldItali.pl term.log plymouth-upstart-bridge rand.so libipw
.ko jisfreq.pyc impedance-analyzer xmon.h 1.5.0.3.txt bank
g*.* 56b8a0b6.0 sl.vim digctl.h groff-base.conffiles python
-software-properties.md5sums CountryInformation.py use_zero_page 
session-noninteractive d2i_RSAPublicKey.3ssl.gz container-detect
.log.4.gz
*[0123456789]* keyboard.h machinecheck 46b2fd3b.0 libip6t_frag.so 
timer_defs.h nano-menu.xpm NI vim-keys.conf setjmp.h memcg


OUTPUT SAMPLE:

Print filenames matching a given pattern to stdout. If there are no such files, print a minus ‘-’ character.

For example:

bh1770.h
IBM1008_420.so
menu_no_no.utf-8.vim
-
groff-base.conffiles
46b2fd3b.0 libip6t_frag.so

CONSTRAINTS:

Matching is case-sensitive.
Filenames cannot contain spaces.
There are 40 test cases and 100 filenames in every test case.

"""

import sys,string,re
test_cases=open(sys.argv[1],'r')
for i in test_cases.read().split('\n'):
    if i!='':
        pattern=i.split(' ')[0]
        a=string.replace(pattern,'*','\S*')
        a=string.replace(a,'?','\S')
        a=string.replace(a,'.','[.]')
        b=i.split(' ')[1:]
        list1=[]
        for j in b:
            if pattern[0]==pattern[-1]=='*':
                if re.findall(a,j)!=[]:
                    list1.append(j)

            elif pattern[0]!='*' and pattern[-1]=='*':
                if re.match(a,j):
                    list1.append(j)

            elif pattern[-1]!='*' and pattern[0]=='*':
                a+='\Z'
                if re.findall(a,j)!=[]:
                    list1.append(j)               
        if list1==[] or list1==[None]:
            print '-'
        else: print ' '.join(list1)
                
            
