# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 15:01:28 2020

@author: Thinkpad
"""
'''
Dynamically create dictionary of department and employees
'''
deptlist = {}

nodept = int(input('enter number of department: '))

for i in range (nodept):
    DeptName = input("Enter Department Name: ")
    noofemp = int(input("No of employees in the department"))
    emplist = []
    for i in range(noofemp):
        EmpName = input("Enter Employee Name: ")
        emplist.append(EmpName)
    deptlist[DeptName] = emplist
print("Deparment and Employees details of Company: ",deptlist)

'''
{'mech': ['suresh', 'ashok', 'prasad'], 'cs': ['sundresh', 'asha', 'ramya', 'vani'], 'ec': ['ravi', 'rohan', 'samhita', 'rajesh', 'balaji']}
'''

'''
2. print department and employees
'''

for k,v in deptlist.items():
    print(k,' : ',v)
    
'''
mech ['suresh', 'ashok', 'prasad']
cs ['sundresh', 'asha', 'ramya', 'vani']
ec ['ravi', 'rohan', 'samhita', 'rajesh', 'balaji']
'''

'''
3. change the existing employee with new employee
Get the user input for the department, current employee name and 
new employee
'''
print("dept employees ",deptlist)
dept = input("Enter department")
newemp = input("Enter new employee")
oldemp = input("Enter old employee")

for deptele,emplst in deptlist.items():
    #print("dept : ", deptele, " emplst :",emplst)    
    if (deptele == dept):  
        for i in range (len(emplst)):            
            if (emplst[i]==oldemp):
                print('matched ')
                emplst[i] = newemp
                
print('Updated employee list ',deptlist)

'''
4. Delete an existing employee.
Input - dept and the employee
'''
print("dept list ",deptlist)
dept = input('enter department: ')
delemp = input('enter delete employee: ')

for deptele,dellst in deptlist.items():
    if (deptele == dept):
        for i in range (len(dellst)):
            if (dellst[i]==delemp):
                print("found employee ",dellst[i])
                dellst.remove(delemp)
                break

print('Updated employee list ',deptlist)

            
                
