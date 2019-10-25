# -*- coding: utf-8 -*-
class Car():
    def __init__(self,make,model,color,price):
        self.make = make
        self.model = model
        self.color = color
        self.price = price
        self.speed = 0    
    def start(self):
        self.speed =0
        return self.speed =0
    def move(self):
        self.speed = self.speed + 5
        return self.speed = self.speed + 5
    def stop(self):
        self.speed = 0
        return self.speed = 0
    def info(self):
        return 'Info : Make ',self.make, ' Model ',self.model)
myCar = Car('Maruti','Swift','Red',650000)

myCar.info()
initialspeed = myCar.start()
print('Initial speed ',initialspeed)
myCar.move()
myCar.move()
myCar.stop()
    