#Class
class myClass():    
    def method1(self):
        print("myClass:method1")
    def method2(self, name):
        print("myClass:method2:Name " , name)
    '''
    def method3():
        print('without self',name)
    '''

mycls = myClass()
mycls.method1()
mycls.method2("Python")

mycls1 = myClass()
mycls1.method1()
mycls1.method2("Machine Learning")

def main1():
    # exercise the class methods
    c = myClass()
    c.method1()
    c.method2("Python")
    
    c1 = myClass()
    c1.method1()
    c1.method2("Machine Learning")
if (__name__ == "__main__"):
    main1()
    
class student():
    def register(self,regno,name,standard,section):        
        self.regno = regno
        self.name = name
        self.standard = standard
        self.section = section
        
    def information(self):
        print('Regno ',self.regno,' Name ',self.name,' Standard ',self.standard,' Section ',self.section)
        
bhavikaa = student()
bhavikaa.register(101,'Bhavikaa','9','A')
bhavikaa.information()
shloka = student()
shloka.register(102,'Shloka','9','C')
shloka.information()

print('Enter student information')
regno = int(input('Enter Registration Number'))
name = input('Enter your name')
std = int(input('Enter your standard'))
sec = input ('Enter your section')
newstd = student()
newstd.register(regno,name,std,sec)
newstd.information()
   
class Animal:
    def eat(self):
        print('Eating')
        
class Dog(Animal):
    def bark(self):
        print('Barking')
d= Dog()
d.eat()
d.bark()
#Multi level
class Animal:
    def eat(self):
        print('Eating')
class Dog(Animal):
    def bark(self):
        print('Barking')
class BabyDog(Dog):
    def weep(self):
        print('Weeping ')
d= BabyDog()
d.eat()
d.bark()
d.weep()

'''
Method overriding - polymorphism
'''

#Inheritance
class myClass():
    def method1(self):
        print("Parent:method1")
    def method2(self, name):
        print("Parent Method 2 :",name)
    def method3(self,city):
        print ("You are from ", city)
#class childClass():
class childClass(myClass):
    '''
    overriding
    '''
    def method1(self):
        #myClass.method1(self)
        print("ChildClass:method1")
    def method2(self):
        print("childClass:method2")
def main():
    # exercise the class methods
    c2 = childClass()
    c2.method1()
    c2.method2()
    c2.method3("Bengaluru")
if (__name__ == "__main__"):
    main()
    
    
    
class Bank():
   def __init__(self,name,address,noOfBranch):
       print('init of bank')
       self.name = name
       self.address = address
       self.noOfBranch = noOfBranch
       print ('bank details :name ',self.name,' address : ',self.address,' no of branches ',self.noOfBranch )
   def Bank(self):
       print('tesing')
       
   def rateOfInterest(self):
       return 0
   
   def calculateInterest(self,p,r,t):
       return p*r*t/100

class SBI(Bank):
       
   def rateOfInterest(self):
       print('interest rate of sbi')
       return 6

class Karnataka(Bank):
    def __init__(self,name,address,noOfBranch):
        print('init of Karnataka')
        Bank.__init__(self,name,address,noOfBranch)
       
    def rateOfInterest(self):
        print('interest rate of Karnataka')
        return 6.5

sbi = SBI('State Bank of India','Nariman point,Mumbai',1000)
roi = sbi.rateOfInterest()
interest =sbi.calculateInterest(100000,roi,1)
print('interest from sbi is ',interest)
 
kar = Karnataka('Karnataka Bank','Nehru Road,Mangaluru',1003)
roi = kar.rateOfInterest()
interest =kar.calculateInterest(100000,roi,1)
print('interest from karnataka bank is ',interest)

bnk = Bank('RBI','Delhi',10)
bnk.Bank()
'''
Method overloading
'''
class drawing():
    def __init__(self,colorPainting,pencilShading=None,caricature=None):
        self.colorPainting = colorPainting
        self.pencilShading = pencilShading
        self.caricature = caricature
        if (self.colorPainting):
            print('You have drawn a color painting')
        if (self.pencilShading):
            print('You have drawn a pencil shading')
        if (self.caricature):
            print('You have drawn a caricature')
            
draw = drawing('Gandhi painting')

drawnshade = drawing('Gandhi painting','pencil shading')

drawnshadecari = drawing('Gandhi painting','pencil shading','Caricature')

class vehicle():
    def buyVehicle(self,make,model,fueltype,price,speed):
        self.make=make
        self.model=model
        self.fueltype=fueltype
        self.price=price
        self.speed=speed
    def start(self):
        #self.speed=int(self.speed)+0
        self.speed = 0
    def accelerate(self):
        self.speed=self.speed+10
    def stop(self):
        self.speed=0
    def information(self):
        print('make ',self.make,' model ',self.model,' fueltype ',self.fueltype,' price ',self.price,' speed ',self.speed)
veh1=vehicle()
veh1.buyVehicle('honda','city','petrol',100000,0)
veh1.start()
veh1.accelerate()
veh1.information()
veh1.accelerate()
veh1.information()
veh1.stop()
veh1.information()


class Scooter (vehicle):
    '''
    Method overriding
    '''
    def start(self):
        #self.speed=int(self.speed)+0
        print('Button start')
        self.speed = 0

myScooter = Scooter("Hero","plesure",'petrol',65000,0) 
myScooter.start() 
    
'''
class Coaching
constructor - name, type,address,city,zipcode,mobile,email,

method called coach()
	no implementation
info()

'''

class Coaching():
    def __init__(self,name, typec,address,city,zipcode,mobile,email):
        self.name = name
        self.typec = typec
        self.address = address
        self.city = city
        self.zipcode = zipcode
    def coach(self):
        pass
    def info(self):
        print('info beging called ')
        return 'Name : ',self.name, 'Coaching Type :',self.typec
'''
class music - inherits from coaching
method called coach()
'Learing music'
'''
class Music(Coaching):
    def coach(self):
        print('Learning Music')
    
'''
class instrument - inherits from coaching

additional parameter in the constructor which is instrument

method called coach()
'coaching with ',instrument

overding info()
is is printing the instument along with other details

'''
class Instrument(Coaching):
    def __init__(self,name, typec,address,city,zipcode,mobile,email,instrument):
        Coaching.__init__(self,name, typec,address,city,zipcode,mobile,email)
        self.instrument = instrument
    def coach(self):
        print('Coaching with ',self.instrument)
    def info(self):
        self.infofromparent = Coaching.info(self)
        self.info = self.infofromparent,' Instrument : ',self.instrument
        return self.info
    
mymusiccls = Music('Raghu ', 'Karnatic','1094,Indushankara','Bengaluru',560077,9008663619,'prasadraghuks@gmail.com')

mymusiccls.coach()
myclsinfo = mymusiccls.info()  
print('info about my music class',myclsinfo) 

myinstrumentcls = Instrument('Raghu ', 'Karnatic','1094,Indushankara','Bengaluru',560077,9008663619,'prasadraghuks@gmail.com','violin')

myinstrumentcls.coach()
myinstinfo = myinstrumentcls.info()  
print('info about my instrument class',myinstinfo) 
    
'''
static method
'''    
class calculator():
    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2  
    def add(self):
        return self.n1+ self.n2    
    @staticmethod
    def sub(n1,n2):
        return n1 - n2
    
    
calci = calculator(100,50)
print('add : ',calci.add())
print('subtract ',calculator.sub(100,30))
    
    
    
    
    
    
    
    
    
    