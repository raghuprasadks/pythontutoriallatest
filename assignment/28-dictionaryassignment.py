# -*- coding: utf-8 -*-

result ={'ravi':90,'rajan':67,'ramya':98}

max = result['ravi']

print ('assumed max marks',max)
for name,marks in result.items():
    print (name,marks)
    if (marks > max):
        max = marks
print(max)

# Dynamically getting values
noOfStudents = int(input("enter number of students"))
result = {}
for i in range(noOfStudents):
    name = input('enter the student name')
    marks = int(input ('enter the marks'))
    result[name] = marks
print ('my dictionary ',result)
max = result['ravi']
print ('assumed max marks',max)
for name,marks in result.items():
    print (name,marks)
    if (marks > max):
        max = marks
print(max)



