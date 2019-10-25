# -*- coding: utf-8 -*-

def group_by_owners(files):
    return None
   
files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
} 

newdict = {}
for k,v in files.items():
    if (v in newdict):
        
        #print('if v ',v, 'k ',k)
        newdict[v].append(k)
         
        #print('if :dict ',newdict)           
    else:
        newdict[v] = [k]
        
        
print(newdict)


