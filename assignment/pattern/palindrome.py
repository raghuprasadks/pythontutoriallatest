# -*- coding: utf-8 -*-
# Python Program to Reverse a Number using While loop    
     
Number = int(input("Please Enter any Number: ")) 
originalnumber = Number
   
Reverse = 0    
while(Number > 0):    
    Reminder = Number %10    
    Reverse = (Reverse *10) + Reminder    
    Number = Number //10    
     
print("\n Reverse of entered number is = %d" %Reverse)  

if(originalnumber==Reverse):
    print(originalnumber,' is a palindrome')
else:
    print(originalnumber,' is not a palindrome')
 
