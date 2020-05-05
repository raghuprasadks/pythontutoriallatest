#with out expection handling
n = int(input('Enter a number to validate division by zero'))
div = 100/n
print('result is ',div)

d=int(input('Enter a number to validate zero division'))
try:
    a=100/d
    print(a)
except:
    print('Exception : Enter a positive number')
else:
    print('No exception')


d=input('Enter a number to validate zero division')
try:
    a=100/d
    print(a)
except Exception as e:
    print('Enter a number to validate zero division')
    print('Exception occured ',e.trace())
else:
    print('No exception')



d = int(input('Enter a number to validate division by zero'))
try:
    a=10/d
    print(a)
except ArithmeticError:
    print("This statement is raising an exception")
else:
    print("No exception proceed")

print ('after the exception')
#Except with no exception

try:
    a=10/'a'
    print(a)
except Exception as e:
    print("Exception : ",e)
else:
    print("Proceed no exception")

#Declaring multiple exception
try:
    #a=10/0
    a=10/'raghu'
    print(a)
#except ArithmeticError,NameError: - 3.6 does not support
except ZeroDivisionError:
    print("ZeroDivisionError")
except ArithmeticError:
    print("ArithmeticError")
except:
    
    print("Generic Error")
else:
    print("Successfully Done")
#Finally Block

try:
    #a=10/0;
    a=10/2;
    print(a)
except ZeroDivisionError:
    print(ZeroDivisionError)
finally:
    print("Finally block is always called")
a=2
print('value of a ',a)
try:
   a=10/0;
   a=10/2;
   print(a)
except ZeroDivisionError:
   print(ZeroDivisionError)
finally:
    #print(a)
    b=29/(a+2)
    print("Finally block is always called and the result is: ",b)


#Raise an exception

try:
    a=10
    print(a)
    raise NameError("Hello")
except NameError as e:
    print("An exception occured :",e)
    
#Custom exception
class ErrorInCode(Exception):
    def __init__(self,data):
     self.data = data
    def __str__(self):
        return repr('Error Code ' +str(self.data))
try:
    raise ErrorInCode(2000)
except ErrorInCode as ae:
#except ErrorInCode:
    print("Received error :",ErrorInCode)
    print("Received error :",ae)

class Student(object):
	def __init__(self, name, age, twitter_url=None, google_plus=None, youtube_channel=None):
		self.name = name
		self.age = age
		self.twitter_url = twitter_url
		self.google_plus = google_plus
 #       self.youtube_channel = youtube_channel

	def __str__(self):
		# Override to print a readable string presentation of your object
		# below is a dynamic way of doing this without explicity constructing the string manually
		return ', '.join(['{key}={value}'.format(key=key, value=self.__dict__.get(key)) for key in self.__dict__])

student = Student(name='Jone', age=23, twitter_url='http://twitter.com/jone')
print(student)

#class InvalidAge(object):
class InvalidAge(Exception):
    def __init__(self,data):
     self.data = data
    
    def __str__(self):
        #print('over riding str')
        #return repr('Invalid Age ' +str(self.data))
        return 'Invalid age '
    '''
    def __repr__(self):
        print('overriding repr')
    '''    
age = int(input ('Enter your age'))
if (age >= 18):
    print('you are eligible to vote')
else:
    print('you are not eligible to vote')
    raise InvalidAge(age) 
    
    
class InvalidMarks(Exception):
    def __init__(self,data):
     self.data = data
    def __str__(self):
        return repr('Invalid marks ' +str(self.data))
    
marks=int(input('Enter your marks '))
if(marks<0 or marks>100):
    print('Marks is invalid ')
    raise  InvalidMarks(marks)
else:
    print('Marks is valid')


class InsufficientBal(Exception):
    def __init__(self,actno,amt):
        self.actno = actno
        self.amt = amt
    def __str__(self):
        return repr('Insufficient balance ' +str(self.amt))
    
   
class Account():
    def __init__(self,actno,name,mobile,email,idproof):
        self.actno = actno
        self.actno=actno
        self.mobile = mobile
        self.email = email
        self.idproof = idproof
        self.balance = 0
        
    def deposit(self,actno,amt):   
        self.balance = self.balance + amt
        return self.balance
    
    def withdraw(self,actno,amt):
        if (amt > self.balance):
            raise InsufficientBal(actno,amt)
        else:
            self.balance = self.balance - amt
        return self.balance
    
myact = Account(101,'raghu',9845547471,'prasadraghuks@gmail.com','adhar')
bal = myact.deposit(101,30000)
try:
    bal = myact.withdraw(101,35000)
except Exception as e:
    print('exception ',e)

print('after initial deposit',bal)

# REPR
#https://www.journaldev.com/22460/python-str-repr-functions

class Person:
    name = ""
    age = 0

    def __init__(self, personName, personAge):
        self.name = personName
        self.age = personAge

p = Person('Pankaj', 34)

print(p.__str__())
print(p.__repr__())



class Person:
    name = ""
    age = 0

    def __init__(self, personName, personAge):
        self.name = personName
        self.age = personAge

   
    def __repr__(self):
        return '{name:'+self.name+', age:'+str(self.age)+ '}'

    '''
    def __str__(self):
        return 'Person(name='+self.name+', age='+str(self.age)+ ')'
    '''

p = Person('Pankaj', 34)

# __str__() example
print(p)
print(p.__str__())

s = str(p)
print(s)

# __repr__() example
print(p.__repr__())
print(type(p.__repr__()))
print(repr(p))

x = object()

print(dir(x))

'''
class calculator
add(n1,n2)
sub(n1,n2)
mul
div


write expection class to hangle folloing scenarios
if (n1 <0) then raise InvaidData
if (n1  or n2 is a charecter then raise InvalidDataFormat)
'''


#Calculator
n1= int (input ("Enter the value of number one"))
n2= int (input("Enter the value of number two"))

class Calculator():
    Add=0
    Sub=0
    Div=0
    Multi=0
    
try:
    Add=n1 + n2
    Sub=n1 - n2
    Div=n1/n2
    Multi=n1*n2


    
except (n1<0):
        print("Invalid data")
except (type(n1)==char or type(n2)==char):
        print ("Invalid data")
          
else:
    print ("Successfully done")
    print ("Addition is",Add)
    print ("Subtraction is",Sub)
    print ("Division is",Div)
    print ("Multiplication is",Multi)
    

class InvalidDataException(Exception):
    def __init__(self,data):
        self.data = data
        
    def __str__(self):
        return 'Invalid Data '

class Calculator():
    def add(self,n1,n2):
        if (n1 < 0 ):
            raise InvalidDataException(n1)