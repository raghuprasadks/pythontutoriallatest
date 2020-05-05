# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 16:48:13 2020

@author: Thinkpad
"""

'''
service

name - raghu
itemtype - 1 - mobile 2 - tv 3- refrigerator
issue - mobile is getting heated
place - bengaluru
mobile - 9845547471
zipcode - 560077
status - open/closed

1. Create service
2. list
3. update
4. delete
5. search
6. Find all records having status as open
7. Find count of all records having status as open
8. Find percentage of open/totalnoofrecords
9. Find the citiwise count of service calls
'''


class Service():
    
    def __init__(self,name,itemtype,issue,place,mobileno,zipcode,status):
        self.name = name
        self.itemtype = itemtype
        self.issue = issue
        self.place = place
        self.mobileno = mobileno
        self.zipcode = zipcode
        self.status = status

    def info(self):
        print(self.name,self.itemtype,self.issue,self.place,self.mobileno,self.zipcode,self.status)
'''
1. Create service
'''
customerList = []
c1 = Service('Raghu',1,'Heating','Bengaluru',9845547471,560077,'Open')
customerList.append(c1)

c2 = Service('Rudresh',3,'Not cooling','Chennai',9845547472,600001,'Closed')
customerList.append(c2)

c3 = Service('Sravani',2,'Volume','Vizag',9619320218,530000,'Open')
customerList.append(c3)

c4 = Service('Shrayva',3,'Not cooling','Chennai',9845547472,600001,'Closed')
customerList.append(c4)

'''
2. list
'''   
for l in customerList:
    print(l.info())


'''
3. update
'''
number=int(input("Enter customer's mobile no.: "))
for l in customerList:
    if (l.mobileno==number):
        char=input("Enter updated attribute:")
        if (char=='name'):
            name = input("Enter new name")
            l.name = name
            print(l.info())

'''
4. Delete
'''
number = int(input("Enter mobile no. to be deleted: "))
for l in customerList:
    if (l.mobileno == number):
        customerList.remove(l)

'''
5. Search
'''
name =input("Enter name: ")
for l in customerList:
    
    if (l.name == name):
        print('Customer details:',l.info())
        
'''
6 & 7. Find all records having status as open
'''
      
countopen=0

for l in customerList:
    if (l.status == 'Open'):
        print("open cases ",l.info())
        countopen = countopen +customerList.count(l)
        
print ('count of open cases ',countopen)

'''
8. Find percentage of open/totalnoofrecords
'''

totalnoofrecords = len(customerList)

percentage = (countopen/totalnoofrecords)*100
print('Percentage of open cases%5.2f ' %(percentage))
        
'''
9. Find the citiwise count of service calls
'''

citylist=[]
for l in customerList:
    citylist.append(l.place)    
    
print('city list ',citylist)

dictcity ={}
for c in citylist:

    dictcity[c]=citylist.count(c)
    
print(dictcity)

    


