# -*- coding: utf-8 -*-

# Python program to 
# show format () is 
# used in dictionary 

tab = {'geeks': 4127, 'for': 4098, 'geek': 8637678} 

# using format() in dictionary 
print('Geeks: {0[geeks]:d}; For: {0[for]:d}; '
	'Geeks: {0[geek]:d}'.format(tab)) 

data = dict(fun ="GeeksForGeeks", adj ="Portal") 

# using format() in dictionary 
print("I love {fun} computer {adj}".format(**data)) 


