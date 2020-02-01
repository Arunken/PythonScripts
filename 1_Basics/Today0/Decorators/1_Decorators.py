# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 12:40:42 2018

@author: Ourabora
"""


# decorators wrap a function, modifying its behavior

def my_decorator(some_function):

    def wrapper():

        print("Something is happening before some_function() is called.")

        some_function()

        print("Something is happening after some_function() is called.")

    return wrapper


def just_me():
    print("Wheee!")


just_some_function = my_decorator(just_me)

just_some_function()


# Python allows you to simplify the calling of decorators using the @ symbol (this is called “pie” syntax)

@my_decorator
def fun1():
    print("hello  there!")

fun1()
