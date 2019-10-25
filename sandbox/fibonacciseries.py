# -*- coding: utf-8 -*-


n=int(input('enter the number of terms'))
firstnum=0
secondnum=1
for i in range(2,n):
   thirdnumber=firstnum + secondnum
   print(thirdnumber)
   firstnum=secondnum
   secondnum=thirdnumber

