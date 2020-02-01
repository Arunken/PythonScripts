# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 12:40:42 2018

@author: Ourabora
"""

def parent():
    print("Printing from the parent() function.")

    def first_child():
        print( "Printing from the first_child() function.")

    def second_child():
        first_child()
        print("Printing from the second_child() function.")
    second_child()

    #print(first_child())
    #print(second_child())
    
parent()

