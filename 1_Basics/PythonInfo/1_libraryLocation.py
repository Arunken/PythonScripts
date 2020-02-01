# -*- coding: utf-8 -*-
"""
Created on Fri May 18 17:38:00 2018

@author: SilverDoe
"""

# Get python library location

from distutils.sysconfig import get_python_lib
print(get_python_lib())



# Get path of a python module

import openpyxl

print(openpyxl.__file__)

# Get path of a python module

import openpyxl
import os
path = os.path.dirname(openpyxl.__file__)
print(path)


"""
The inspect module provides several useful functions to help get information
 about live objects such as modules, classes, methods, functions, tracebacks,
 frame objects, and code objects. For example, it can help you examine the 
 contents of a class, retrieve the source code of a method, extract and format
 the argument list for a function, or get all the information you need to 
 display a detailed traceback
"""

import os
import inspect

inspect.getfile(os) # gets the directory of the module
inspect.getfile(inspect)
os.path.dirname(inspect.getfile(inspect))