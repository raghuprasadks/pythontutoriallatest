

'''
customer
name,mobile,email,address,zipcode

a. add a new customer
b. display/list customers
c. update address/customer
d. delete a customer 
e. search for a customer
'''

class Customer():
    
    def __init__(self,name,mobile,email,address,city,zipcode):
        self.name = name
        self.mobile = mobile
        self.email = email
        self.address = address
        self.city = city
        self.zipcode = zipcode
    
    def info(self):
        return "Customer: name ",self.name,"Address:  ",self.address

customerList = []
c1 = Customer('raghu',9845547471,'prasadraghuks@gmail.com','1094,MCECHS Layout','Bengaluru',560077)
customerList.append(c1)

c2 = Customer('rudresh',9845547472,'prasadrudreshks@gmail.com','1095,MCECHS Layout','Bengaluru',560077)
customerList.append(c2)

c3 = Customer('girish',9845547473,'girish@gmail.com','1096,MCECHS Layout','Bengaluru',560077)
customerList.append(c3)


for l in customerList:
    print(l.info())
    
email =input("Enter email id of the person to delete")

for l in customerList:
    if (l.email == email):
        customerList.remove(l)
        print('Customer having email {} is removed'.format(email))
    
for l in customerList:
    print(l.info())


'''
search
'''
name =input("Enter name of the person to search")
isMatched = False
for l in customerList:
    
    #print('existing cutomers ',l.name)
    if (l.name == name):
        isMatched = True
        print('matched  customer profiels',l.info())
 
if(not isMatched):
    print('no profiles matched  ')

'''
Update
'''
email =input("Enter email id of the person for updation")
address =input("Enter new address")

for l in customerList:
    if (l.email == email):
        l.address = address

for l in customerList:
    print(l.info())
        


