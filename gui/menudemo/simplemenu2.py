'''
https://www.geeksforgeeks.org/python-gui-tkinter/
'''
from tkinter import *
	
root = Tk() 
root.geometry('400x600') 
e1=''
e2=''
e3=''
f1=Frame(root,height=300, width = 300)
f = Frame(root,height=300, width = 300)

def showCustomer():
    global f
    f1.pack_forget()
    f = Frame(root,height=300, width = 300)
        #self.f.propagate(0)
    f.pack()
        
        # labels
    l1 = Label(f,text='Principal')
    l2 = Label(f,text='Rate')
    l3 = Label(f,text='Time')
        
    l1.place(x=50,y=100)
    l2.place(x=50,y=150)
    l3.place(x=50,y=250)
        
    #Entry for user name
    global e1        
    e1 = Entry(f,width = 25,fg='blue',bg='yellow',font=('Arial',14))
    
    global e2    
    e2 = Entry(f,width = 25,fg='blue',bg='yellow',font=('Arial',14))
    global e3    
    e3 = Entry(f,width = 25,fg='blue',bg='yellow',font=('Arial',14))
        
    e1.place(x=150,y=100)
    e2.place(x=150,y=150)
    e3.place(x=150,y=250)
    e3.bind("<Return>",display)
    
    
def display(event):
        str1 = e1.get()
        str2 = e2.get()
        str3 = e3.get()
        interest = float(str1)*float(str2)*float(str3)/100
        strinterest = str(interest)
        # display the values uisng labels
        lbl1 = Label(text='Interest is : '+strinterest).place(x=150,y=200)
    
    
    
    
def showProduct():
    global f1
    f.pack_forget()
    f1 = Frame(root,height=300, width = 300)
        #self.f.propagate(0)
    f1.pack()
    
        
        # labels
    l1 = Label(f1,text='Principal-product')
    l2 = Label(f1,text='Rate')
    l3 = Label(f1,text='Time')
        
    l1.place(x=50,y=100)
    l2.place(x=50,y=150)
    l3.place(x=50,y=250)
    
    

menu = Menu(root) 
root.config(menu=menu) 
filemenu = Menu(menu) 
menu.add_cascade(label='File', menu=filemenu) 
filemenu.add_command(label='Customer',command=showCustomer) 
filemenu.add_command(label='Product',command=showProduct) 
filemenu.add_separator() 
filemenu.add_command(label='Exit', command=root.quit) 
helpmenu = Menu(menu) 
menu.add_cascade(label='Help', menu=helpmenu) 
helpmenu.add_command(label='About') 
mainloop()

    
    
