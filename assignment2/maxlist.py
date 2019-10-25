data=[2,4,1,47,38]
for i in range(0,len(data)):
    for j in range(i+1,len(data)):
        if(data[i]>data[j]):
            max=data[i]
        else:
            max=data[j]
print("Maximum element is",max)

list = [2,4,1,47,38]
m = list[0]
for num in list:
    if num > m:
        m = num
        
print('Maximum number =',m)

list=[2,4,1,47,38]
list.sort()
print("Max:",list[-1])
print("Min:",list[0])

total=0
for i in range(0,len(list)):
    total+=list[i]
avg=total/len(list)
print('The average is ',avg)

data=[20,45,7,3]
flag=0
value=int(input('Enter the search element'))
for i in data:
    print(i)
    if(value==i):
        flag=1
    else:
        flag=0
if(flag==1):
    print('Found')
elif(flag==0):
    print('Not found')
    
    
data=[2,4,1,47,38]
ele=int(input("Enter element to be searched"))
exits = False
for i in data:
    if i==ele:
        exists = True
    
if(exists):
    print("Exist")
else:
    print("Does not Exist")
        