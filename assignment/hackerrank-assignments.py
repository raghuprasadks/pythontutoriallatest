# -*- coding: utf-8 -*-

n = list(input())

for i in range(0,len(n)):
    n[i] = int(n[i])
    
print(type(n[0]))

y = max(n)

x = n.count(y)
print(x)

for p in range(x):
    if( n.count(y)>=1):
        n.remove(max(n))
    else:
        print(max(n))
    
print(max(n))


data = eval(input("enter a list"))

data = [1,2,3,5,6,6,3]
data.sort(reverse=True)
print("sorted ",data)
secondmax = data[1]
print("second max ",secondmax)











