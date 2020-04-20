from tkinter import *
class SimpleInterest():
    def __init__(self):
        window = Tk()
        window.geometry('400x300')
        window.title("Simple Interest Calculator")
        Label(window, text = "Annual Interest Rate").grid(row = 1,column = 1, sticky = W)
        Label(window, text = "Number of Years").grid(row = 2,column = 1, sticky = W)
        Label(window, text = "Principal Amount").grid(row = 3,column = 1, sticky = W)
        Label(window, text = "Simple Interest").grid(row = 4,column = 1, sticky = W)
        
        self.annualInterestRateVar = StringVar() 
        Entry(window, textvariable = self.annualInterestRateVar,justify = RIGHT).grid(row = 1, column = 2) 
        self.numberOfYearsVar = StringVar()
        Entry(window, textvariable = self.numberOfYearsVar,justify = RIGHT).grid(row = 2, column = 2)
        self.principalAmountVar=StringVar()
        Entry(window, textvariable = self.principalAmountVar,justify = RIGHT).grid(row = 3, column = 2)
        self.siVar = StringVar()
        lblSI = Label(window, textvariable =self.siVar).grid(row = 4,column = 2, sticky = E)
        btComputePayment = Button(window, text = "Compute SI",command = self.computePayment).grid(row = 6, column = 2, sticky = E)
        window.mainloop()
        
    def computePayment(self):
        p = float(self.principalAmountVar.get())
        r = float(self.annualInterestRateVar.get())
        t = int(self.numberOfYearsVar.get())
        i = (p*r*t)/100
        self.siVar.set(format(i, '10.2f')) 
si = SimpleInterest()