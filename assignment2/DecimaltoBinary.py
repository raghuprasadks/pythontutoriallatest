# -*- coding: utf-8 -*-]


def convertToBinary(n):
   # Function to print binary number for the input decimal using recursion
   
   if n > 1:
       
       convertToBinary(n//2)
   print(n)
   print('in loop')
   binary = (n%2)
   print(binary,end = '')

# decimal number
dec = 10

convertToBinary(dec)

sen1 = 'I love india india is a great country'
list1 = sen1.split()
newlist = []
for l in list1:
    print(newlist.count(l))
     
    if (newlist.count(l) >= 1):
         continue
    else:
         newlist.append(l)    

print(' '.join(newlist))

