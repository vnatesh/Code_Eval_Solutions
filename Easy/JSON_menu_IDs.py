"""

JSON MENU IDS

CHALLENGE DESCRIPTION:

You have JSON string which describes a menu. Calculate the SUM of IDs of all "items" in the case a "label" exists for an item.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Input example is the following

{"menu": {"header": "menu", "items": [{"id": 27}, {"id": 0, "label": "Label 0"}, null, {"id": 93}, {"id": 85}, {"id": 54}, null, {"id": 46, "label": "Label 46"}]}}

{"menu": {"header": "menu", "items": [{"id": 81}]}}

{"menu": {"header": "menu", "items": [{"id": 70, "label": "Label 70"}, {"id": 85, "label": "Label 85"}, {"id": 93, "label": "Label 93"}, {"id": 2}]}}
All IDs are integers between 0 and 100. It can be 10 items maximum for a menu.

OUTPUT SAMPLE:

Print results in the following way.

46
0
248

"""

import sys,re
test_cases=open(sys.argv[1],'r')
for i in test_cases.read().split('\n'):
    if i!='':
        i=str(i)
        pattern=re.compile(r'Label\s\d+')
        list1=re.findall(pattern,i)
        print sum(map(int,[j[6:] for j in re.findall(pattern,i)]))
        

        
      
