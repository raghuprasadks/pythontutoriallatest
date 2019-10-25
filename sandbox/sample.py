# -*- coding: utf-8 -*-

for i in range(10):
    #print(i)
    print(i,end=' ')
    
    
n1 = int(input("Enter a number "))
n2 = int(input("Enter another number "))

temp = n1
n1 = n2
n2 = temp

print(n1,n2)