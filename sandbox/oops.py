class Calculator():
    def addition(self,num1,num2):
        return num1+ num2
    
    def subtraction(self,num1,num2):
        return num1- num2
    
    def multiplication(self,num1,num2):
        return num1- num2
    
    def division(self,num1,num2):
        return num1/ num2
#Instance 
calci = Calculator()
result = calci.addition(100,150)
print('Result of addition is ',result)

result = calci.multiplication(100,150)
print('Result of multiplication is ',result)

calci1 = Calculator()
result = calci1.addition(100,150)
print('Result of addition from calci 1 is ',result)

n2 = 100
def calculate():
    n1 = 10
    global n2
    n2 = 20
    print(n1)
    print(n2)

calculate()
print(n2)
