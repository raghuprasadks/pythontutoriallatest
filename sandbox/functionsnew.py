# -*- coding: utf-8 -*-
def greet():
    print('Hello')
    print('Welcome to python')
greet() 
def greet(name):
    print ('hello ',name)
print('another line')
greet('ravi')
def evenOrodd(num):
    result = (num % 2 == 0)
    return result
result = evenOrodd(5)
print (result)
def multivalue(num):
    result = (num % 2 == 0)
    return num,result
num,result = multivalue(9)
print (num, ' is even ',result )