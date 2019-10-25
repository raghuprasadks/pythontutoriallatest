# -*- coding: utf-8 -*-

n=int(input("Enter a number:"))
tot=0
while(n>0):
    dig=n%10
    print('step 1 : modulus ',dig)
    tot=tot+dig
    print('step 2 : total ',tot)    
    n=n//10
    print('step 3 : division ',n)
    
print("The total sum of digits is:",tot)

