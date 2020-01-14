# -*- coding: utf-8 -*-


actlist = []

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

    def checkBalance(self,actno):
        print('in check balance')
        bal = 0
        for lst in actlist:
            for k,v in lst.items():
                if (k == actno):
                   bal = v.balance
        return bal
    
myact = Account(101,'raghu',9845547471,'prasadraghuks@gmail.com','adhar')
actlist.append({101:myact})
bal = myact.deposit(101,30000)
bal = myact.withdraw(101,5000)
bal = myact.checkBalance(101)
print('balance of 101 ', bal)


myact1 = Account(102,'ranga',9845547472,'prasadranga@gmail.com','adhar')
actlist.append({102:myact1})
bal = myact1.deposit(102,30000)
bal = myact1.withdraw(102,8000)
bal = myact1.checkBalance(102)
print('balance of 102 ', bal)

#print(actlist)
