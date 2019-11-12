# -*- coding: utf-8 -*-

'''
prime number

9

1 and 9

9 % 2 == 0
9 % 3 == 0 (not a prime number) 
'''
number = int(input("Enter a number"))
isPrime = True
for n in range(2,number):
    if (number % n == 0):
        isPrime = False
        break

if (isPrime):
    print (number, ' is prime ')
else:
    print (number, ' is not prime ')
    
