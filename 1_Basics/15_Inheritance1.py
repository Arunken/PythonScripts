# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 15:02:46 2018

@author: Arken
"""

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return 'My name is {0} and I am {1} years old'.format(self.name,self.age)
    
    def printperson(self):
        return ('I am a person')
    
    
class animal:
    def __init__(self, species):
        self.species = species
    
    def __str__(self):
        return 'I belong to {0} species'.format(self.species)
    
    def printperson(self):
        return ('I am an animal')
    
class Military(animal,Person):
    def __init__(self,name,age,species,rank):
        Person.__init__(self,name,age)
        animal.__init__(self,species)
        self.rank = rank
        
    def __str__(self):
        return Person.__str__(self)+' '+animal.__str__(self)+' '+'I am a {0}'.format(self.rank)
    
    
p = Person('Arun',26)
print(p)

ani = animal('Human')
print(ani)

mil = Military(p.name,p.age,ani.species,'major')
print(mil)



#===================   constructor  ===========================================

class parent:
    
    def __init__(self):
        print("parent constructor")


class child(parent):
    
    def __init__(self):
        print("child constructor")
        parent.__init__(self)
        
c = child()


#==================   attributes ==============================================

class Employee:

   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)


emp1 = Employee("Zara", 2000)

emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print ("Total Employee %d" % Employee.empCount)

emp1.age = 27  # Add an 'age' attribute.
print(emp1.age)
emp1.name = 'xyz'  # Modify 'name' attribute.
del emp1.salary  # Delete 'salary' attribute.


#=============  built-in class attributes   ===================================

class Employee:
   'Common base class for all employees'

   def __init__(self):
      pass


emp1 = Employee()
print ("Employee.__doc__:", Employee.__doc__)  # Class documentation string or none, if undefined.
print ("Employee.__name__:", Employee.__name__) # Class name.
print ("Employee.__module__:", Employee.__module__) # Module name in which the class is defined. This attribute is "__main__" in interactive mode.
print ("Employee.__bases__:", Employee.__bases__) # A possibly empty tuple containing the base classes, in the order of their occurrence in the base class list.
print ("Employee.__dict__:", Employee.__dict__ ) # Dictionary containing the class's namespace
    
    
#=================  Destructor ================================================

class Point:
   def __init__( self, x=0, y=0):
      self.x = x
      self.y = y
   def __del__(self):
      class_name = self.__class__.__name__
      print (class_name, "destroyed")

pt1 = Point()
pt2 = pt1
pt3 = pt1
print (id(pt1), id(pt2), id(pt3))   # prints the ids of the objects
del pt1
del pt2
del pt3
    
    
    
""" 

>>> Python deletes unneeded objects (built-in types or class instances) automatically to free the memory space.
    The process by which Python periodically reclaims blocks of memory that no longer are in use is termed as 
    Garbage Collection.
 
>>> Python's garbage collector runs during program execution and is triggered when an object's reference count 
    reaches zero. An object's reference count changes as the number of aliases that point to it changes.
    
>>> An object's reference count increases when it is assigned a new name or placed in a container 
    (list, tuple, or dictionary). The object's reference count decreases when it is deleted with del, 
    its reference is reassigned, or its reference goes out of scope. When an object's reference count 
    reaches zero, Python collects it automatically.
 
"""
a = 40      # Create object <40>
b = a       # Increase ref. count  of <40> 
c = [b]     # Increase ref. count  of <40> 

del a       # Decrease ref. count  of <40>
b = 100     # Decrease ref. count  of <40> 
c[0] = -1   # Decrease ref. count  of <40> 


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    