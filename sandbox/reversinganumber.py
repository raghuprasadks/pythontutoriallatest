# -*- coding: utf-8 -*-

number = int(input("Enter a number"))
original = number
reverse = 0
while (number > 0):
    rem = number % 10
    reverse = reverse * 10 + rem
    number = number // 10

if (reverse == original):
    print (original, ' is a palindrome ')
else:    
    print (original, ' is not palindrome ')
    
    
'''
continue
break
'''
    
   
for i in range(10):
    if (i == 5):
        break
    print (i)

for i in range(10):
    if (i == 5):
        continue
    print (i)

    

