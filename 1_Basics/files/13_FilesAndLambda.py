# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 15:01:51 2018

@author: Arken
"""
'''
>> Used to read data from a file and write data into a file

fstream = open(filepath,mode,buffering)

======================= Modes =================================================

r : Opens a file for reading only
rb : Opens a file for reading only in binary format
r+ : Opens a file for both reading and writing
rb+ : Opens a file for both reading and writing in binary format
w : Opens a file for writing only
wb : Opens a file for writing only in binary format
w+ : Opens a file for both writing and reading
wb+ : Opens a file for both writing and reading in binary format
a : Opens a file for appending
ab : Opens a file for appending in binary format
a+ : Opens a file for both appending and reading
ab+ : Opens a file for both appending and reading in binary format

======================== Buffering ============================================

0 : no buffering
1 : line buffering
>1 : buffer size
-1 : system default

'''

import sys
sys.getdefaultencoding()

#============= reading a file =================================================
s ='E:\\er.txt'
print(s)

fpath ="/mnt/Soft/Documents/PythonProjects/1_Basics/files/Hello.txt"
f_in = open(fpath,'r',encoding='ascii')
#text = f_in.readlines() # Returns a list with each element as a line from the file
text = f_in.readline() # Returns the next line to be read
text = f_in.read(3) # read only 10 characters
text = f_in.read() # Returns a string of all lines
print(text)


print(f_in.tell()) # Check current position
# seek(position,offset)
f_in.seek(2, 0) # Reposition pointer at the beginning once again
f_in.close()
''' ======offset values=====
>>defaults to 0, which means absolute file positioning
>>1 which means seek relative to the current position 
>>2 means seek relative to the file's end
'''

f_in = open(fpath,'r',encoding='ascii')
for line in f_in:
    print(line)

#=============writing to a file(appending)=====================================
data = input('Enter something to write')
f_out = open(fpath,'a') # use w
f_out.write(data)
f_out.close()



''' =================== file attributes =======================================

f_in.mode: Returns access mode with which file was opened
f_in.name: Returns name of the file.
f_in.closed: Returns true if file is closed, false otherwise

'''
# Refer os module for other file operations

''' ========================== Lambdas ========================================'''

lambda argument: manipulate(argument)

add = lambda x, y: x + y
print(add(3, 5))

#=================

def dothis(x):
    return lambda y:x+y

hello = dothis(4)
print(hello(5))
    

#=================
def fun(x,y):
    return x+y

add=fun
add(23,5)
#=================

a = [(1, 2), (4, 1), (9, 10), (13, -3)]
a.sort(key=lambda x: x[1])
print(a)
 
a.sort(key=lambda x: x[1],reverse=True) # sort in the reverse order
print(a)   

sorted(a, key=lambda x: x[1], reverse=True)
    
    
    
    












