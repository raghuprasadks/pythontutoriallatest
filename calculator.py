class Calculator():
    def add(self,n1,n2):
        return n1+n2

    def subtract(self,n1,n2):
        return n1 - n2

calci = Calculator()
result = calci.add(100,50)
print('Calci : add',result)
result = calci.subtract(100,50)
print('Calci : subtract',result)

    