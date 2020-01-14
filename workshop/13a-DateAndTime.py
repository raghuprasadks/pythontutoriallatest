# -*- coding: utf-8 -*-
'''
The epoch
The epoch is the point where the time starts.
The point is taken as the 0.0 hours of January 1st
of the current year.
For Unix,the epoch is 0.0 hours of January 1st 1970
It is possible to measure the time in seconds since
the epoch using time() function of 'time' module
'''

'''
Program 1 : A python program to measure the time in
seconds since the epoch
'''
import time
epoch = time.time()
print(epoch)


'''
Program 2 : A python program to get date and time
from the epoch time

tm_year - 4 digit year like 2019
tm_mon - range [1,12]
tm_mday - range [1,31]
tm_hour - range [0,23]
tm_min - range [0,59]
tm_sec - range [0,61] including leap seconds
tm_wday - range [0,6] Monday is 0
tm_yday - range [1,366]
tm_isdst - [0,1 or -1] 0 - no DST,1 - DST is ineffect
-1= not known
tm_zone timezone name
'''
import time
epoch = time.time()
t = time.localtime(epoch)

#Retrieve the date from the structure t
d = t.tm_mday
m = t.tm_mon
y = t.tm_year
print('Current date is: %d - %d - %d' %(d,m,y))

#Retrive the time from the strurcture t
h = t.tm_hour
m = t.tm_min
s = t.tm_sec

print('Current time is: %d : %d : %d' %(h,m,s))

'''
Program 3 : A python program to convert epoch time
into corresponding date and time

The current date and time as shown in our computer 
system can be known using the following
ctime() function of 'time' module
now() method of 'datetime' class of 'datetime' module
today() method of 'datetime' class of 'datetime' module
'''
import time
epoch = time.time()
t = time.ctime(epoch)
print('Current date and time ',t)

'''
Program 4 : A python program to know the current date
and time using ctime() function
'''

import time
t = time.ctime()
print('Current date and time is ',t)


'''
Program 5 : A python program to know the local date and time.

now () methods returns the object that contains date
and time information in any timezone.
By default the local time zone in india is IST 
if the timezone is not passed
'''

from datetime import *
now = datetime.now()
print('current date time ' ,now) 
print('Date now : {}/{}/{}'.format(now.day,now.month,now.year))
print('Time now : {}:{}:{}'.format(now.hour,now.minute,now.second))

'''
Program 6 : A python program to know today's date and time
'''

from datetime import *
# today() of timetime class gives date and time
tdm = datetime.today()
print("Today's date and time = ",tdm)

#today() of the date class gives the date only
td = date.today()
print("Today's date = ",td)


