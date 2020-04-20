x = ['ab', 'cd']
for i in x:
    i.upper()
print(x)

name = 'python'
print(name.upper())


x = ['ab', 'cd']
index = 0
for i in x:
    upd = i.upper()
    x[index] = upd
    index = index + 1
print(x)

x = ['ab', 'cd']
for i in x:
    x.append(i.upper())
print(x)


i = 1
while True:
    print(i)
    i = i +1
    if (i == 10):
        break

start = 1
end = 10
while (start <=end):
    print(start)
    start = start +1

start = 1
end = 10
while (start <=end):
    if (i==5):
        continue
    print(start)
    start = start +1


    
start = 1
end = 10
while (end >=start):
    print(end)
    end = end - 1

for i in range(10):
    print(i)

for i in range (2,20,2):
    print(i)

for i in range (20,1,-2):
    print(i)
    
def evenOrOdd(num):
    if (num%2 ==0):
        print(num, ' is even number')
    else:
        print(num, ' is odd number ')

evenOrOdd(11)

def evenOrOdd(num):
    isEven = False
    if (num%2 ==0):
        isEven = True
    return isEven

checkEven = evenOrOdd(13)
if (checkEven):
    print('its even')
else:
    print('its odd')
    
def simpleInterest(p,r,t):
    i = (p*r*t)/100
    return i,p

inte,prin = simpleInterest(1000,6,1)
print('interest ',inte,' principal ',prin)


def add (n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2


total = add(100,40)
print('total ',total)
'''
ask user to enter two numbers
ask user to enter the operation (+,-,/,*)

functions
'''
n1 = int(input("Enter first number"))
n2 = int(input("Enter second number"))
oper = input("Enter operation (+,-,/,*)")

result = 0
if (oper=='+'):
    result = add(n1,n2)
elif (oper == '-'):

    
print(n1,' ',n2, ' ' , oper,' = ',result)