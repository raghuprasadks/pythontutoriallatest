# -*- coding: utf-8 -*-

# Operators - Single line comment
'''
multi line comment
line 2
line 3
'''
"""
This is also a comment
"""

# operators - Arithmetic, Relational, Logical
'''
and
or
not
'''

num1 = 10
num2 = 15
num3 = 8

result = (num1 < num2) and ( num3 < num2)
print (result)

# both operations should be true 
# in order to get true
result = (num1 > num2) and ( num3 < num2)
print (result)
#if any one of the operation is true
# in order to get true
result = (num1 > num2) or ( num3 < num2)
print (result)

# not

result = not (num1 < num2)
print (result)


 




