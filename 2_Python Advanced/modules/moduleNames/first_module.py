# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 21:19:49 2018

@author: SilverDoe
"""
'''
Whenever python runs a file it sets a few special variables and __name__ is one
of them. If the file is run directly then the name variable value is set as __main__
'''



def fun():
    print("First module name : {}".format(__name__))

# this checks whether this file is run directly...i.e if the value in name variable is __main__
if __name__ =='__main__': 
    print("first_module is run directly")
    fun()