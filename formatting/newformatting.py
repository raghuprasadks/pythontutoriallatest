# -*- coding: utf-8 -*-

#https://pyformat.info/

#old
'%s %s' % ('one', 'two')

#new
'{} {}'.format('one', 'two')

#old
'%d %d' % (1, 2)

#New
'{} {}'.format(1, 2)

#Padding and aligning strings

#Align right:

#Old
'%10s' % ('test',)
#New
'{:>10}'.format('test')

#Align left:

#Old
'%-10s' % ('test',)
#New
'{:10}'.format('test')


#New
'{:_<10}'.format('test')
#center allignment
#New
'{:^10}'.format('test')

#This operation is not available with old-style formating

#New
'{:^6}'.format('zip')

#Truncating long strings
#Old
'%.5s' % ('xylophone',)
#New
'{:.5}'.format('xylophone')

'{:.5}'.format('9898989')

#Combining truncating and padding
#Old
'%-10.5s' % ('xylophone',)
#New
'{:10.5}'.format('xylophone')

#numbers
#Of course it is also possible to format numbers.

#Integers:
#Old
'%d' % (42,)
#New
'{:d}'.format(42)


#Floats:
#Old
'%f' % (3.141592653589793,)
#New
'{:f}'.format(3.141592653589793)

#Padding numbers
#Similar to strings numbers can also be constrained to a specific width.

#Old
'%4d' % (42,)
#New
'{:4d}'.format(42)

#Signed numbers
#By default only negative numbers are prefixed with a sign. This can be changed of course.

#Old
'%+d' % (42,)
#New
'{:+d}'.format(42)

#Use a space character to indicate that negative numbers should be prefixed with a minus symbol and a leading space should be used for positive ones.

#Old
'% d' % ((- 23),)
#New
'{: d}'.format((- 23))

#Old
'% d' % (42,)
#New
'{: d}'.format(42)

#New style formatting is also able to control the position of the sign symbol relative to the padding.

#This operation is not available with old-style formatting.

#New
'{:=5d}'.format((- 23))

#New
'{:=+5d}'.format(23)

#Named placeholders
#Both formatting styles support named placeholders.

#Setup
data = {'first': 'Hodor', 'last': 'Hodor!'}
#Old
'%(first)s %(last)s' % data
#New
'{first} {last}'.format(**data)

#.format() also accepts keyword arguments.

#This operation is not available with old-style formatting.

#New
'{first} {last}'.format(first='Hodor', last='Hodor!')

#Getitem and Getattr
#New style formatting allows even greater flexibility in accessing nested data structures.

#it supports accessing containers that support __getitem__ like for example dictionaries and lists:

#This operation is not available with old-style formatting.

#Setup
person = {'first': 'Jean-Luc', 'last': 'Picard'}
#New
'{p[first]} {p[last]}'.format(p=person)


#Setup
data = [4, 8, 15, 16, 23, 42]
#New
'{d[4]} {d[5]}'.format(d=data)

#This operation is not available with old-style formatting.

#Setup
class Plant(object):
    type = 'tree'
#New
'{p.type}'.format(p=Plant())

#Both type of access can be freely mixed and arbitrarily nested:

#This operation is not available with old-style formatting.

#Setup
class Plant(object):
    type = 'tree'
    kinds = [{'name': 'oak'}, {'name': 'maple'}]
#New
'{p.type}: {p.kinds[1][name]}'.format(p=Plant())

#DateTime
#Setup
from datetime import datetime
#New
'{:%Y-%m-%d %H:%M}'.format(datetime(2001, 2, 3, 4, 5))

#Parameterised format
#Parametrized alignment and width:

#This operation is not available with old-style formatting.

#New
'{:{align}{width}}'.format('test', align='^', width='10')

  
#Parametrized precision:

#Old
'%.*s = %.*f' % (3, 'Gibberish', 3, 2.7182)
#New
'{:.{prec}} = {:.{prec}f}'.format('Gibberish', 2.7182, prec=3)


#Width and precision:
#Old
'%*.*f' % (5, 2, 2.7182)
#New
'{:{width}.{prec}f}'.format(2.7182, width=5, prec=2)
#The nested format can be used to replace any part of the format spec, so the precision example above could be rewritten as:

#This operation is not available with old-style formatting.

#New
'{:{prec}} = {:{prec}}'.format('Gibberish', 2.7182, prec='.3')

#The components of a date-time can be set separately:

#This operation is not available with old-style formatting.

#Setup
from datetime import datetime
dt = datetime(2001, 2, 3, 4, 5)
#New
'{:{dfmt} {tfmt}}'.format(dt, dfmt='%Y-%m-%d', tfmt='%H:%M')

#The nested formats can be positional arguments. Position depends on the order of the opening curly braces:

#This operation is not available with old-style formatting.

#New
'{:{}{}{}.{}}'.format(2.7182818284, '>', '+', 10, 3)

#And of course keyword arguments can be added to the mix as before:

#This operation is not available with old-style formatting.

#New
'{:{}{sign}{}.{}}'.format(2.7182818284, '>', 10, 3, sign='+')

#Custom objects
#The datetime example works through the use of the __format__() magic method. You can define custom format handling in your own objects by overriding this method. This gives you complete control over the format syntax used.

#This operation is not available with old-style formatting.

#Setup
class HAL9000(object):

    def __format__(self, format):
        if (format == 'open-the-pod-bay-doors'):
            return "I'm afraid I can't do that."
        return 'HAL 9000'
#New
'{:open-the-pod-bay-door}'.format(HAL9000())