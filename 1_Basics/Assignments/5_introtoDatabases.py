# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 16:45:32 2018

@author: Kenrig
"""

#1) ===========



import sqlite3

conn = sqlite3.connect('vehicles.db')

cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Cars(ID INT NOT NULL,NAME TEXT NOT NULL,MAKE INT NOT NULL,PRICE INT NOT NULL);''')

cursor.execute('''INSERT INTO Cars(ID,NAME,MAKE,PRICE) VALUES(1,'Alto',2008,2000)''')
cursor.execute('''INSERT INTO Cars(ID,NAME,MAKE,PRICE) VALUES(2,'Swift',2010, 9000)''')
cursor.execute('''INSERT INTO Cars(ID,NAME,MAKE,PRICE) VALUES(3,'Santro',2017,4000)''')

conn.commit()


c = cursor.execute("SELECT ID,NAME,MAKE,PRICE FROM CARS")
for row in c:
    print("ID :",row[0])
    print("Name :",row[1])
    print("MAKE :",row[2])
    print("PRICE :",row[3]) 
 
x = cursor.execute("UPDATE Cars SET PRICE=4480 WHERE ID=2")
conn.commit()
print('No. of rows affected : ',x.rowcount)

cursor = conn.execute("SELECT ID,NAME,MAKE,PRICE FROM CARS")
print('====== new values after updation======')
for row in cursor:
    print("ID :",row[0])
    print("Name :",row[1])
    print("MAKE :",row[2])
    print("PRICE :",row[3]) 


conn.execute("DELETE FROM Cars WHERE MAKE<2010")
conn.commit()

cursor = conn.execute("SELECT ID,NAME,MAKE,PRICE FROM CARS")
print('====== new values after deletion======')
for row in cursor:
    print("ID :",row[0])
    print("Name :",row[1])
    print("MAKE :",row[2])
    print("PRICE :",row[3]) 
    
conn.close()






# ====================dict cursor 
import sqlite3
import psycopg2 # conda install psycopg2
from psycopg2 import pool, extras
 # they are not imported automatically if not needed. This is standard Python practice.


conn = psycopg2.connect('vehicles1.db')

dict_cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
dict_cur.execute('''INSERT INTO Cars (ID,NAME,MAKE,PRICE) VALUES(10,'trev',2008,2000)''')
dict_cur.execute("SELECT * FROM Cars")
record = dict_cur.fetchone()
print(record['ID'])
print(record['NAME'])
print(record['MAKE'])
