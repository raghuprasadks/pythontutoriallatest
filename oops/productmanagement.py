# -*- coding: utf-8 -*-

class product():
    def __init__(self,code,name,price,qty):
        self.code = code
        self.name = name
        self.price = price
        self.qty = qty
        self.netamt = self.price * self.qty
  
    def display(self):
        print("Code : ",self.code,"name : ",self.name," price : ",self.price ," Quantity : ",self.qty, "net amout : ",self.netamt)
             
        
noOfProdu =int(input("How many products you want to create"))
productlist = []
for i in range(noOfProdu):
    code = input("Enter code")
    name = input("Enter name")
    price = float(input("enter price"))
    qty = int(input("Enter quantity"))
    prod = product(code,name,price,qty)
    productlist.append(prod)
    
# Display list of products    
for p in productlist:
    print(p.display())
        
# Display product having maximum price

maxpriceindex = 0
index = 0
maximumprice = 0
for p in productlist:
    if(p.price > maximumprice):
        maximumprice = p.price
        maxpriceindex = index
    index = index + 1
print("Maximum price ",maximumprice)
print(productlist[maxpriceindex].display() )

# To find the product
'''
for p in range (noOfProdu):
    if (p == maxpriceindex):
        productlist[p].display()

'''
# Maximum sold

maxQtySoldIndex = 0
index = 0
maxQtySold = 0
for p in productlist:
    if(p.qty > maxQtySold):
        maxQtySold = p.qty
        maxQtySoldIndex = index
    index = index + 1
print("Maximum qty sold ",maxQtySold)
print(productlist[maxQtySoldIndex].display() )


# Maximum net amount

maxNetAmtIndex = 0
index = 0
maxNetAmt = 0
for p in productlist:
    if(p.netamt > maxNetAmt):
        maxNetAmt = p.netamt
        maxNetAmtIndex = index
    index = index + 1
print("Maximum Net amount of the product  sold ",maxNetAmt)
print(productlist[maxNetAmtIndex].display() )



