# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 14:02:05 2018

@author: SilverDoe
"""

# Module For Connecting To MySQL database
import MySQLdb as mysql

# connect
db=mysql.connect( host="localhost", port=3307, user="root", passwd="root", db="sakila")
print(db)

# insert data





# select data
db.query("""SELECT spam, eggs, sausage FROM breakfast WHERE price < 5""")




