# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 15:15:11 2020

@author: Thinkpad
"""
import sqlite3

class Account():
    acctno = 0
    name = ''
    email = ''
    mobile = ''
    address = ''
    city = ''
    balance = 0
        
  
    def openAccount(self,name,email,mobile,address,city):
        connection = sqlite3.connect ("account.db")
        print('open account ')
        self.acctno = 0
        self.name = name
        self.email = email
        self.mobile = mobile
        self.address = address
        self.city = city
        self.balance = 0
             
        try:      
            sql ="insert into accountnew(name,email,mobile,address,city,balance) values ('%s','%s','%s','%s','%s','%d')"  %(self.name,self.email,self.mobile,self.address,self.city,self.balance)
            print(sql)
            cur = connection.cursor()
            cur.execute(sql)
            print('account created successfully')
            connection.commit()
            print("last row id ",cur.lastrowid)
            self.acctno = cur.lastrowid
        except Exception as e:
            print('Exception occured ',e)
            connection.rollback()
        finally:
            connection.close()
        return self.acctno

    def deposit(self,actno,amount):
        connection = sqlite3.connect ("account.db")
        cur = connection.cursor()
                
        try:
            sql = "update accountnew set balance =balance + ?  where actnum=?"
            param = (amount,actno)
            print('update sql ',sql)
            cur.execute(sql,param)
            connection.commit()
            
            self.balance = self.checkBalance(actno)
            print('Balance after deposit : ',self.balance)
        except Exception as e:
            print('Exception :deposit ',e)
            connection.rollback()
        finally:
            connection.close()
        return self.balance
    
   
    def withdraw(self,acctno,amount):
        connection=sqlite3.connect ("account.db")
        cur=connection.cursor()        
        
        try:
            sql = "update accountnew set balance =balance - ?  where actnum=?"
            param = (amount,acctno)
            print('withdraw sql ',sql)
            cur.execute(sql,param)
            connection.commit()
            self.balance = self.checkBalance(acctno)
            print('Balance after withdraw : ',self.balance)
            
        except Exception as e:
            print('Exception :deposit ',e)
            connection.rollback()
        finally:
            connection.close()
        return self.balance
     
    def checkBalance(self,acctNo):  
        connection = sqlite3.connect('account.db')
        cur=connection.cursor()
        sql = "select balance from accountnew where actnum=?"
        param=(acctNo,) 
        print('checkBalance sql ',sql)
        result = cur.execute(sql,param)
        for row in result:
            print("BALANCE = ", row[0])
            self.balance = row[0]
            print("YOUR ACCOUNT BALANCE IS ",self.balance)
        return self.balance

act = Account()
'''
actno1  = act.openAccount('Karthik','Karthik@gmail.com','9845547476','Udaya ravi','Mysuru')
print('account number ',actno1)

actno2  = act.openAccount('Yatharth','Yatharth@gmail.com','9845547477','Gangadhar','Kanpur')
print('account number ',actno2)


bal1  = act.deposit(actno1,20000)
bal1  = act.deposit(actno1,10000)

print(' balance : ',bal1)

bal = act.withdraw(1,500)
print('Balance after withdraw :Act no 1 ',bal)
bal = act.checkBalance(1)
print('Check balance:Act no 1 ',bal)

'''
actno1  = act.openAccount('Sathwik','sathwik@gmail.com','9845547477','Udaya ravi','Shimoga')
print('account number ',actno1)

bal = act.deposit(actno1,20000)
print('Balance after first deposit :',bal)
bal  = act.deposit(actno1,10000)
print('Balance after second deposit :',bal)

bal  = act.checkBalance(actno1)
print('Check Balance  :',bal)

bal  = act.withdraw(actno1,5000)
print('Balance after withdraw :',bal)








