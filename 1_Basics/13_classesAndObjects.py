# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 14:39:34 2018

@author: Arken
"""

class Python:
    
    def __init__(self):
        pass
    
    # internal function
    def maid():
        print('I am working here')
        
    #     
    def disp(self):
        print('hello world')
    
    def disp1(self):
        print('How are you')
        
    def disp2(self):
        print('presumptious')

        
o1 = Python() #object creation
o1.disp()  
o1.maid() # internal function cannot be called from outside     

# =========================================================

class Ph:
    def __init__(self):
        self.y = 5
        self.b = 7 # scope is global
        c = 10 # scope is local
        
    #c = 10 
    
    def method1(self):
        print('I am method1')
        print(c)
        
    def method2(self):
        print('I am method2')
        print(self.y)
        
        
x = Ph()
x.y
x.b
x.c
x.method1()
x.method2()

# =========================================================

class Arith:
    def summ(self,x,y):
        c = x+y
        return c
    
    def diff(self,x,y):
        c = x-y
        return c



# =========================================================

        
        