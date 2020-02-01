# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 23:49:24 2018

@author: SilverDoe
"""

class Student:
    
    __stream = 'ece'    # Hidden variable
    college  = 'gcek' # Class variable
              
    def __init__(self,name,roll):
        self.name = name            # Instance Variable
        self.roll = roll            # Instance Variable
 

a = Student('Geek', 1)
a.__stream # error cannot access the variable
a.college

b = Student('Geek', 1)     
print(b._Student__stream) # Nothing in Python is truly private


#==============================================================================


def display(): 
    x = 20 # encapsilation
    y = 30
    z = x+y
    return z
    
n = display()
print(n)















