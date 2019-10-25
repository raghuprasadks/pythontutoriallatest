# -*- coding: utf-8 -*-

fruits = ['Banana','Mango','Apple','Guava']
print(type(fruits))
print(fruits[2])
subsetFruits = fruits[1:3]
print('subset ',subsetFruits)

print('Guava from negative index ',fruits[-1])

for i in fruits:
    print(i)

print('length of fruits',len(fruits))
l = len(fruits)
i = 0;
while (i<l):
    print(fruits[i])
    i = i +1

fruits.append('papaya')
print('after adding', fruits)

fruits.pop()
print('after pop', fruits)

fruits.pop(0)
print('after pop', fruits)

list=[13,9,6,17,8]
largest=list[0]
i=1
while(i<len(list)):
    if(largest<list[i]):
        largest=list[i]
    i=i+1
print("largest is",largest)





