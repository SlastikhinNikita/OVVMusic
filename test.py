# -*- coding: utf-8 -*-
    
	

FILENAMES = ['cat','dog','cat bird','lol','asda','czx','vzx']
IGNORLIST = ['cat','das','gd','xv','3','1','6']
	
	
print(FILENAMES)
print(IGNORLIST)
#FILENAMES=list(set(FILENAMES) - set(IGNORLIST))   







for e in FILENAMES:
    for i in IGNORLIST:
        if e.find(i) != -1:
            FILENAMES.remove(e)
		

print(FILENAMES)		
		
		
		
		
'''

g = ['mon1-1','mon2-2','mon3-3']
g2 = ['mon1-1','mon2-2']
for e in g:
    if not e in g2:
        print e
'''

