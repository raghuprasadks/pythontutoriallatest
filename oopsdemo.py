# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 20:13:41 2020

@author: Thinkpad
"""

class vehicle():
    '''
    Constructor
    + method overloading
    '''
    def __init__(self,make,model,color,price,ac=None):
        self.make = make
        self.model = model
        self.color = color
        self.price = price
        self.speed = 0
        if (ac):
            self.ac = ac
    
    def start(self):
        self.speed = 0
        print("Vehicle started : ",self.speed)
        
    def move (self):
        self.speed = self.speed + 5
        print("Vehicle moved : ",self.speed)
    
    def stop(self):
        self.speed = 0
        print("Vehicle stop : ",self.speed)
        
        
    def info(self):
        return "Vehicle ::Make ",self.make," Model : ",self.model,"color : ",self.color," price : ",self.price
        
'''
myvehicle =  vehicle("Hyundai","Aastha i10","Red",670000)
myvehicle.start()
myvehicle.move()
myvehicle.move()
print(myvehicle.info())
myvehicle.stop()
'''

     
class car(vehicle):
    
    '''
    Method overriding
    '''
    def move (self):
        self.speed = self.speed + 10
        print("Vehicle moved : ",self.speed)
        
myvehicle =  car("Hyundai","Aastha i10","Red",670000)
myvehicle.start()
myvehicle.move()
myvehicle.move()
print(myvehicle.info())
myvehicle.stop()


make=input("Enter make")
model=input("Enter model")
color=input("Enter color")
price=int(input("Enter price"))
ac = input("Enter ac")

mysecondvehicle =  car(make,model,color,price,ac)
mysecondvehicle.start()
mysecondvehicle.move()
mysecondvehicle.move()
print(mysecondvehicle.info())
mysecondvehicle.stop()







    