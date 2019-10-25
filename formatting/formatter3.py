# -*- coding: utf-8 -*-

# Python program showing 
# a use of format() method 

# combining positional and keyword arguments 
print('Number one portal is {0}, {1}, and {other}.'
	.format('Geeks', 'For', other ='Geeks')) 

# using format() method with number 
print("Geeks :{0:2d}, Portal :{1:8.2f}". 
	format(12, 00.546)) 

# Changing positional argument 
print("Second argument: {1:3d}, first one: {0:7.2f}". 
	format(47.42, 11)) 

print("Geeks: {a:5d}, Portal: {p:8.2f}". 
	format(a = 453, p = 59.058)) 


