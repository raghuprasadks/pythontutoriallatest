# -*- coding: utf-8 -*-
import random
class Account():
    '''
    def openAccount(self,name,address,idproof):
        self.name = name
        self.address = address
        self.idproof = idproof
        self.accountno = random.randint(1000,9999)
        self.balance = 0
        return self.accountno
    '''
    
    #Constructure
    def __init__(self,name,address,idproof):
        self.name = name
        self.address = address
        self.idproof = idproof
        self.accountno = random.randint(1000,9999)
        self.balance = 0
        return self.accountno
        
        
    def deposit(self,actno,amt):
        self.balance = self.balance + amt
        return self.balance

    def withdraw(self,actno,amt):
        self.balance = self.balance - amt
        return self.balance

    def checkBalance(self,actno):
        return self.balance

'''
saiact = Account()
saiactno = saiact.openAccount('Sai Venkat','Bengaluru',393993)
print(saiactno)
'''
saiact = Account('Sai Venkat','Bengaluru',393993)
saiactno = saiact.accountno
print(saiactno)

bal = saiact.deposit(saiactno,10000)
print('Balance after first deposit',bal)

bal = saiact.deposit(saiactno,15000)
print('Balance after second',bal)

bal = saiact.withdraw(saiactno,5000)
print('Balance after withdraw',bal)

bal = saiact.checkBalance(saiactno)
print('Check balance ',bal)

naveenaact = Account()
navactno = saiact.openAccount('Naveena','Bengaluru',393999494)
print(navactno)

bal = saiact.deposit(navactno,23000)
print('Balance after initial deposit of naveena',bal)


