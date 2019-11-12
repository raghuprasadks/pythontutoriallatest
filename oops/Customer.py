# -*- coding: utf-8 -*-
class Customer():
    def __init__(self,name,age,aadhar=None):
        self.name = name
        self.age = age
        self.aadhar =aadhar
        if(aadhar != None):
            print('validation of Aadhar')
        else:
            print('no Aadhar')
        
    def display(self):
    	print('Name :',self.name,' Age : ',self.age,' Aadhar ',self.aadhar)   
customers = []
customer1 = Customer('raghu',40)
customers.append(customer1)
customer2 = Customer('rakesh',22)
customers.append(customer2)

customer3 = Customer('rakesh',22,9393939399)
customers.append(customer3)


print('Customers :name ',customers[0].name)
print('Customers :age ',customers[0].age)
print('Customer info',customers[0].display())
#for i,c in enumerate(customers):
for c in customers:
    #print('name ',  customers[i].name)
    #print('age ',  customers[i].age)
    print('name check ',  c.name)
    print('age check ',  c.age)
    print('Customer info',c.display())