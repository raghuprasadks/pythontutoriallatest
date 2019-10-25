# Python Program to Reverse a Number using While loop    
     
Number = int(input("Please Enter any Number: "))  
originalno = Number  
Reverse = 0    
while(Number > 0):    
    Reminder = Number %10    
    Reverse = (Reverse *10) + Reminder    
    Number = Number //10    
     
print("\n Reverse of entered number is = %d" %Reverse) # -*- coding: utf-8 -*-

if (originalno == Reverse):
    print('its a palindrome')
else:
    print('its not a palindrome')
'''
Number = 123

1st time loop

Remainder = 123%10 = 3
Reverse = (0*10) + 3
Number = 123//10 = 12


2nd loop
12 >0

Remainder = 12%10 = 2

Reverse = 3*10+2 = 32
Number = 12//10 = 1
3nd loop
1>0

remainder = 1%10 = 1
Reverse = 32*10 + 1

'''