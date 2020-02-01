# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 15:43:53 2018

@author: Ourabora
"""

def out_fn(msg):
    message = msg
    print('outer function called')
    def inner_fun():
        print(message)
    return inner_fun  # remove the () / give arguments and show

hi_func = out_fn('hi')


hi_func()






def decorator_function(original_function):
    def wrapper_function():
        return original_function
    
    return wrapper_function

def display():
    print('display function ran')
    
decorated_display = decorator_function(display)
decorated_display()