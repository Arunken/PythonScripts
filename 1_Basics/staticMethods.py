# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 23:44:45 2018

@author: SilverDoe
"""

# allows you only to access the static variables in the same class

class Example:
    name = "Example"

    @staticmethod
    def static():
        print("%s static() called" % Example.name)

class Offspring1(Example):
    name = "Offspring1"

class Offspring2(Example):
    name = "Offspring2"

    @staticmethod
    def static():
        print("%s static() called" % Offspring2.name)

Example.static() # prints Example
Offspring1.static() # prints Example
Offspring2.static() # prints Offspring2

#==============================================================================
# in this approach you’ll be able to modify class variables of the subclasses 
# without the neccessity of redefining the method when using inheritance

class Example:
    name = "Example"

    @classmethod
    def static(cls): 
        print("%s static() called" % cls.name)

class Offspring1(Example):
    name = "Offspring1"
    

class Offspring2(Example):
    name = "Offspring2"

    @classmethod
    def static(cls):
        print("%s static() called" % cls.name)

Example.static()    # prints Example
Offspring1.static() # prints Offspring1
Offspring2.static() # prints Offspring2 