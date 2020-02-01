# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 11:09:02 2018

@author: Ourabora
"""

# Python Generators Practice

def vowels():
    yield "a"
    yield "e"
    yield "i"
    yield "o"
    yield "u"

for i in vowels():
    print(i)
    
    
def myfun():
    for i in range(10):
        print(i)
        
myfun()
myfun()