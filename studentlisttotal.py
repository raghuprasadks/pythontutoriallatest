# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 12:59:39 2019

@author: Thinkpad
"""

lst = [10,1,4,33,77,5]

sum = 0
length = len(lst)
for l in lst:
    
    sum = sum + l
    
print('sum ',sum)
print('max ',max(lst))
print('min ',min(lst))
avg = sum/length
print('average ',avg)

lst = [10,1,4,33,77,5]

max = lst[0]

for l in lst:
    if (l > max):
        max = l
        
print('maximum ',max)

conlst = []
lst1 = {'name':'raghu','sub1':80,'sub2':77,'sub3':89}
lst2 = {'name':'ravi','sub1':99,'sub2':76,'sub3':92}
lst3 = {'name':'raghav','sub1':56,'sub2':88,'sub3':73}
conlst.append(lst1)
conlst.append(lst2)
conlst.append(lst3)
mt = []
sub1max = 0
index = 0
sub1index = 0
for i in conlst:
    total = 0    
    for k,v in i.items():
        if (k !='name'):
            total = total + v
        else:
            student = v
        if (k =='sub1'):
            if (v > sub1max):
                sub1max = v
                sub1index = index
    index = index + 1                
    print(student, total)
    tot = int(total)
    mt.append(tot)
print('total scores',mt)
maxscore = max(mt)
print('highest score ',maxscore) 
highindex = mt.index(maxscore)
print('index of max score ',highindex)
highscorer = conlst[highindex]['name']
print(highscorer, maxscore)
#print('maximum in subject 1',sub1max)
#print('maximum scorer index in subject 1',sub1index)

print('maximum scorer with highest marks in subject 1', conlst[sub1index]["name"],sub1max)
                                
        


