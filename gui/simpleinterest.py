# Import tkinter 
'''
from tkinter import *
class SimpleInterest(): 

	def __init__(self):
		window = Tk()
		window.title("Simple Interest Calculator")
		Label(window, text = "Annual Interest Rate").grid(row = 1,column = 1, sticky = W) 
		Label(window, text = "Number of Years").grid(row = 2,column = 1, sticky = W) 
		Label(window, text = "Principal Amount").grid(row = 3,column = 1, sticky = W) 
		Label(window, text = "Simple Interest").grid(row = 4,column = 1, sticky = W)
        

	# compute the total payment. 
	def computePayment(self):
        p = float(self.principalAmountVar.get())
        r = float(self.annualInterestRateVar.get())
        t = int(self.numberOfYearsVar.get())
        
        i = (p*r*t)/100
				
		
		self.siVar.set(format(i, '10.2f')) 
		
	
# call the class to run the program. 
SimpleInterest() 
'''

from tkinter import *
class SimpleInterest():
    def __init__(self):
        window = Tk()
		window.title("Simple Interest Calculator")
		Label(window, text = "Annual Interest Rate").grid(row = 1,column = 1, sticky = W) 
		Label(window, text = "Number of Years").grid(row = 2,column = 1, sticky = W) 
		Label(window, text = "Principal Amount").grid(row = 3,column = 1, sticky = W) 
		Label(window, text = "Simple Interest").grid(row = 4,column = 1, sticky = W)
    
