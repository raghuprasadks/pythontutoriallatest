# -*- coding: utf-8 -*-
# Python 3.x code to demonstrate star pattern 

# Function to demonstrate printing pattern 
def pypart(n): 
	# outer loop to handle number of rows 
	# n in this case 
	for i in range(0, n): 
	
		# inner loop to handle number of columns 
		# values changing acc. to outer loop 
		for j in range(0, i+1): 
		
			# printing stars 
			print("* ",end="") 
	
		# ending line after each row 
		print("\r") 
# Driver Code 
n = 5
pypart(n) 

'''

def simpleinterest(p,r,t):
    return (p*r*t)/100

p = int(input("enter principal"))
intr = simpleinterest(p,6,1)
print(intr)

'''

n = int(input("enter no of rows"))
for i in range(0, n): 
    print(i)
	
# inner loop to handle number of columns 
# values changing acc. to outer loop 
    for j in range(0, i+1):
              		
        #printing stars 
    	print("* ",end="")
        #print(j)
	
    	# ending line after each row 
    print("\r")