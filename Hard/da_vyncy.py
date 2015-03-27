
"""
You were reading The Da Vyncy Code, the translation of a famous murder mystery novel into Python. The Code is finally revealed on the last page. You had reached the second to last page of the novel, and then you went to take a bathroom break.

While you were in the bathroom, the Illuminati snuck into your room and shredded the last page of your book. You had 9 backup copies of the book just in case of an attack like this, but the Illuminati shredded the last page from each of the those books, too. Then they propped up a fan, aimed it at the remains, and turned it on at high-speed. 

The last page of your book is now in tatters. 

However, there are many text fragments floating in the air. You enlist an undergraduate student for a 'summer research project' of typing up these fragments into a file. Your mission: reassemble the last page of your book. 

Problem Description 
============= 

(adapted from a problem by Julie Zelenski) 

Write a program that, given a set of fragments (ASCII strings), uses the following method (or a method producing identical output) to reassemble the document from which they came: 

At each step, your program searches the collection of fragments. It should find the pair of fragments with the maximal overlap match and merge those two fragments. This operation should decrease the total number of fragments by one. If there is more than one pair of fragments with a maximal overlap, you may break the tie in an arbitrary fashion.Fragments must overlap at their start or end. For example:

- "ABCDEF" and "DEFG" overlap with overlap length 3
- "ABCDEF" and "XYZABC" overlap with overlap length 3
- "ABCDEF" and "BCDE" overlap with overlap length 4
- "ABCDEF" and "XCDEZ" do *not* overlap (they have matching characters in the middle, but the overlap does not extend to the end of either string).
Fear not - any test inputs given to you will satisfy the property that the tie-breaking order will not change the result, as long as you only ever merge maximally-overlapping fragments. Bonus points if you can come up with an input for which this property does not hold (ie, there exists more than 1 different final reconstruction, depending on the order in which different maximal-overlap merges are performed) -- if you find such a case, submit it in the comments to your code! 

All characters must match exactly in a sequence (case-sensitive). Assume that your undergraduate has provided you with clean data (i.e., there are no typos).

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Each line in this file represents a test case. Each line contains fragments separated by a semicolon, which your assistant has painstakingly transcribed from the shreds left by the Illuminati. You may assume that every fragment has length at least 2 and at most 1022 (excluding the trailing newline, which should *not* be considered part of the fragment). E.g. Here are two test cases.

O draconia;conian devil! Oh la;h lame sa;saint!
m quaerat voluptatem.;pora incidunt ut labore et d;, consectetur, adipisci velit;olore magnam aliqua;idunt ut labore et dolore magn;uptatem.;i dolorem ipsum qu;iquam quaerat vol;psum quia dolor sit amet, consectetur, a;ia dolor sit amet, conse;squam est, qui do;Neque porro quisquam est, qu;aerat voluptatem.;m eius modi tem;Neque porro qui;, sed quia non numquam ei;lorem ipsum quia dolor sit amet;ctetur, adipisci velit, sed quia non numq;unt ut labore et dolore magnam aliquam qu;dipisci velit, sed quia non numqua;us modi tempora incid;Neque porro quisquam est, qui dolorem i;uam eius modi tem;pora inc;am al

OUTPUT SAMPLE:

Print out the original document, reassembled. E.g.

O draconian devil! Oh lame saint!
Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem.

"""

# This program is a greedy optimization for recreating a master string of characters from a list of overlapping substrings of the master string. 


import sys,string,itertools,difflib,time
start=time.time()

def side1(s):                                       # Find all substrings from one side (eg. s='ABCDE' and side1(s) = set(['BCDE', 'CDE', 'DE', 'ABCDE', 'E']) )
    return set([s[i:] for i in xrange(len(s))])

def side2(s):                                       # Find all substrings from the other side (eg. s='ABCDE' and side2(s) = set(['', 'A', 'AB', 'ABCD', 'ABC']) )
    return set([s[:i] for i in xrange(len(s))])     # The side functions are defined such that returned substrings are only those at the end (side1) or beginning (side2) of the input string


def overlap(a,b):
    if b in a: return b                     
    elif a in b: return a                    # In the trivial cases where b is in a or a is in b, return either b or a respectively
    q = side1(a) & side2(b)                   
    r = side1(b) & side2(a)                  # Create two sets of common overlaps from either side. This satisfies the condition that overlaps must occur at the start or end
    if q|r == set([]):                       # If the union of the two sets is empty, there are no overlaps so return ''
        return ''
    else: return max(q|r , key=len)           # If there are overlaps, return the longest one


def merge(a,b):    
    if overlap(a,b) == overlap(b,a) == '':  
            return ''
    elif a in b: return b
    elif b in a: return a                 

    q=len(overlap(a,b))
    if overlap(a,b) == a[:q] == b[-q:]: return b+a[q:]
    elif overlap(a,b) == a[-q:] == b[:q]: return a+b[q:] 



test_cases=open(sys.argv[1],'r')
for test in test_cases.read().split('\n'):
    line = [j for j in string.split(''.join(test),';')]
    q=line[0]
    while len(line)!=0:
        pairs=[(q,seq) for seq in line]
        matches=[overlap(y[0],y[1]) for y in pairs]
        best_match = max(matches,key=len)
        index = matches.index(best_match)
        x = pairs[index]
        q=merge(x[0],x[1])
        line=set(line)-set(x)
    print q



print time.time()-start

##            
        

###------------------------------BONUS------------------------------------
##
### If you have a list of strings ['atgc','gcat','attgc'], they can merge on the first
### operation as ['atgcat','attgc'], ['gcattgc','atgc' ] or ['gcatgc','attgc'] and can
### merge on the second operation as ['atgcattgc'] or ['attgcatgc'], yielding two different
### possible final reconstructions
##
##

# ___________TEST CASE________________

##O draconia;conian devil! Oh la;h lame sa;saint!
##m quaerat voluptatem.;pora incidunt ut labore et d;, consectetur, adipisci velit;olore magnam aliqua;idunt ut labore et dolore magn;uptatem.;i dolorem ipsum qu;iquam quaerat vol;psum quia dolor sit amet, consectetur, a;ia dolor sit amet, conse;squam est, qui do;Neque porro quisquam est, qu;aerat voluptatem.;m eius modi tem;Neque porro qui;, sed quia non numquam ei;lorem ipsum quia dolor sit amet;ctetur, adipisci velit, sed quia non numq;unt ut labore et dolore magnam aliquam qu;dipisci velit, sed quia non numqua;us modi tempora incid;Neque porro quisquam est, qui dolorem i;uam eius modi tem;pora inc;am al
##t,he Holy@ Gr'ail, wh^ich ;be da Teacher for wh!o;"t~*he Vatican. He compels La;marri]ed Mary Magdale;ary Magdalene a%.nd bore ch;olve t~he se|co`nd cryptex's;lizes is]\"APPLE.\" Lan-gd'o;retly opens cryptex a,nd remove; at gunpoint to solve t~he ;ve at Abbey, Tea'bi!ng <is \;x a,nd removes its contents bef; time %the.y arrive at Abbe;is\ a series .of documen<ts e; he beli$eves. is\ a serie;wi@shes' to use t,he Holy@;documen<ts establishing\"th-at;'bi!ng <is \"re&vealed| to` be ;E.\" Lan-gd'on secretly opens c;on# re`alizes is]\"AP;aled| to` be da Teache; which Lan]gdon# re`aliz;e compels Lan>gd)on at gunpoint;ldren, in ord`er to ruin \"t;a%.nd bore ch\ildren, in ord;er to ruin \"t~*he Vatican;i$las #is work$ing. Tea$bing wi;r'ail, wh^ich he beli$ev; cryptex's pw=d, which Lan]gdo;. Tea$bing wi@shes' to u;er for wh!om Si$las #is wor;hing\"th-at Je%sus Ch;t Je%sus Christ marri]ed Mary;s contents before destroyin@g
##ni*ng _th%e c[ryp6tex, th#e;name, \"SOFIA.\" Openi;FIA.\" Openi*ng _th%e ; estrangeme^nt f{rom< her) ;spell o,ut S\"oph:ie}'s;hat da proper combination ?; to ?the tomb of Isaac ;ctedly fr>om university, ;. Arriving home unexpectedly fr>;aller cry'pt*ex ins'ide it, ;s'ide it, along@ wi_th a; letters spell o,ut S\;ombination ?of letters spe;er riddle: th>at ultimately;f{rom< her) g@ran3dfat*he;_ th}e se]cret basement /of he,r;at ultimately le\"ads ;ng@ wi_th anot}her riddle: th; \"to Britain, So>ph/ie r;re|veals th=e source of\"her e;ten years earlier. Arriving h;[ryp6tex, th#ey discover a sm*a;S\"oph:ie}'s given name, \"SOF;wh:ich th,ey conclude t;h:e group to ?the tomb ;n, So>ph/ie re|veals th=e ;over a sm*aller cry'pt*;niversity, Sop]hie clandestinely;ce of\"her estrangeme^n; conclude that da prope;pri'ng fertility rite conduc;ly le\"ads th:e group to ;omb of Isaac Newton <at =Ab'bey;<at =Ab'bey. During/ t|he@;g@ran3dfat*he~r, ten years ea;uring/ t|he@ flight \"to Brit;y rite conducted in_ th}e se]cret;ely wit'ne]sses a spri'ng ferti;ement /of he,r gr&and4fat>her; clandestinely wit'ne]ss
##own as Hieros gamos or \"sacr;establishing\"th-at Je%sus Ch;y, Tea'bi!ng <is \"re&vealed| to`;amos or \"sacred ma=rriage; da Teacher for wh!om Si;l c:ontact with Sau#niere;r for wh!om Si$las #is;th Sau#niere.Lang|don \! th\";ne a%.nd bore ch\ildren,;of documen<ts establishing;ch\ildren, in ord`er to ;s a'n ancient ceremony k\nown;i@shes' to use t,he Holy;arri]ed Mary Magdalene a%.nd bore;re&vealed| to` be da Teache;reaks off all c:ontact wit;remony k\nown as Hieros ;use t,he Holy@ Gr'ail, wh^ic; he beli$eves. is\ a series .;t[he time %the.y arrive ;n \"t~*he Vatican. He compels La;'ail, wh^ich he beli$eve;\ a series .of documen<ts;ed ma=rriage\". By t[he time ;th\"at what she% witnessed w%a;ng|don \! th\"at what s;-at Je%sus Christ marri]ed Mary;Si$las #is work$ing. Tea$bing;e.y arrive at Abbey, Tea'bi!ng <;. Tea$bing wi@shes' to u;witnessed w%as a'n ancien;n ord`er to ruin \"t~*he Vat
##m quaerat voluptatem.;pora incidunt ut labore et d;, consectetur, adipisci velit;olore magnam aliqua;idunt ut labore et dolore magn;uptatem.;i dolorem ipsum qu;iquam quaerat vol;psum quia dolor sit amet, consectetur, a;ia dolor sit amet, conse;squam est, qui do;Neque porro quisquam est, qu;aerat voluptatem.;m eius modi tem;Neque porro qui;, sed quia non numquam ei;lorem ipsum quia dolor sit amet;ctetur, adipisci velit, sed quia non numq;unt ut labore et dolore magnam aliquam qu;dipisci velit, sed quia non numqua;us modi tempora incid;Neque porro quisquam est, qui dolorem i;uam eius modi tem;pora inc;am al
##/ere's )est`ra?nged gr'andda;f# hers gr>andfath#er,'s in;h#er,'s involveme\"nt ;)pagan gr\"oup. However, s*h;rer, because \of *the note h/;gr#and?fat'he.r left sayin,g to;ft sayin,g to \"fi!nd' La.ng^;-hat her( gra1ndfa{th;\"hat Fa,che thinks L!an; troubled b%y memories& ;erased prior to\ Lan<gdon$; memories& of# hers gr>an;r>, a)<nd t\"hat Fa,che ;*the note h/er :gr#and?fat'h; inten<ded L#'an-~gdon% to d;<n a> sec,ret )pagan gr\"ou;ged gr'anddaughter>, a)<nd t\";}e isSaun&i^/ere's )est`r;s*he understands t-hat her( g; gra1ndfa{ther` inten<ded L#;?s t$he mu'rderer, because;thinks L!an\<g:don i?s t$he mu';~gdon% to decipher th>;n,\" wh^$ich s$he says Fa$che;e says Fa$che h>ad erased prior;/rival. Sop%hie i]s troubled ;!nd' La.ng^don,\" wh^$ic;g#do(n sh}e isSaun&i^/;However, s*he underst;\ Lan<gdon$'s ar/rival. Sop;olveme\"nt i<n a> sec,ret
##"the> c]ryp&tex is for;al, hand-held vault w[it;ie an@d Lan\gd!on go t.o ;x t\h%ey fi(nd :the key)st%one: a ;d L>ang_don rea.lize l~ead=;ad=s them to, a s(afe) b.ox at;'he Paris branch of @t>he Dep;rich, wh(ich Sop-hie an@d Lan\g;ository Bank of Zurich, wh(ic;g po=lice!. In th/e safe b%ox ;\gd!on go t.o after\" escapin#g;f @t>he Depository Bank ;to decipher th>=e code, w!;h five c/oncentric, rotati(ng di;rs [tha`t when lin^ed up pr(ope;er\" escapin#g po=lice!. ;key)st%one: a cry(<pte$x, a cy;rrect pas:sw_ord, unlocki:n;>=e code, w!hic#h s?he an_d ;/th lette?rs [tha`t wh; s?he an_d L>ang_don ;/e safe b%ox t\h%ey fi(n; vault w[ith five c/oncen;<ded L#'an-~gdon% to decipher t; dials labeled wi/th lette;ed up pr(operly form ;te$x, a cylindrical, hand-he;.lize l~ead=s them to; rotati(ng dials labele;, unlocki:ng @the device.;fe) b.ox at :t'he Paris bran;yp&tex is forced o:pen, a,n e;operly form t@h,e correct pas:s;the device. If \"the> c]ryp
##=ce Captain Bezu Fac\";@mmon Harvard Professor Robe;on busines-s. Poli=ce Captain;oned> t=.os\"help\? pol=ice decod;l?udes) a Fibonacci sequence le[;@is li}fe. Da no`te al,so i$nc;unie$re)'s body is dis>co\v;o is< i{n town ]on busines-s. ;a'il. After Sa@&unie$re)'s bod;a#l minutes ,of h@is li}fe. ;al,so i$ncl?udes) a Fibo;'e) H}oly\@! Gra'il. After ; }he w>as summoned> t=.os\;i&ere l/eft dur/ing] th|;e_t%ells him th`a{t }he w>as su;ofessor Robert <Lan%]g~;equence le[ft o(ut [of or%de;s.sage Sa@uni&ere l/eft du;ol=ice decode <the) cr'yp;in Bezu Fac\"he_t%ells him ;dur/ing] th|e fi_na#l minutes ,;ut [of or%der*, as` a c@;e. Lan@gd}on ? to Fac;vian Man, police su@mmon Harvard ; is dis>co\vered~ in. th!)e po;e <the) cr'yptic mes.sage Sa@u;rch f&or th'e) H}oly\@! ;pose of~t\"heVitruvian Man, po; in. th!)e pose of~t\"h;der*, as` a c@ode. Lan@gd};t <Lan%]g~don, w=ho is< i{n to
##ecretly opens cryptex a,nd rem;front #of Te,abing.T;e, |who by now knows t@hat L; hiding in an Opus De;S\il#as has be>en used _;to murder innoce}nt p; find Si_las hiding in a;e, rus?hes t\"o help t<he cop;ows t@hat Lan,gd@on w*;eabi$ng i\"s arrested by Fache;ted by Fache, |who by now;izing th?at S\il#as has ;nnoce}nt people, rus?hes t\;d, which Lan]gdon# re`alizes i;ontents before destroyin;be>en used _to murder ;x a,nd removes its contents befo;ssumes -tha{t they are ther;Lan,gd@on w*as inn[ocent. Bi?sh;"APPLE.\" Lan-gd'on secre;help t<he cops find him. When p;-gd'on secretly opens ;[ocent. Bi?shop, r(eal; Te,abing.Teabi$ng i\"s ;n an Opus Dei Center, he ;nd him. When police find Si_la; destroyin@g it in front #of ;hey are there to k<ill;?shop, r(ealizing th?a;i Center, he assumes -tha{;e`alizes is]\"APPLE.\" L
##etly ex-plai'ns ']to !L;e (believe}s. A pol]ice cr>y;e isSaun&i^/ere's )est`ra?nged gr; h>ad erased prior to\ Lan<gdon$'s;nd t\"hat Fa,che thinks L!;'ns ']to !Lang#do(n sh};h s$he says Fa$che h>ad erased ;g#do(n sh}e isSaun&i^/;t(o t{he\ godd*ess a/nd n/;,\" wh^$ich s$he says Fa; \"devil worship\", as;nd $that| th@e pentacle Sa#u;left sayin,g to \"fi!nd' La.n;nddaughter>, a)<nd t\"hat F;e Ne@veu s|ecr(etly ex-pl;he thinks L!an\<g:don i?s t$h;dd*ess a/nd n/ot \"devil wors;'allu#sion~ t(o t{he\ g;ol]ice cr>yptographe-r, S;sen[ts an 'allu#sion~ t;g:don i?s t$he mu'rderer, bec;re drew in his own blood repr;of *the note h/er :gr#and?fat'; Lan<gdon$'s ar/rival. So;r#and?fat'he.r left sayin,g;'odd{es_s artwork a-nd $that| th;tographe-r, So\"ph!ie Ne@veu s|ecr;i!nd' La.ng^don,\" wh^$ich ; blood represen[ts an 'al;tacle Sa#uni=ere drew in h;orship\", as Fa&che (believe}s;st`ra?nged gr'anddaughter;rderer, because \of *the no
##<ded L#'an-~gdon% to decip;=e code, w!hic#h s?he a;<gdon$'s ar/rival. Sop%hie i];t :t'he Paris branch of @t>he D; an_d L>ang_don rea.liz;"nt i<n a> sec,ret )pagan gr\"ou;p. However, s*he understands t-h;h of @t>he Depository; because \of *the note ;gan gr\"oup. However;r>andfath#er,'s involv;?nged gr'anddaughter>,;troubled b%y memories& of# hers; Sop%hie i]s troubled b%y;nks L!an\<g:don i?s t$he mu'rd; Depository Bank of Zur;\"fi!nd' La.ng^don,\" w;f *the note h/er :gr#and?fat'he.;ies& of# hers gr>andfath#;$he says Fa$che h>ad erased ;-hat her( gra1ndfa{ther`;ft sayin,g to \"fi!nd' La.;1ndfa{ther` inten<ded L#'an-;erstands t-hat her( ;l~ead=s them to, a s(afe) b.o;ry Bank of Zurich, wh(ich; prior to\ Lan<gdon$'s ar/;at Fa,che thinks L!an\<g:;anddaughter>, a)<nd t\"hat;ere's )est`ra?nged gr'andd;r,'s involveme\"nt i<n a> se;don rea.lize l~ead=s them;La.ng^don,\" wh^$ich s$he says Fa$;w!hic#h s?he an_d L>ang;#and?fat'he.r left sayin,g to ; h>ad erased prior to\ La;a)<nd t\"hat Fa,che th; s(afe) b.ox at :t'he Paris;gdon% to decipher th>=e code, w!;?s t$he mu'rderer, because \
##men<ts establishing\"th-at Je;in ord`er to ruin \"t~;eries .of documen<ts estab;m Si$las #is work$ing. Tea$bi;ary Magdalene a%.nd bore ch\i;s pw=d, which Lan]gdon# re`aliz; or \"sacred ma=rriage\".;o`nd cryptex's pw=d, wh;d'on secretly opens crypt;.nd bore ch\ildren, in ord`er to;opens cryptex a,nd removes i; ruin \"t~*he Vatican. He compe;bbey, Tea'bi!ng <is \"re&ve;can. He compels Lan>gd)on;ng\"th-at Je%sus Christ marri;don# re`alizes is]\"APPLE.\;solve t~he se|co`nd crypt;a=rriage\". By t[he time;s is]\"APPLE.\" Lan-gd'on secretl;ed| to` be da Teacher for wh;,nd removes its contents b;l, wh^ich he beli$eves. is\ a s;els Lan>gd)on at gunpoint;Christ marri]ed Mary Magdale;acher for wh!om Si$las #is; ceremony k\nown as Hiero;By t[he time %the.y arrive ;t,he Holy@ Gr'ail, wh^ich he ;ing. Tea$bing wi@shes' to ;g wi@shes' to use t,he Holy@ Gr;the.y arrive at Abbey, Tea'b;wn as Hieros gamos or \"sacred; <is \"re&vealed| to` be da ; at gunpoint to solve t~he;ves. is\ a series .of
##n-gd'on secretly opens c;\"s arrested by Fache, ;e,abing.Teabi$ng i\"s arreste;ve t~he se|co`nd crypte;ront #of Te,abing.Teabi;o by now knows t@hat ;ed by Fache, |who by now k;wh^ich he beli$eves. is\ a ser; gunpoint to solve t~he se|co`;Lan,gd@on w*as inn[ocent. Bi?s;co`nd cryptex's pw=d, w; be>en used _to murder innoc;es. is\ a series .of do;ch\ildren, in ord`er to ruin \";eries .of documen<ts establish;lene a%.nd bore ch\ildren, i;r to ruin \"t~*he Vatican. He co;ri]ed Mary Magdalene a%.nd ;murder innoce}nt people, ru;t people, rus?hes t\"o help t<h;ex's pw=d, which Lan]g;s Lan>gd)on at gunpoint to; which Lan]gdon# re`alizes i;ealizing th?at S\il#as ha; its contents before destroyin@g ;s is]\"APPLE.\" Lan-gd'on sec;Vatican. He compels Lan>gd)on;[ocent. Bi?shop, r(ealizing th?;nows t@hat Lan,gd@on w;at S\il#as has be>en used;-at Je%sus Christ marri]ed Mary ; destroyin@g it in front #of Te;s establishing\"th-at Je%sus Ch;ptex a,nd removes its contents;re`alizes is]\"APPLE;etly opens cryptex a,nd re
##O draconia;conian devil! Oh la;h lame sa;saint!
##ey fi(nd :the key)st%on;h,e correct pas:sw_ord, ;t when lin^ed up pr(operly form;b%ox t\h%ey fi(nd :the ; rotati(ng dials labeled wi/th l;operly form t@h,e correct ; vial of vinegar ruptur@es a)nd ; after\" escapin#g po=lice!. ;drical, hand-held vault w[;tur@es a)nd disso*lves t.he m;e key)st%one: a cry(<p;ten on papyrus. )The. b;po=lice!. In th/e safe;te?rs [tha`t when lin^ed ; If \"the> c]ryp&tex is fo;e$x, a cylindrical, hand-h;ie an@d Lan\gd!on go t;p&tex is forced o:pen, a,n e; a cry(<pte$x, a cyli; wh(ich Sop-hie an@d Lan\;ld vault w[ith five c/oncentric;led wi/th lette?rs [tha; c/oncentric, rotati(ng d;*lves t.he mes\sage, wh*ich ;d o:pen, a,n enclosed vial of vi;e, wh*ich w#as written on pap;ki:ng @the device. If \"the> c;as:sw_ord, unlocki:ng @the ;n th/e safe b%ox t\h%ey;an\gd!on go t.o after\" esc
##WHMHT_p\fDZsJo;FjhEzTAYPdDEEqaB;XmgfCrBwqYfy^qlsGvs;jvjSxwcusgKqsgyjTZ;xGSJzmwq[jO[oPYdTxMW;ONW\zUKsSnTgI;WHMHT_p\fDZsJoFjh;EzTAYPdDEEqaBXm;gfCrBwqYfy^qlsGvsjv;jSxwcusgKqsgyjTZxG;SJzmwq[jO[oPYdTxMWO;NW\zUKsSnTgI;WHMHT_p\f;DZsJo;FjhEzTAYPdDEEqaB;XmgfCrBwqYfy^qlsG;vsjvjSxwcusgKqsgyjT;ZxGSJzmwq[jO[oP;YdTxMWONW\zUKsSnTgI;WHMHT_p\fDZsJoFjhEzTAYP;dDEEqaBXmgfCrBwqYfy;^qlsGvsjvjS;xwcusgKqsgyj;TZxGSJzmwq;[jO[oPYdTxMWONW\z;UKsSnTgI;WHMHT_p\fDZsJoFjhEzT;AYPdDEEqaBXmgfCrBw;qYfy^qlsGvsjvjS;xwcus;gKqsgyjTZxGSJ;zmwq[jO[o;PYdTxMWONW\zUKsS;nTgI;WHMHT_p\fDZsJ;oFjhEzTAYPdDEEqaBXmgfC;rBwqYfy^qls;GvsjvjSxwcusgKqsg;yjTZxGSJzmwq[jO[oPYd;TxMWONW\zUKs;SnTgI;WHMHT_p\fDZs;JoFjhEzTAYPdDEEqaBXmgfC;rBwq;Yfy^qlsGvsjvjSx;wcusgKqsgyjTZxGSJzm;wq[jO[oPYdTxMWONW;\zUKsSnTgI;WHMHT_p\fDZsJoFjh;EzTAYPdDEEqaBXmgfCr;BwqYfy^qlsGvsjvj;SxwcusgKqsgyjTZxGSJzmw;q[jO[oPYdT;xMWONW\zUKsSnTgI;WHMHT_p\fDZsJoFjhE;zTAYPdDEEqa;BXmgfCrBwq;Yfy^qlsGvsjvjSx;wcusgKqsgyjTZxGSJzmwq;[jO[oPYdTxMWON;W\zUKsSnTgI;WHMHT_p\fDZsJoFjhEzTAY;PdDEEqaBXmgfCrBwqYf;y^qlsGvsjvjSxw;cusgKqsgyjTZxGSJzmwq[jO[o;PYdTxMWONW;\zUKsSnTgI;WHMHT_p\fDZsJoFjhEzTA;YPdDEEqaBXmgfCr;BwqYfy^qlsGvsjv;jSxwcusgKqsgyjTZx;GSJzmwq[jO[oPYd;TxMWONW\zUKsSnTgI;WHMHT_p\fDZs;JoFjhEzTAYPdDEE;qaBXmgfCrBwqYfy;^qlsGvsjvjSxwcu;sgKqsgyjTZxGSJzmwq[j;O[oPY;dTxMWONW\zUKsSnTgI;WHMHT_p\fDZsJoFjhEz;TAYPdDEEqaBXmgfCrBwq;Yfy^ql;sGvsjvjSxwcusgKqsgyjTZxGS;Jzmwq[jO[oPYdTx;MWONW\zUKsSnTgI;WHMHT_p\fDZsJoFjh;EzTAYPdDEEqaBXmg;fCrBwqYfy^qlsG;vsjvjSxwcusgKqsgyjTZ;xGSJzmwq[jO[oPY;dTxMWONW\zU;KsSnTgI;WHMHT_p\fDZsJoFjhEzTA;YPdDEEqaBXmgf;CrBwqYfy^qlsG;vsjvjSxwcusgKqsgyjTZxG;SJzmwq[jO[oPY;dTxMWONW\zUKsSnTgI
##ell o,ut S\"oph:ie}'s given;s ]of Ma\"ry. trio then f; tomb of Isaac Newton <at =A;n name, \"SOFIA.\" Openi*ng _;wton <at =Ab'bey. During/ t|h;me^nt f{rom< her) g@ran3dfat*he~;n ?of letters spell o,ut S\"; trio then fl)ees# th%*e cou@nt\;%e c[ryp6tex, th#ey disc;:ich th,ey conclude t;\"to Britain, So>ph/ie;t}her riddle: th>at ul;m university, Sop]hie clande;, th#ey discover a sm*aller cr;an3dfat*he~r, ten years ear;in, So>ph/ie re|veals th=e ;th%*e cou@nt\"ry on Tea}$;e|veals th=e source of\"her estran;ectedly fr>om university,;ins'ide it, along@ wi_th ano; Openi*ng _th%e c[ryp6te;conclude that da proper combi;"ry on Tea}$b.ing's privat;ie}'s given name, \"SOF; ten years earlier. Arriving home;mately le\"ads th:e group;rriving home unexpectedly fr;roper combination ?of letters ; sm*aller cry'pt*ex ins'ide it,;ane, on wh:ich th,ey ;f\"her estrangeme^nt f{rom<;.ing's private plane, on wh:; During/ t|he@ flight \"to Britai; th:e group to ?the tomb of Is;dle: th>at ultimately le\";g@ wi_th anot}her riddl
##'ng fertility rite conducted i;arlier. Arriving home unex;nation ?of letters spell o,;ex, th#ey discover a sm*aller cry;h>at ultimately le\"ads th:e gr;along@ wi_th anot}her riddle: th;ers spell o,ut S\"oph:ie}'s giv;omb of Isaac Newton <a;th=e source of\"her estr;to Britain, So>ph/ie re|veals th;andestinely wit'ne]sses ;oph:ie}'s given name, \"SOFI;er) g@ran3dfat*he~r, ten y; t|he@ flight \"to Britain, ;bey. During/ t|he@ flight; sm*aller cry'pt*ex ins'ide it,;ing home unexpectedly fr>om un; on wh:ich th,ey conclude th;t'ne]sses a spri'ng fertili;re|veals th=e source ;me, \"SOFIA.\" Openi*ng _th%e; ins'ide it, along@ wi_th a;eni*ng _th%e c[ryp6tex, th#ey disc; da proper combination ?of l;ads th:e group to ?the t; riddle: th>at ultimat;up to ?the tomb of Isaac;ity, Sop]hie clandestinely;angeme^nt f{rom< her) g@ran3d;t*he~r, ten years earlier. Arriv; Newton <at =Ab'bey. During/ ;dly fr>om university, Sop]hie;of\"her estrangeme^nt f{r;onclude that da proper com
##an expert on the{ H\oly' Gr;`ts password. L'ang\"d; Neveu take k\eys#to<ne 'to L);a sm*aller cry'pt*ex ins;clues %to i`ts password; it, along@ wi_th anot}her riddle:;cry'pt*ex ins'ide it, along@ wi;S\"oph:ie}'s given nam; n@ot a cup, b(ut t)=he .to@;le\"ads th:e group to ?the t;vate plane, on wh:ich t; co%ntaining{ th)e bones ]of;u@nt\"ry on Tea}$b.ing's;th>at ultimately le\"ads th:e;ord. L'ang\"do{n a$nd Neveu take k;FIA.\" Openi*ng _th%e c[ryp6;\"ry. trio then fl)ees# th%*e c;&bi\ng explai*ns t'hat ? is ;t}her riddle: th>at ulti;Tea}$b.ing's private plane; th#ey discover a sm*aller cr;ox co.nta3in]ing cry<pt.ex co; letters spell o,ut S\"oph:ie}'s;h)e bones ]of Ma\"ry. trio;ail. ^There, :Tea&bi\ng expla;g>don's friend, Sir Leigh Te;up to ?the tomb of Isaac N; Sir Leigh Teabing, an expert on;_th%e c[ryp6tex, th#ey disco;l)ees# th%*e cou@nt\"ry o;ch th,ey conclude that da pro;'s given name, \"SOFIA.\" Openi;that da proper combination ?o;ination ?of letters spe;ns t'hat ? is n@ot a cup, ;e, on wh:ich th,ey con;t t)=he .to@mb co%ntaining{;y<pt.ex con>tains clues %to i;{ H\oly' Gr.ail. ^There;to<ne 'to L)ang>don's fr
##he subject {of g'odd{es_s ;a/nd n/ot \"devil worship\",;te al,so i$ncl?udes) a Fibonacc;minutes ,of h@is li}fe.;de <the) cr'yptic mes.sage Sa@;ty in *t|\"he subject {of;h@e pentacle Sa#uni=ere drew;is own blood represen[ts a;^ th)at S`aun{ie&re wa@s a l;ci sequence le[ft o(ut ;believe}s. A pol]ice cr>yptog;mes.sage Sa@uni&ere l/eft du;k a-nd $that| th@e pentacle S; as Fa&che (believe}s. A ; t{he\ godd*ess a/nd n/ot ;lu#sion~ t(o t{he\ godd*e;e wa@s a leadi^ng authorit;il worship\", as Fa&che (be;a Fibonacci sequence;e[ft o(ut [of or%der*, as` a c;ng authority in *t|\"h;he-r, So\"ph!ie Ne@veu s|ec;er*, as` a c@ode. Lan@gd}on ?;ere l/eft dur/ing] th|e fi_na#l m;represen[ts an 'allu#sion~ t(o t;#uni=ere drew in his own blood; g'odd{es_s artwork a-nd $th;ce cr>yptographe-r, So\"ph;h|e fi_na#l minutes ,of h;h@is li}fe. Da no`te al,so i$n;Lan@gd}on ? to Fac]he^ th)at S`a
##ff all c:ontact with Sau#n;.y arrive at Abbey, Tea'b;t with Sau#niere.Lang|don \;-to a woman @at %/t|he;% witnessed w%as a'n ancien;er making love -to a woman;t/he go#ddess. She flees ho; Holy@ Gr'ail, wh^ich he beli;to use t,he Holy@ Gr'a;$bing wi@shes' to use t,he ;t Abbey, Tea'bi!ng <is \"re&v;a'n ancient ceremony k\now;ceremony k\nown as Hiero; for wh!om Si$las #is work$ing. ;n \! th\"at what she% witnessed;e.Lang|don \! th\"at ;ks a!nd chanti,ng praise to? t;ouse a.n]d breaks off all c:ont; ma=rriage\". By t[he tim;raise to? t/he go#dde; @at %/t|he cen'ter of a r;wn as Hieros gamos or \"sacre;en<ts establishing\"th-at Je%;eves. is\ a series .of; series .of documen<ts establ; <is \"re&vealed| to` be da T;o` be da Teacher for wh!om ;By t[he time %the.y arrive at ;h^ich he beli$eves. is\ ;n'ter of a ritual attended `b; She flees house a.n]d b;s or \"sacred ma=rriage\;l attended `by men a,!nd w;#is work$ing. Tea$bing wi@shes; men a,!nd women w`ho a(re wear; a(re wearing masks a!nd chan
##

