# -*- coding: utf-8 -*-
import time
epoch =time.time()
print("epoch",epoch)
t = time.localtime(epoch)
print('local time',t)
d = t.tm_mday
m = t.tm_mon
y = t.tm_year
print('Current date is %d-%d-%d' %(d,m,y))
te = time.ctime(epoch)
print('Ctime : epoch ',te)
t = time.ctime()
print('ctime ',t)

from datetime import *
now = datetime.now()
print(now)
print('Date now {}/{}/{}'.format(now.day,now.month,now.year))
print('Time now {}:{}:{}'.format(now.hour,now.minute,now.second))

today = datetime.today()
print("Today's date and time",today)
td = date.today()
print("Today's date",td)
d = date(1980,1,1)
print('date of Birth',d)
t = time(7,5)
print('time of birth',t)
dt= datetime.combine(d,t)
print('Date and time of birth 1st kid',dt)
dt1 = datetime(year=2016,month=6,day=24,hour=19,minute=59)
print('date 1',dt1)
dt2 = dt1.replace(year=2018)
print('Date and time of 2nd kid birth',dt2)

'''
strf format
'''
x = datetime.now()
print('current date and time',x)

print(x.strftime("%a"))


day = input ("Enter date in dd/mm/yyyy format")
d, m, y = day.split('/')
if (int(y)%4 == 0):
    print('its a leap year')
else:
    print('its not a leap year')
    
d,m,y = input("Enter date in dd/mm/yyyy format").split('/')
print (d,m,y)
d,m,y = [int (x) for x in input("Enter date in dd/mm/yyyy format").split('/')]
print ('converted to int' ,d,m,y)
    
lst = [int (x) for x in input("Enter date in dd/mm/yyyy format").split('/')]
print('list ',lst)

a,b,c=[10,20,30]
print(a,b,c)

'''
https://www.w3resource.com/python/python-date-and-time.php
'''
import datetime
today = datetime.date.today()
print('today ',today)
new_year = datetime.date(2020, 1, 1)
print(new_year)

#import datetime
#Time object
noon = datetime.time(12, 0, 0)
print(noon)

# Current datetime
now = datetime.datetime.now()
print(now)

# Datetime object
millenium_turn = datetime.datetime(2020, 1, 1, 0, 0, 0)
print(millenium_turn)


# The size of each step in days
day_delta = datetime.timedelta(days=1)

start_date = datetime.date.today()
end_date = start_date + 7*day_delta

for i in range((end_date - start_date).days):
    print(start_date + i*day_delta)
    
    
from datetime import datetime, timedelta
now = datetime.now()
then = datetime(2018, 1, 1)
delta = now-then
print(delta)

from datetime import datetime, timedelta
now = datetime.now()
then = datetime(2019, 5, 23)
delta = now-then
print(delta.days)
# 60
print(delta.seconds)
# 40826


from datetime import date, timedelta

current_date = date.today().isoformat()   
days_after = (date.today()+timedelta(days=30)).isoformat()  

print("\nCurrent Date: ",current_date)
print("30 days after current date : ",days_after)

from datetime import date, timedelta

current_date = date.today().isoformat()   
days_before = (date.today()-timedelta(days=30)).isoformat()

print("\nCurrent Date: ",current_date)
print("30 days before current date: ",days_before)

import time
from datetime import datetime
seconds_since_epoch=time.time()  #1469182681.709

utc_date=datetime.utcfromtimestamp(seconds_since_epoch)
print(utc_date)

import datetime

today = datetime.date.today()
print('Today:', today)

yesterday = today - datetime.timedelta(days=1)
print('Yesterday:', yesterday)

tomorrow = today + datetime.timedelta(days=1)
print('Tomorrow:', tomorrow)

print('Time between tomorrow and yesterday:', tomorrow - yesterday)



