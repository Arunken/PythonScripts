# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 12:21:27 2018

@author: Ourabora
"""
'''
https://www.tutorialspoint.com/python/python_database_access.htm

'''
import sqlite3

# create or open database
conn = sqlite3.connect('/home/arken/trashdata/mydb1.db')

# create table if it doesn't exist
conn.execute('''CREATE TABLE IF NOT EXISTS STUDENT(ROLLNO INT 
               NOT NULL,NAME TEXT NOT NULL,AGE INT NOT NULL)''')

#insert data in to the table
conn.execute('''INSERT INTO STUDENT VALUES(3,'Sam',26)''')
conn.execute('''INSERT INTO STUDENT(ROLLNO,NAME,AGE) VALUES(23,'Sam',23)''')

# commit the data
conn.commit()


# fetch data from the table
cursor = conn.execute("SELECT ROLLNO,NAME,AGE FROM STUDENT")

# iterating over the cursor
for row in cursor:
    print("Roll No :",row[0])
    print("Name :",row[1])
    print("Age :",row[2])
    
   
    
conn.execute("UPDATE STUDENT SET AGE=23 WHERE ROLLNO=1")
conn.commit()


conn.execute("DELETE FROM STUDENT WHERE ROLLNO=32")
conn.commit()
conn.close()


