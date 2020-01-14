count1=eval(input('Enter count value:'))
print(count1+1)

count=input('Enter count value:')
print(count+1)

a=float('123.456')

bool(a)+True

bool(10)+False
bool('-20.0')
bool('hello')

class test():
    var1 = 10
    def testing(self):
        self._prote = 10
        self.__priv = 15
        print('say hello')

print(test.var1)
#print(test._prote)

test1 = test()
print('protected ',test1._prote)
print('private ',test1.__priv)
#print(test.testing())

class employee:
    def __init__(self, name, sal):
        self.__name=name  # private attribute 
        self._salary=sal # private attribute
e1=employee("Swati", 10000)
e1._salary

def test(t,l):
    l[0] = 10
    t = t +1

l =[1,2,3]
t = 3
test(t,l)
print('t ',t)
print('l ',l)


def testargs(x=10,y=12):
    x=x+5
    y = y+10
    print ('x : ',x, ' y : ',y)
    
x=3
y=4
testargs(x,y)

print('after function call' ,x,y)

lst1 = [2,3,4]
lst2 = [10,15,16]
lst2 = lst1
lst1[0] = 100
print('lst2 ',lst2)
del lst2
print('after deletion ',lst1)

    
# Python program to illustrate 
# *args for variable number of arguments 
def myFun(*argv):
    print('type of ',type(argv))
    for arg in argv:        
        print(arg) 
	
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks') 

# Python program to illustrate 
# *kargs for variable number of keyword arguments 

def myFun(**kwargs):
    print('type of ',type(kwargs))
    for key, value in kwargs.items(): 
        print("%s == %s" %(key, value)) 

# Driver code 
myFun(first ='Geeks', mid ='for', last='Geeks')	 

def keytypes(*argv,**kwargs):
    
    print('dicts ',type(kwargs))
    print('tup ',type(argv))
    
lst=5*[4]
print(lst)

lst = [2,3,4]
lst[4]

lst = [1,2,3,4,5,6]
lst[::-2]
