# -*- coding: utf-8 -*-

import numpy as np
a = np.array([1,2,3])
print('single dimensional array',a)
'''
1 2 3
'''
print('type of ',type(a))

'''
1 2 3
4 5 6
'''
b = np.array([(1,2,3),(4,5,6)],dtype=float)
b.shape

c = np.array([[(1,2,3),(4,5,6)],[(7,8,9),(10,11,12)]])

np.zeros((3,4))
np.ones((4,2))

d = np.arange(10,25,5)
print(d)
np.linspace(0,2,10)
e=np.full((2,2),7)
print(e)
f=np.eye(2)
print(f)
g = np.random.random((2,2))
print(g)
h = np.empty((4,3))
print(h)
# Saving and loading on disk
np.save('my_array',a)
np.savez('array.npz',a,b)
np.load('my_array.npy')
np.load('array.npz')

# saving and loading text files
np.savetxt("myarray.txt",a,delimiter= " ")
np.loadtxt("myarray.txt")
#Data types
np.int64
np.float32
np.complex
np.bool
np.object
np.string_
np.unicode_
#inspecting your array
b.shape
len(b)
b.ndim
b.dtype
b.dtype.name
b.astype(int)
#asking for help
np.info(np.ndarray.dtype)

#Arithmetic operations
a =np.array([(2,4,6),(8,10,12)])
b = np.array([(1,3,5),(7,9,11)])
a+b
c = np.add(a,b)
print('result of addition ',c)
d = np.subtract(a,b)
print('result of subtraction ',d)
e=np.multiply(a,b)
print('result of multiplication ',e)

x = np.array([(10,4,12),(13,4,1)])
print(x)
y = x.sort()
print(y)
y = x.sort(axis=0)
print(y)
name ='raghu'
name.