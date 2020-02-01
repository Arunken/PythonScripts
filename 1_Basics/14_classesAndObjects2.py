# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 15:22:59 2018

@author: Arken
"""

import classesAndObjects as cobj


a = cobj.Arith()
p = a.summ(3,4)
print(p)


# =========================================================

class DocumentationDemo:
    '''This is a documentation '''

    def msg():
        print('hello arun')
    

a = DocumentationDemo()
a.__doc__

# =========================================================

 
# Class for Computer Science Student
class CSStudent:
    stream = 'cse'                  # Class Variable
    def __init__(self,name,roll):
        self.name = name            # Instance Variable
        self.roll = roll            # Instance Variable
 
# Objects of CSStudent class
a = CSStudent('Geek', 1)
b = CSStudent('Nerd', 2)
print(a.stream)  # prints "cse"
print(b.stream)  # prints "cse"
print(a.name)    # prints "Geek"
print(b.name)    # prints "Nerd"
print(a.roll)    # prints "1"
print(b.roll)    # prints "2"
 
# Class variables can be accessed using class
# name also
print(CSStudent.stream) # prints "cse"s






class Aurobora:
    def __init__(self,name):
        self.name = name
        self.health = 100
        
    def eat(self,food):
        if(food == 'coffee'):
            self.health-=100
        elif(food == 'apple'):
            self.health +=20
        else:
            pass
        
p = Aurobora('arun')
print(p.name)
print(p.health)

p.eat('coffee')
p.eat('apple')
p.eat('biriyani')

print(p.health)
    
# =========================================================
    
class student:
    
    def __init__(self,name):
        self.name = name
        self.attend = 0
        self.grades = []
        print('Hi, my name is {0} and my attendance is {1}'.format(self.name,self.attend))
        
    def addGrade(self,grade):
        self.grades.append(grade)
        
    def attenday(self):
        self.attend +=1
        return self.attend
    
    def av(self):
        return sum(self.grades)/len(self.grades)
    
student1 = student('ravi');
student1.addgrade(90)
student1.addgrade(95)
student1.addgrade(50)
student1.addgrade(95)
student1.addgrade(60)

print(student1.grades)
x = student1.av()
print("Average : ",x)
print(student1.attenday())
print(student1.attenday())

# ===========================================================

class dictionary:
    
    def __init__(self,dictname):
        self.dictname = dictname
        