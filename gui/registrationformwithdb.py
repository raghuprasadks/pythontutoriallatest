import sqlite3
conn = sqlite3.connect('registrationnew.db')
print("Opened database successfully")
conn.execute('''CREATE TABLE REGISTRATIONS
         (NAME            TEXT      NOT NULL,
          EMAIL         TEXT     NOT NULL,
          MOBILE            INT    NOT NULL,
          PWD            TEXT    NOT NULL)''')
         
         
from tkinter import *
class Registration():
   def __init__(self):
       window = Tk()
       window.geometry('400x300')
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
       try:
           conn = sqlite3.connect('registrationnew.db')
           name=self.nameVar.get()
           email=self.emailVar.get()
           mobile =self.mobileVar.get()
           password = self.passwordVar.get()
           param = (name,email,mobile,password)
           #conn.execute("INSERT INTO REGISTRATIONS VALUES (?,?,?,?),(name,email,mobile,password)")                           
           
           sql = ''' INSERT INTO REGISTRATIONS VALUES (?,?,?,?) '''
           cur = conn.cursor()
           cur.execute(sql, param)
           
           conn.commit()
           
           self.nameVar.set('')
           self.emailVar.set('')
           self.mobileVar.set('')
           self.passwordVar.set('')
           self.conpasswordVar.set('')
           conn.close()
       except Exception as e:
            print("Exception ::",e)
            
        
       print('Saved to db')
       
             
reg=Registration()