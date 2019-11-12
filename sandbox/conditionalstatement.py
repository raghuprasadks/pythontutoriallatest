# -*- coding: utf-8 -*-
name = input('Enter name')
print(name)
age = int(input('Enter age'))
print(age)
print(type(age))
amt = float(input('Enter amount'))
print(amt)
print(type(amt))
if (age >=18):
    print('You are eligible to vote')

if (age >=18):
    print('You are eligible to vote')
else:
    print('You are not elible to vote')

marks = int(input('Enter marks'))
if (marks > 90 and marks <=100):
    print('A+')
elif (marks > 80 and marks <=90):
    print('A')
elif (marks > 70 and marks <=80):
    print('B+')
else :
    print ('Below B+')
    