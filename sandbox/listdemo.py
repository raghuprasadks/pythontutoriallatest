# -*- coding: utf-8 -*-
# List
players = ['Rohit Sharma','Mayank Agarwal','Virat Kohli']
print(players)
#Length
print(len(players))
#Looping through list
for p in players:
    print(p)
# Append
players.append('Rahane')
#index - Slicing
players[0]
players[2]

newlist = players[1:3]
print(newlist)
players.insert(2,'Jadeja') 

numbers = []
numbers.append(1)
numbers.append('One')
numbers.append(True)
print(numbers)
numbers[1] = 'Two'
numbers.pop()
conlist = players + numbers
data = [89,78,67,91,97,56,46,56,91]
max(data)
min(data)
sum(data)
avg = sum(data)/len(data)
print(avg)
data.pop(2)
data.count(56)

'''
1. Create a list of even numbers between 20 and 80
2. Find the maximum,minimum and sum of elements in the above list
3. Find whether a given number is prime or not
'''

start = int(input('Enter starting range'))
end = int(input('Enter ending range'))

evennumber = []
for n in range(start,end+1):
   if (n % 2 == 0):
       evennumber.append(n)
print(evennumber)


def evennumlist(start,end):
    evennumber = []
    for n in range(start,end+1):
        if (n % 2 == 0):
            evennumber.append(n)
    return evennumber

start = int(input('Enter starting range'))
end = int(input('Enter ending range'))
enumlist = evennumlist(start,end)
print(enumlist)

fivetables = []
for n in range (5,51,5):
    fivetables.append(n)
    
print(fivetables)


oddnumbers = []
for n in range (10,21):
    if (n%2 != 0):
        oddnumbers.append(n)
    
print(oddnumbers)







