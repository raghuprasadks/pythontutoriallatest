# -*- coding: utf-8 -*-
# First python program

print('Hello. Welcome to python')

num1 = 100
num2 = 200
sum = num1 + num2
print('sum is ',sum)

'''
This is a multiline comment
Data types
'''
inttype = 10
floattype = 20.5
stringtype = 'CS department'
booleantypeTrue = True
booleantypeFalse = False
print(type(booleantypeTrue))
print(type(floattype))

# Arithmatic operators
# + - * / // %
num1 = 100
res = 100//3
print(res)
rem = num1%2
print(rem)
# Relational operators < > >= <= == !=
num2 = 20
num1 > num2
num1 = 20
num1 != num2
# logical opeartors and or not
num3 = 10
(num1 > num2) and (num1 > num3)
(num1 > num2) or (num1 > num3)
not (num1 > num2)

# single line comment

# double line comments
'''
this is line 1
this is line 2
this is line 3
'''

"""
this is multi line comment
this is multi line comment

"""

# valid variable A-Z, a-z, 0 -9 _
_name = 'test'
print(_name)
#invalid
$name = 'test'
print(_name)


# conditional statements

age = 17
if (age >=18):
    print('You are eligible to vote')

if (age >=18):
    print('You are eligible to vote')
else:
    print('You are not eligible to vote')
    
marks = 75

if (marks >=90):
    print('Grade is A+')
elif(marks >=80 and marks <89):
    print('Grade is A')    
else:
    print(' Lesser than A')
    
# User inputs
    
name = input ("Enter your name")
print(" your name is ", name)

age = int(input("Enter your age"))
print("Your age is ",age)
    
amt = float(input("Enter amount"))
print("Amount is ",amt)


name = input ("Enter your name").upper()
print(name)

# Loops

# while loop

start = 1
end = 10

while (start<=end):
    print(start)
    start = start + 1
    
#for loop
for i in range(1,11):
    print(i) 

#for loop
for i in range(11):
    print(i) 

#for loop
for i in range(2,21,2):
    print(i) 
    
#for loop
for i in range(10,0,-1):
    print(i) 

#for loop
for i in range(10,0):
    print(i) 
    
name = 'raghu'
for n in name:
    print(n) 
    
# functions

def greet():
    print('hello')

greet()

def greet(name):
    print('hello',name)
greet('raghu')

def simpleInterest(p,r,t):
    return p*r*t
si = simpleInterest(1000,6,1)
print(si)

def multiargs(* args):
    print(type(args))
    print(args)

multiargs(1,2)
multiargs(1,2,3,4,5)

    
    

    
    

    