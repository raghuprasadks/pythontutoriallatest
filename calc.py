class calc():
    def add(self,num1,num2):
        return num1+num2
    def sub(self,a,b):
        return(a-b)
    def mul(self,a,b):
        return(a*b)
    def div(self,a,b):
        return(a/b)
        
calculator = calc()
result = calculator.add(10, 20)
print('Result of addition is ', result)
print(calculator.sub(10,20))
print(calculator.mul(10,20))
print(calculator.div(10,20))


