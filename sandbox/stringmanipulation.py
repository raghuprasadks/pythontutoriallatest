# -*- coding: utf-8 -*-
#ABaBCbG -- Count
word =input('Enter a word')
worddict = {}
for w in word:
    print(word.count(w),w)
    worddict[w]=word.count(w)
#print(worddict)
for k,v in worddict.items():
    print(v,k)

# print the word john in john@google.com 
email = input('Enter a email')
#email = 'john@google.com'
#print(email.index('@'))
firstpart = email[0:email.index('@')]
print(firstpart)   

# present in 
print ('an' in 'name') 


