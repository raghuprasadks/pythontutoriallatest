from tkinter import *
class Registration():
    def __init__(self):
       window = Tk()
       window.geometry('500x300')
       window.title("Registration form")
       Label(window, text = "Name").grid(row = 1,column = 1, sticky = W)
       Label(window, text = "Email address").grid(row = 2,column = 1, sticky = W)
       Label(window, text = "Mobile number").grid(row = 3,column = 1, sticky = W)
       Label(window, text = "Password").grid(row = 4,column = 1, sticky = W)
       Label(window, text = "Confirm Password").grid(row = 5,column = 1, sticky = W)
       self.nameVar = StringVar()
       Entry(window, textvariable = self.nameVar,justify = LEFT).grid(row = 1, column = 2)
       self.emailVar = StringVar()
       Entry(window, textvariable = self.emailVar,justify = LEFT).grid(row = 2, column = 2)
       self.mobileVar=StringVar()
       Entry(window, textvariable = self.mobileVar,justify = LEFT).grid(row = 3, column = 2)
       self.passwordVar=StringVar()
       Entry(window, textvariable = self.passwordVar,justify = LEFT).grid(row = 4, column = 2)
       self.conpasswordVar=StringVar()
       Entry(window, textvariable = self.conpasswordVar,justify = LEFT).grid(row = 5, column = 2)
       btSubmit = Button(window, text = "Submit",command = self.Save).grid(row = 6, column = 2, sticky = E)
       window.mainloop()
       
    def Save(self):
        message = "Thanks for registering with us \n Name : ",self.nameVar.get()," Email : ",self.emailVar.get()
        messagebox.showinfo('Registration',message)
      
       #window.mainloop()
      
reg=Registration()