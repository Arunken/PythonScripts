# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 21:23:19 2018

@author: SilverDoe
"""

'''
here the first module is run indirectly from here as it is imported and so 
the name of it is not __main__ but that of but that of second module is...

also since the name of the first_module is not main the condition given in the 
if construct is false

'''
import first_module

first_module.fun()

print("Second module name : {}".format(__name__))