# -*- coding: utf-8 -*-

import pymysql
# Open database connection
db = pymysql.connect("localhost","pythonuser","password","pythondb")
# prepare a cursor object using cursor() method
cursor = db.cursor()

records_to_insert = [('Raghu','Prasad',45,'M', 10000) ,
                         ('Ramya','Prasad',40,'F', 12000),
                         ('Vikas','Ram',24,'M', 12600) ]

# Prepare SQL query to INSERT a record into the database.
sql = ("INSERT INTO EMPLOYEE (FIRST_NAME,LAST_NAME, AGE, SEX, INCOME)  VALUES (%s, %s, %d, %c, %d )")
# %('Windows', 'Ravi', 20, 'M', 12000)
try:
   # Execute the SQL command
   cursor.executemany(sql,records_to_insert)
   # Commit your changes in the database
   db.commit()
   print('After commit')
except:
   # Rollback in case there is any error
   db.rollback()
   print('rollback')
# disconnect from server
db.close()# -*- coding: utf-8 -*-

