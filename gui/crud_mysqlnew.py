# Import tkinter 
from tkinter import *
import pymysql
class SimpleCRUD:
    def __init__(self):
        window = Tk()
        window.title("Simple CRUD")
        Label(window, text = "Full Name").grid(row = 1,column = 1, sticky = W)
        Label(window, text = "Mobile Number").grid(row = 2,column = 1, sticky = W)
        Label(window, text = "Email").grid(row = 3,column = 1, sticky = W)
        self.fullNameVar = StringVar()
        Entry(window, textvariable = self.fullNameVar,justify = RIGHT).grid(row = 1, column = 2)
        self.mobileVar = StringVar()
        Entry(window, textvariable = self.mobileVar,justify = RIGHT).grid(row = 2, column = 2)
        self.emailVar = StringVar()
        Entry(window, textvariable = self.emailVar,justify = RIGHT).grid(row = 3, column = 2)
        btInsert = Button(window, text = "Insert",command = self.insert).grid(row = 6, column = 2, sticky = E)
        window.mainloop()
        
    def insert(self): 
        print('inside insert')
        fullname = self.fullNameVar.get()
        email = self.emailVar.get()
        mobile = int(self.mobileVar.get())       
        
        # Open database connection
        db = pymysql.connect("localhost","internuser","123","pythoninterndb")
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        # Prepare SQL query to INSERT a record into the database.
        sql = "INSERT INTO phonedirectory(FULLNAME,EMAIL, MOBILE)    VALUES ('%s', '%s', '%d' )" %(fullname, email, mobile)
        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Commit your changes in the database
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback()
            # disconnect from server
            db.close()# -*- coding: utf-8 -*-
         

# call the class to run the program. 
SimpleCRUD() 
