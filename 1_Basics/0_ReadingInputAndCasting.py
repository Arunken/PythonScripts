# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 12:25:51 2018

@author: Ourabora

Execute Python source file in commandline :-

>> Open python commandline and type exec(open(pathToFile).read())




"""



# reading input from the keyboard

x = input('enter an input :  ') # input will be read as string
print(x)

# casting values

a = int(x)
b = float(x)
c = str(x)


"""

Python as a programming language has no saying about if it's an compiled or interpreted
 programming language, only the implementation of it. The terms interpreted or compiled 
 is not a property of the language but a property of the implementation. Python program 
 runs directly from the source code . so, Python will fall under byte code interpreted. 
 The .py source code is first compiled to byte code as .pyc. This byte code can be 
 interpreted (official CPython), or JIT compiled (PyPy). Python source code (.py) can be
 compiled to different byte code also like IronPython (.Net) or Jython (JVM). There are 
 multiple implementations of Python language . The official one is a byte code interpreted
 one. There are byte code JIT compiled implementations too.

"""