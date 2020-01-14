# https://www.programiz.com/python-programming/args-and-kwargs

'''
Introduction to *args and **kwargs in Python
In Python, we can pass a variable number of arguments to a function using special symbols. There are two special symbols:

*args (Non Keyword Arguments)
**kwargs (Keyword Arguments)

'''

def adder(*num):
    print(type(num))
    sum = 0
    
    for n in num:
        sum = sum + n
    print("Sum:",sum)
adder(3,5)
adder(4,5,6,7)
adder(1,2,3,5,6)

'''
Python **kwargs
Python passes variable length non keyword argument to function using *args 
but we cannot use this to pass keyword argument. For this problem Python 
has got a solution called **kwargs, it allows us to pass the variable 
length of keyword arguments to the function.
'''
def intro(**data):
    print("\nData type of argument:",type(data))
    for key, value in data.items():
        print("{} is {}".format(key,value))
intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)

intro(lst=[1,2,3,4])
intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)

data = 1,2,3,4
print(type(data))